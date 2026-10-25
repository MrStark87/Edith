# ============================================================
#  EDITH — Start / Help / Privacy  (logic only)
#  Owner : Mister Stark
#  Texts  -> misskaty/ui/help_texts.py
#  Buttons -> misskaty/ui/buttons.py
# ============================================================
import contextlib
import html
import re

from cachetools import TTLCache

from pyrogram import enums, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import CallbackQuery, InputMediaPhoto, InputRichMessage, LinkPreviewOptions, Message, ReplyParameters

from database.users_chats_db import db as mk_db
from misskaty import BOT_USERNAME, app
from misskaty.edith import db as edith_db
from misskaty.helper import bot_sys_stats
from misskaty.ui import buttons as B
from misskaty.ui.help_texts import (
    GROUP_HELP_TEXT,
    GROUP_START_TEXT,
    HELP_CATEGORY_TEXT,
    HELP_MENU_TEXT,
    HELP_NOT_FOUND_TEXT,
    HELP_TABLES,
    HELP_TEXTS,
    PRIVACY_TEXT,
    START_TEXT,
)
from misskaty.vars import (
    COMMAND_HANDLER,
    PRIVACY_IMAGE,
    PRIVACY_POLICY_URL,
    START_IMAGE,
    SUPPORT_GROUP,
    UPDATE_CHANNEL,
)

HTML = enums.ParseMode.HTML
BOT_LINK = f"https://t.me/{BOT_USERNAME}"
CAPTION_LIMIT = 1000  # telegram photo caption limit ~1024


def _plain_len(text: str) -> int:
    plain = html.unescape(re.sub(r"<[^>]+>", "", text))
    return len(plain.encode("utf-16-le")) // 2


def _start_text(user: str) -> str:
    return START_TEXT.format(user=html.escape(user), bot_link=BOT_LINK, privacy_url=PRIVACY_POLICY_URL)


async def render(msg: Message, text: str, markup):
    """Photo + caption me dikhata hai; text caption limit se bada ho to normal text message."""
    chat_id = msg.chat.id
    fits = _plain_len(text) <= CAPTION_LIMIT
    if fits and msg.photo:
        return await msg.edit_media(
            InputMediaPhoto(media=START_IMAGE, caption=text, parse_mode=HTML), reply_markup=markup
        )
    if fits:
        await msg.delete()
        return await app.send_photo(chat_id, START_IMAGE, caption=text, reply_markup=markup, parse_mode=HTML)
    nopreview = LinkPreviewOptions(is_disabled=True)
    if msg.photo:
        await msg.delete()
        return await app.send_message(chat_id, text, reply_markup=markup, parse_mode=HTML, link_preview_options=nopreview)
    return await msg.edit_text(text, reply_markup=markup, parse_mode=HTML, link_preview_options=nopreview)


async def send_doc(chat_id: int, key: str, markup, reply_to: int = None):
    """Help ko table (rich message) me bhejta hai; fail ho to Edith plain text me."""
    try:
        return await app.send_rich_message(
            chat_id,
            rich_message=InputRichMessage(html=HELP_TABLES[key]),
            reply_markup=markup,
            reply_parameters=ReplyParameters(message_id=reply_to) if reply_to else None,
        )
    except Exception:
        return await app.send_message(
            chat_id,
            HELP_TEXTS.get(key, HELP_NOT_FOUND_TEXT),
            reply_markup=markup,
            parse_mode=HTML,
            link_preview_options=LinkPreviewOptions(is_disabled=True),
        )


async def show_text(msg: Message, text: str, markup):
    """Menu / category: text message jo usi message me edit hota rehta hai.

    Sirf start ka photo message pehli baar replace hota hai (photo ko text me edit nahi kar sakte).
    """
    nopreview = LinkPreviewOptions(is_disabled=True)
    chat_id = msg.chat.id
    if not msg.photo:
        try:
            return await app.edit_message_text(
                chat_id, msg.id, text=text, reply_markup=markup, parse_mode=HTML, link_preview_options=nopreview
            )
        except Exception:
            pass
    with contextlib.suppress(Exception):
        await msg.delete()
    return await app.send_message(chat_id, text, reply_markup=markup, parse_mode=HTML, link_preview_options=nopreview)


async def show_doc(msg: Message, key: str, markup):
    """Help table ko usi message me edit karke dikhata hai (naya message nahi)."""
    chat_id = msg.chat.id
    nopreview = LinkPreviewOptions(is_disabled=True)
    if not msg.photo:
        try:
            return await app.edit_message_text(
                chat_id, msg.id, rich_message=InputRichMessage(html=HELP_TABLES[key]), reply_markup=markup
            )
        except Exception:
            try:
                return await app.edit_message_text(
                    chat_id, msg.id, text=HELP_TEXTS.get(key, HELP_NOT_FOUND_TEXT), reply_markup=markup,
                    parse_mode=HTML, link_preview_options=nopreview,
                )
            except Exception:
                pass
    with contextlib.suppress(Exception):
        await msg.delete()
    return await send_doc(chat_id, key, markup)


# ------------------------------------------------------------ /start
@app.on_message(filters.command("start", COMMAND_HANDLER) & filters.group)
async def group_start(_, message: Message):
    await message.reply_photo(
        START_IMAGE,
        caption=GROUP_START_TEXT,
        reply_markup=B.group_start(BOT_USERNAME, SUPPORT_GROUP),
        parse_mode=HTML,
        has_spoiler=True,
    )


@app.on_message(filters.command("start", COMMAND_HANDLER) & filters.private)
async def start_private(client, message: Message):
    user = message.from_user
    if not user:
        return
    parts = message.text.split(maxsplit=1)
    payload = parts[1].strip() if len(parts) > 1 else ""

    # deep links jo dusre plugins handle karte hain (notes / rules buttons)
    if payload.startswith(("btnnotesm_", "btnrules_")):
        return

    if not await mk_db.is_user_exist(user.id):
        await mk_db.add_user(user.id, user.first_name)
    await edith_db.add_user(user.id, user.first_name)

    # welcome setup deep link: /start wsetup_<chat_id>
    if payload.startswith("wsetup_"):
        try:
            chat_id = int(payload[len("wsetup_"):])
        except ValueError:
            return await message.reply_text("❌ ɪɴᴠᴀʟɪᴅ ꜱᴇᴛᴜᴘ ʟɪɴᴋ.")
        try:
            member = await client.get_chat_member(chat_id, user.id)
            if member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                return await message.reply_text("❌ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ɢʀᴏᴜᴘ.")
            chat = await client.get_chat(chat_id)
        except Exception as e:
            return await message.reply_text(f"❌ ᴄᴏᴜʟᴅ ɴᴏᴛ ᴠᴇʀɪꜰʏ ᴀᴅᴍɪɴ ꜱᴛᴀᴛᴜꜱ: {e}")
        from misskaty.edith.handlers.welcome import _send_panel, _sessions

        data = await edith_db.get_welcome_v2(chat_id) or {}
        _sessions[user.id] = {
            "chat_id": chat_id,
            "chat_title": chat.title or str(chat_id),
            "step": "main",
            "text": data.get("text"),
            "media_file_id": data.get("media_file_id"),
            "media_type": data.get("media_type"),
            "buttons": list(data.get("buttons") or []),
        }
        return await _send_panel(client, message.chat.id, user.id)

    # /start help  |  /start help_<key>
    if payload == "help":
        return await message.reply_text(HELP_MENU_TEXT.format(support_url=SUPPORT_GROUP), reply_markup=B.help_menu(), parse_mode=HTML, link_preview_options=LinkPreviewOptions(is_disabled=True))
    if payload.startswith("help_"):
        key = payload[5:].lower()
        if key in HELP_TEXTS:
            return await send_doc(message.chat.id, key, B.help_back(B.category_of(key), 0), reply_to=message.id)

    await message.reply_photo(
        START_IMAGE,
        caption=_start_text(user.first_name),
        reply_markup=B.start_menu(BOT_USERNAME, SUPPORT_GROUP, UPDATE_CHANNEL),
        parse_mode=HTML,
    )


# ------------------------------------------------------------ /help
@app.on_message(filters.command("help", COMMAND_HANDLER) & filters.private)
async def help_private(_, message: Message):
    if message.from_user:
        await edith_db.add_user(message.from_user.id, message.from_user.first_name)
    arg = message.text.split(maxsplit=1)[1].strip().lower().replace(" ", "_") if len(message.command) > 1 else ""
    for key in (arg, f"{arg}_help"):
        if key and key in HELP_TEXTS:
            return await send_doc(message.chat.id, key, B.help_back(B.category_of(key), 0), reply_to=message.id)
    await message.reply_text(
        HELP_MENU_TEXT.format(support_url=SUPPORT_GROUP),
        reply_markup=B.help_menu(),
        parse_mode=HTML,
        link_preview_options=LinkPreviewOptions(is_disabled=True),
    )


@app.on_message(filters.command("help", COMMAND_HANDLER) & filters.group)
async def help_group(_, message: Message):
    arg = message.text.split(maxsplit=1)[1].strip().lower().replace(" ", "_") if len(message.command) > 1 else ""
    payload = "help"
    for key in (arg, f"{arg}_help"):
        if key and key in HELP_TEXTS:
            payload = f"help_{key}"
            break
    await message.reply_photo(
        START_IMAGE,
        caption=GROUP_HELP_TEXT,
        reply_markup=B.group_help(BOT_USERNAME, payload),
        parse_mode=HTML,
        has_spoiler=True,
    )


# ------------------------------------------------------------ /privacy
@app.on_message(filters.command("privacy", COMMAND_HANDLER) & filters.private)
async def privacy_cmd(_, message: Message):
    await message.reply_photo(
        PRIVACY_IMAGE or START_IMAGE,
        caption=PRIVACY_TEXT.format(bot_link=BOT_LINK, privacy_url=PRIVACY_POLICY_URL, support_url=SUPPORT_GROUP),
        reply_markup=B.privacy(PRIVACY_POLICY_URL),
        parse_mode=HTML,
    )


# ------------------------------------------------------------ chat tracking (for /stats)
_tracked = TTLCache(maxsize=4096, ttl=600)  # har chat ko 10 min me sirf ek baar DB me likho


@app.on_message(filters.group & ~filters.service, group=10)
async def track_group(_, message: Message):
    if message.chat and message.chat.id not in _tracked:
        _tracked[message.chat.id] = True
        with contextlib.suppress(Exception):
            await edith_db.add_chat(message.chat.id, message.chat.title or "")


# ------------------------------------------------------------ callbacks
@app.on_callback_query(filters.regex(r"^(help|help_categories)$"))
async def cb_help_menu(_, cq: CallbackQuery):
    await show_text(cq.message, HELP_MENU_TEXT.format(support_url=SUPPORT_GROUP), B.help_menu())
    await cq.answer()


@app.on_callback_query(filters.regex(r"^help_cat\|(\w+)\|(\d+)$"))
async def cb_help_category(_, cq: CallbackQuery):
    category, page = cq.matches[0].group(1), int(cq.matches[0].group(2))
    title = B.HELP_CATEGORIES.get(category, (category, []))[0]
    text = HELP_CATEGORY_TEXT.format(category=title, support_url=SUPPORT_GROUP)
    await show_text(cq.message, text, B.help_category(category, page))
    await cq.answer()


@app.on_callback_query(filters.regex(r"^hm\|(\w+)\|(\w+)\|(\d+)$"))
async def cb_help_module(_, cq: CallbackQuery):
    key, category, page = cq.matches[0].group(1), cq.matches[0].group(2), int(cq.matches[0].group(3))
    await show_doc(cq.message, key, B.help_back(category, page))
    await cq.answer()


@app.on_callback_query(filters.regex(r"^help_close$"))
async def cb_help_close(_, cq: CallbackQuery):
    await cq.message.delete()
    await cq.answer()


@app.on_callback_query(filters.regex(r"^noop$"))
async def cb_noop(_, cq: CallbackQuery):
    await cq.answer()


@app.on_callback_query(filters.regex(r"^back_to_start$"))
async def cb_back_to_start(_, cq: CallbackQuery):
    await render(cq.message, _start_text(cq.from_user.first_name), B.start_menu(BOT_USERNAME, SUPPORT_GROUP, UPDATE_CHANNEL))
    await cq.answer()


@app.on_callback_query(filters.regex(r"^stats_callback$"))
async def cb_stats(_, cq: CallbackQuery):
    text = await bot_sys_stats()
    with contextlib.suppress(QueryIdInvalid):
        await app.answer_callback_query(cq.id, text, show_alert=True)
        
