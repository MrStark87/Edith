# ============================================================
#  EDITH — OCR  (/ocr)
#  Photo / sticker / image document se text nikalta hai (OCR.space API).
#  Key -> misskaty/vars.py (OCR_SPACE_API_KEY)
# ============================================================
import html
import io
import re
from logging import getLogger

from PIL import Image
from pyrogram import enums, filters
from pyrogram.types import Message

from misskaty import app
from misskaty.core.decorator.errors import capture_err
from misskaty.helper import fetch
from misskaty.ui.help_texts import HELP_TEXTS
from misskaty.vars import COMMAND_HANDLER, OCR_SPACE_API_KEY

LOGGER = getLogger("Edith.OCR")

__MODULE__ = "OCR"
__HELP__ = HELP_TEXTS["ocr_help"]

OCR_URL = "https://api.ocr.space/parse/image"
MAX_BYTES = 1000 * 1024  # OCR.space free plan: max 1 MB
HTML = enums.ParseMode.HTML


def _prepare_image(raw: bytes) -> bytes:
    """Kisi bhi image (webp/png/jpg) ko JPEG me badalta hai aur 1 MB ke neeche laata hai."""
    img = Image.open(io.BytesIO(raw))
    if img.mode != "RGB":
        bg = Image.new("RGB", img.size, "white")
        bg.paste(img.convert("RGBA"), mask=img.convert("RGBA").split()[-1])
        img = bg
    longest = max(img.size)
    if longest > 2400:
        ratio = 2400 / longest
        img = img.resize((int(img.width * ratio), int(img.height * ratio)))
    quality = 90
    while True:
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=quality)
        if buf.tell() <= MAX_BYTES or quality <= 40:
            return buf.getvalue()
        quality -= 10
        if quality < 60:
            img = img.resize((int(img.width * 0.8), int(img.height * 0.8)))


async def run_ocr(image_bytes: bytes, language: str = "eng") -> str:
    """OCR.space ko image bhejta hai aur text lautata hai. Error par Exception raise karta hai."""
    if not OCR_SPACE_API_KEY:
        raise RuntimeError("OCR_SPACE_API_KEY is not set in misskaty/vars.py")
    resp = await fetch.post(
        OCR_URL,
        data={
            "apikey": OCR_SPACE_API_KEY,
            "language": language,
            "isOverlayRequired": "false",
            "scale": "true",
            "detectOrientation": "true",
        },
        files={"file": ("image.jpg", image_bytes, "image/jpeg")},
        timeout=90,
    )
    if resp.status_code != 200:
        raise RuntimeError(f"OCR server error {resp.status_code}")
    data = resp.json()
    if data.get("IsErroredOnProcessing"):
        err = data.get("ErrorMessage") or data.get("ErrorDetails") or "unknown error"
        if isinstance(err, list):
            err = ", ".join(map(str, err))
        raise RuntimeError(str(err))
    results = data.get("ParsedResults") or []
    return "\n".join((r.get("ParsedText") or "").strip() for r in results).strip()


@app.on_message(filters.command(["ocr"], COMMAND_HANDLER))
@capture_err
async def ocr(_, ctx: Message):
    reply = ctx.reply_to_message
    is_image_doc = bool(reply and reply.document and (reply.document.mime_type or "").startswith("image"))
    if not reply or not (reply.photo or reply.sticker or is_image_doc):
        return await ctx.reply_text(
            f"❌ Reply to a photo, sticker or image with <code>/{ctx.command[0]}</code>\n"
            f"Optional language: <code>/{ctx.command[0]} hin</code> (default: eng)",
            parse_mode=HTML,
        )
    if reply.sticker and (reply.sticker.is_animated or reply.sticker.is_video):
        return await ctx.reply_text("❌ Animated / video stickers are not supported.", parse_mode=HTML)

    language = "eng"
    if len(ctx.command) > 1 and re.fullmatch(r"[a-zA-Z]{3}", ctx.command[1]):
        language = ctx.command[1].lower()

    msg = await ctx.reply_text("🔍 Scanning your image...", parse_mode=HTML)
    try:
        media = await reply.download(in_memory=True)
        raw = bytes(media.getbuffer()) if hasattr(media, "getbuffer") else bytes(media)
        text = await run_ocr(_prepare_image(raw), language)
    except Exception as e:
        LOGGER.error("OCR failed: %s", e)
        return await msg.edit_text(f"❌ <b>OCR failed:</b> <code>{html.escape(str(e))[:300]}</code>", parse_mode=HTML)

    if not text:
        return await msg.edit_text("⚠️ No text found in this image.", parse_mode=HTML)
    if len(text) > 3500:
        doc = io.BytesIO(text.encode("utf-8"))
        doc.name = "ocr.txt"
        await msg.delete()
        return await ctx.reply_document(doc, caption="🔍 OCR result", parse_mode=HTML)
    await msg.edit_text(f"🔍 <b>OCR result:</b>\n<blockquote expandable><code>{html.escape(text)}</code></blockquote>", parse_mode=HTML)
                                                                
