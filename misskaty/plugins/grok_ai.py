# ============================================================
#  Edith — Grok AI  (/ai , /ask)
#  Owner : Mister Stark
#  Grok model + API key  ->  misskaty/vars.py  (GROK_API_KEY, GROK_MODEL)
# ============================================================
import html
import re
from logging import getLogger

import httpx
from cachetools import TTLCache
from pyrogram import enums, filters
from pyrogram.types import Message

from misskaty import app
from misskaty.ui.help_texts import AI_HELP
from misskaty.vars import COMMAND_HANDLER, GROK_API_KEY, GROK_BASE_URL, GROK_MODEL

LOGGER = getLogger("Edith.GrokAI")

__MODULE__ = "Edith AI"
from misskaty.ui.help_texts import HELP_TEXTS  # noqa: E402

__HELP__ = HELP_TEXTS["ai_help"]

SYSTEM_AI = (
    "You are Edith, a smart and friendly Telegram assistant created by Mister Stark. "
    "Reply in the same language the user writes in. Keep answers clear and reasonably short."
)
SYSTEM_ASK = (
    "You are Edith, an assistant created by Mister Stark. Answer the question directly "
    "and accurately in the user's language. Be concise."
)

_cooldown = TTLCache(maxsize=2048, ttl=8)
_history = TTLCache(maxsize=1024, ttl=1800)  # /ai short-term memory per user


def _to_html(text: str) -> str:
    """Grok markdown -> Telegram HTML."""
    text = html.escape(text.strip())
    text = re.sub(r"```(?:\w+)?\n?(.*?)```", lambda m: f"<pre>{m.group(1).strip()}</pre>", text, flags=re.S)
    text = re.sub(r"`([^`\n]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text, flags=re.S)
    text = re.sub(r"^#{1,6}\s*(.+)$", r"<b>\1</b>", text, flags=re.M)
    return text


def _chunks(text: str, size: int = 3800):
    while text:
        if len(text) <= size:
            yield text
            return
        cut = text.rfind("\n", 0, size)
        cut = cut if cut > 0 else size
        yield text[:cut]
        text = text[cut:].lstrip("\n")


async def _grok(messages: list) -> str:
    if not GROK_API_KEY or not GROK_MODEL:
        raise RuntimeError("Grok API key / model vars.py me set nahi hai.")
    async with httpx.AsyncClient(timeout=90) as http:
        r = await http.post(
            f"{GROK_BASE_URL.rstrip('/')}/chat/completions",
            headers={"Authorization": f"Bearer {GROK_API_KEY}", "Content-Type": "application/json"},
            json={"model": GROK_MODEL, "messages": messages},
        )
    if r.status_code != 200:
        raise RuntimeError(f"Grok API error {r.status_code}: {r.text[:200]}")
    return r.json()["choices"][0]["message"]["content"]


def _prompt(message: Message) -> str:
    parts = []
    if message.reply_to_message:
        rt = message.reply_to_message
        quoted = rt.text or rt.caption
        if quoted:
            parts.append(f"[Replied message]\n{quoted}")
    if len(message.command) > 1:
        parts.append(message.text.split(None, 1)[1])
    return "\n\n".join(parts).strip()


async def _run(message: Message, system: str, remember: bool):
    uid = message.from_user.id if message.from_user else message.chat.id
    if uid in _cooldown:
        return await message.reply_text("⏳ <b>Thoda ruko, 8 second baad dobara try karo.</b>", parse_mode=enums.ParseMode.HTML)
    prompt = _prompt(message)
    if not prompt:
        return await message.reply_text(
            f"❌ <b>Sawal likho ya kisi message ko reply karo.</b>\n<code>/{message.command[0]} your question</code>",
            parse_mode=enums.ParseMode.HTML,
        )
    _cooldown[uid] = True
    wait = await message.reply_text("🤖 <b>Soch raha hu...</b>", parse_mode=enums.ParseMode.HTML)
    msgs = [{"role": "system", "content": system}]
    if remember:
        msgs += _history.get(uid, [])
    msgs.append({"role": "user", "content": prompt})
    try:
        answer = await _grok(msgs)
    except Exception as e:
        LOGGER.error("Grok error: %s", e)
        return await wait.edit_text(f"❌ <b>AI error:</b> <code>{html.escape(str(e))[:300]}</code>", parse_mode=enums.ParseMode.HTML)
    if remember:
        hist = _history.get(uid, []) + [{"role": "user", "content": prompt}, {"role": "assistant", "content": answer}]
        _history[uid] = hist[-8:]
    first = True
    for part in _chunks(_to_html(answer)):
        body = f"<blockquote expandable>{part}</blockquote>"
        try:
            if first:
                await wait.edit_text(body, parse_mode=enums.ParseMode.HTML)
            else:
                await message.reply_text(body, parse_mode=enums.ParseMode.HTML)
        except Exception:
            plain = html.unescape(re.sub(r"<[^>]+>", "", part))
            if first:
                await wait.edit_text(plain)
            else:
                await message.reply_text(plain)
        first = False


@app.on_message(filters.command("ai", COMMAND_HANDLER))
async def ai_cmd(_, message: Message):
    await _run(message, SYSTEM_AI, remember=True)


@app.on_message(filters.command("ask", COMMAND_HANDLER))
async def ask_cmd(_, message: Message):
    await _run(message, SYSTEM_ASK, remember=False)
