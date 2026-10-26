# ============================================================
#  EDITH — URL Bypass / Direct Link  (/directurl , /bypass)
#
#  Kya karta hai:
#   - Short link (bit.ly, we.tl, tinyurl ...) ko final URL tak kholta hai
#   - Google Drive / Dropbox / GitHub link ko direct-download link me badalta hai
#   - MediaFire, Pling, WeTransfer ka direct link nikalne ki koshish karta hai
#   - Baaki kisi bhi link ka final URL + file name/size/type batata hai
# ============================================================
import base64
import html
import re
import urllib.parse
from logging import getLogger
from urllib.parse import unquote

from pyrogram import enums, filters
from pyrogram import types as pyro_types
from pyrogram.types import Message

from misskaty import app
from misskaty.core.decorator.errors import capture_err
from misskaty.helper import fetch, get_readable_file_size
from misskaty.ui import buttons as UIB
from misskaty.ui.help_texts import HELP_TEXTS
from misskaty.vars import COMMAND_HANDLER

LOGGER = getLogger("Edith.Bypass")

__MODULE__ = "Bypass"
__HELP__ = HELP_TEXTS["bypass_help"]

HTML = enums.ParseMode.HTML
NO_PREVIEW = pyro_types.LinkPreviewOptions(is_disabled=True)
BROWSER_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


# ---------------------------------------------------------------- pure URL rewrites (no network)
def gdrive_direct(url: str):
    m = re.search(r"drive\.google\.com/(?:file/d/|open\?id=|uc\?(?:export=\w+&)?id=)([\w-]{10,})", url) or re.search(
        r"docs\.google\.com/uc\?(?:export=\w+&)?id=([\w-]{10,})", url
    )
    return f"https://drive.google.com/uc?export=download&id={m[1]}" if m else None


def dropbox_direct(url: str):
    if not re.search(r"(?:www\.)?dropbox\.com/", url):
        return None
    parts = urllib.parse.urlsplit(url)
    query = dict(urllib.parse.parse_qsl(parts.query, keep_blank_values=True))
    query.pop("dl", None)
    query.pop("raw", None)
    query["dl"] = "1"
    return urllib.parse.urlunsplit(parts._replace(query=urllib.parse.urlencode(query)))


def github_direct(url: str):
    m = re.match(r"https?://github\.com/([^/]+)/([^/]+)/blob/(.+)", url)
    return f"https://raw.githubusercontent.com/{m[1]}/{m[2]}/{m[3].split('?')[0]}" if m else None


def mediafire_extract(page_html: str):
    m = re.search(r'data-scrambled-url="([^"]+)"', page_html)
    if m:
        try:
            return base64.b64decode(m[1]).decode()
        except Exception:
            pass
    m = re.search(r'href="(https?://download[^"]*mediafire\.com/[^"]+)"', page_html)
    return html.unescape(m[1]) if m else None


# ---------------------------------------------------------------- network helpers
async def pling_bypass(url: str):
    pid = re.search(r"https?://(?:store\.kde\.org|www\.pling\.com)/p/(\d+)", url)
    if not pid:
        return None
    res = await fetch.get(f"https://www.pling.com/p/{pid[1]}/loadFiles", headers=BROWSER_HEADERS)
    files = res.json().get("files") or []
    if not files:
        return None
    return [(f["name"], unquote(f["url"]), int(f.get("size") or 0)) for f in files]


async def wetransfer_bypass(url: str):
    if url.startswith("https://we.tl/"):
        r = await fetch.get(url, headers=BROWSER_HEADERS, follow_redirects=True)
        url = str(r.url)
    params = urllib.parse.urlparse(url).path.split("/")[2:]
    if len(params) == 2:
        transfer_id, security_hash = params
        recipient_id = None
    elif len(params) == 3:
        transfer_id, recipient_id, security_hash = params
    else:
        return None
    payload = {"intent": "entire_transfer", "security_hash": security_hash}
    if recipient_id:
        payload["recipient_id"] = recipient_id
    r = await fetch.get("https://wetransfer.com/", headers=BROWSER_HEADERS)
    m = re.search(r'name="csrf-token" content="([^"]+)"', r.text)
    if not m:
        return None
    r = await fetch.post(
        f"https://wetransfer.com/api/v4/transfers/{transfer_id}/download",
        json=payload,
        headers={**BROWSER_HEADERS, "x-csrf-token": m[1], "x-requested-with": "XMLHttpRequest"},
    )
    return r.json().get("direct_link")


async def probe(url: str):
    """Redirects follow karke final url + file info (name, size, type) nikalta hai."""
    info = {"final": url, "hops": 0, "name": None, "size": None, "type": None}
    try:
        resp = await fetch.get(url, headers=BROWSER_HEADERS, follow_redirects=True, timeout=25)
    except Exception as e:
        raise RuntimeError(f"Could not open the link: {e}") from e
    info["final"] = str(resp.url)
    info["hops"] = len(resp.history)
    info["type"] = (resp.headers.get("content-type") or "").split(";")[0].strip() or None
    cl = resp.headers.get("content-length")
    info["size"] = int(cl) if cl and cl.isdigit() else None
    cd = resp.headers.get("content-disposition") or ""
    m = re.search(r"filename\*?=(?:UTF-8'')?\"?([^\";]+)", cd)
    if m:
        info["name"] = unquote(m[1])
    elif info["type"] and not info["type"].startswith("text/html"):
        info["name"] = unquote(urllib.parse.urlparse(info["final"]).path.rsplit("/", 1)[-1]) or None
    info["is_page"] = bool(info["type"] and info["type"].startswith("text/html"))
    info["html"] = resp.text if info["is_page"] else ""
    return info


async def resolve(url: str) -> dict:
    """Return {"links": [(name, url, size)], "note": str}"""
    if not re.match(r"https?://", url, re.I):
        url = "https://" + url
    host = (urllib.parse.urlparse(url).hostname or "").lower()
    note = ""

    # 1) deterministic rewrites
    direct = gdrive_direct(url) or github_direct(url) or dropbox_direct(url)
    if direct:
        return {"links": [(None, direct, None)], "note": "Direct download link generated.", "source": url}

    # 2) site specific
    if "pling.com" in host or host == "store.kde.org":
        files = await pling_bypass(url)
        if files:
            return {"links": files, "note": "", "source": url}
        note = "Pling files could not be fetched (site may have changed).\n"
    if host == "we.tl" or "wetransfer.com" in host:
        dl = await wetransfer_bypass(url)
        if dl:
            return {"links": [(None, dl, None)], "note": "", "source": url}
        note = "WeTransfer link could not be resolved (site may have changed).\n"

    # 3) generic: follow redirects (+ mediafire page parsing)
    info = await probe(url)
    if "mediafire.com" in (urllib.parse.urlparse(info["final"]).hostname or "") and info["is_page"]:
        dl = mediafire_extract(info["html"])
        if dl:
            return {"links": [(None, dl, None)], "note": "", "source": url}
        note += "MediaFire direct link not found on the page.\n"
    if info["is_page"]:
        extra = "Final page opened — this is a web page, not a direct file." if not note else ""
        return {"links": [(None, info["final"], None)], "note": (note + extra).strip(), "source": url, "page": True}
    return {
        "links": [(info["name"], info["final"], info["size"])],
        "note": f"Redirects followed: {info['hops']}" if info["hops"] else "",
        "source": url,
        "type": info["type"],
    }


def format_result(res: dict, mention: str) -> str:
    lines = [f"<b>🔗 Source Link:</b>\n<code>{html.escape(res['source'])}</code>\n"]
    lines.append("<b>✅ Direct Link:</b>" if not res.get("page") else "<b>📄 Final Link:</b>")
    for name, link, size in res["links"][:15]:
        label = html.escape(name) if name else "Open link"
        extra = f" ({get_readable_file_size(size)})" if size else ""
        lines.append(f"→ <a href=\"{html.escape(link, quote=True)}\">{label}</a>{extra}")
        if len(link) < 700:
            lines.append(f"<code>{html.escape(link)}</code>")
    if res.get("type"):
        lines.append(f"\n<b>Type:</b> <code>{html.escape(res['type'])}</code>")
    if res.get("note"):
        lines.append(f"\n<i>{html.escape(res['note'])}</i>")
    lines.append(f"\n{mention}")
    return "\n".join(lines)


@app.on_message(filters.command(["directurl", "bypass"], COMMAND_HANDLER))
@capture_err
async def bypass(_, ctx: Message):
    url = None
    if len(ctx.command) > 1:
        url = ctx.command[1]
    elif ctx.reply_to_message and (ctx.reply_to_message.text or ctx.reply_to_message.caption):
        m = re.search(r"https?://\S+", ctx.reply_to_message.text or ctx.reply_to_message.caption)
        url = m[0] if m else None
    if not url:
        return await ctx.reply_text(
            f"Usage: <code>/{ctx.command[0]} [link]</code> or reply to a message containing a link.\n"
            "Works with short links, Google Drive, Dropbox, GitHub, MediaFire, Pling and WeTransfer.",
            parse_mode=HTML,
        )
    msg = await ctx.reply_text("⏳ Resolving URL...", parse_mode=HTML)
    mention = f"<b>Requested by:</b> {ctx.from_user.mention} (<code>{ctx.from_user.id}</code>)" if ctx.from_user else ""
    try:
        res = await resolve(url)
    except Exception as e:
        LOGGER.error("bypass failed: %s", e)
        return await msg.edit_text(f"❌ <b>Failed:</b> <code>{html.escape(str(e))[:300]}</code>", parse_mode=HTML)
    first_link = res["links"][0][1]
    markup = UIB.bypass_open(link=first_link) if len(first_link) < 1900 else None
    await msg.edit_text(format_result(res, mention), parse_mode=HTML, link_preview_options=NO_PREVIEW, reply_markup=markup)
    
