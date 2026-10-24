# ============================================================
# Group Manager Bot — Tools
# Author: Mr. Stark
# ============================================================

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from misskaty.edith import db
import re
import aiohttp
import logging

logger = logging.getLogger(__name__)


async def is_power(client, chat_id: int, user_id: int) -> bool:
    member = await client.get_chat_member(chat_id, user_id)
    return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]


# ==========================================================
# Patterns
# ==========================================================

PHONE_PATTERN = re.compile(
    r"(\+?\d[\d\s\-]{7,14}\d)",
    re.IGNORECASE
)

HASHTAG_PATTERN = re.compile(r"#\w+")


# ==========================================================
# Telegraph upload helper
# ==========================================================

async def upload_to_telegraph(title: str, content: str) -> str | None:
    """ᴛᴇxᴛ ᴋᴏ ᴛᴇʟᴇɢʀᴀᴘʜ ᴘᴀʀ ᴜᴘʟᴏᴀᴅ ᴋᴀʀᴏ ᴀᴜʀ ʟɪɴᴋ ʀᴇᴛᴜʀɴ ᴋᴀʀᴏ"""
    try:
        async with aiohttp.ClientSession() as session:
            # Account create
            async with session.post("https://api.telegra.ph/createAccount", json={
                "short_name": "NomadeBot",
                "author_name": "ɴᴏᴍᴀᴅᴇ ʜᴇʟᴘ ʙᴏᴛ"
            }) as resp:
                data = await resp.json()
                token = data["result"]["access_token"]

            # Page create
            async with session.post("https://api.telegra.ph/createPage", json={
                "access_token": token,
                "title": title or "Message",
                "content": [{"tag": "p", "children": [content]}],
                "return_content": False
            }) as resp:
                data = await resp.json()
                return data["result"]["url"]
    except Exception as e:
        logger.error(f"ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅ ᴇʀʀᴏʀ: {e}")
        return None


# ==========================================================
# Help Texts
# ==========================================================
from misskaty.ui.help_texts import LONGMSG_HELP_TEXT  # noqa: E402


from misskaty.ui.help_texts import PHONE_HELP_TEXT  # noqa: E402

from misskaty.ui.help_texts import HASHTAG_HELP_TEXT  # noqa: E402


def register_tools_handler(app: Client):

    # ==========================================================
    # /echo
    # ==========================================================

    @app.on_message(filters.group & filters.command("echo"))
    async def echo_cmd(client, message: Message):
        parts = message.text.split(maxsplit=1)
        if len(parts) < 2:
            return await message.reply_text("⚙️ ᴜꜱᴀɢᴇ: `/echo <text>`")

        text = parts[1]
        limit = await db.get_longlimit(message.chat.id)

        if len(text) <= limit:
            await message.reply_text(text)
        else:
            link = await upload_to_telegraph("Echo", text)
            if link:
                await message.reply_text(f"📄 ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ ᴡᴀꜱ ᴠᴇʀʏ ʟᴏɴɢ – ᴜᴘʟᴏᴀᴅᴇᴅ ᴛᴏ ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴘʜ:\n{link}")
            else:
                await message.reply_text("❌ ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅ ꜰᴀɪʟᴇᴅ. ᴛʀʏ ʟᴀᴛᴇʀ.")


    # ==========================================================
    # /setlongmode
    # ==========================================================

    @app.on_message(filters.group & filters.command("setlongmode"))
    async def setlongmode_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text("❌ ᴏɴʟʏ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")

        parts = message.text.split(maxsplit=1)
        if len(parts) < 2 or parts[1].lower() not in ["off", "manual", "automatic"]:
            mode = await db.get_longmode(message.chat.id)
            return await message.reply_text(
                f"⚙️ ᴜꜱᴀɢᴇ: `/setlongmode ᴏꜰꜰ|ᴍᴀɴᴜᴀʟ|ᴀᴜᴛᴏᴍᴀᴛɪᴄ`\n\n📊 ᴄᴜʀʀᴇɴᴛ: `{mode}`"
            )

        mode = parts[1].lower()
        await db.set_longmode(message.chat.id, mode)

        info = {
            "off": "⚠️ ᴛʜᴇʀᴇ ᴡɪʟʟ ʙᴇ ɴᴏ ᴀᴄᴛɪᴏɴ ᴏɴ ʟᴏɴɢ ᴍᴇꜱꜱᴀɢᴇꜱ.",
            "manual": "🗑️ ʟᴏɴɢ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ + ᴜꜱᴇʀ ᴡɪʟʟ ʙᴇ ᴡᴀʀɴᴇᴅ.",
            "automatic": "📄 ʟᴏɴɢ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ + ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴡɪʟʟ ʙᴇ ꜱᴇɴᴛ.",
        }
        await message.reply_text(f"✅ ʟᴏɴɢ ᴍᴇꜱꜱᴀɢᴇ ᴍᴏᴅᴇ: `{mode}`\n\n{info[mode]}")


    # ==========================================================
    # /setlonglimit
    # ==========================================================

    @app.on_message(filters.group & filters.command("setlonglimit"))
    async def setlonglimit_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text("❌ ᴏɴʟʏ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")

        parts = message.text.split(maxsplit=1)
        if len(parts) < 2 or not parts[1].strip().isdigit():
            limit = await db.get_longlimit(message.chat.id)
            return await message.reply_text(
                f"⚙️ ᴜꜱᴀɢᴇ: `/setlonglimit <200–4000>`\n\n📊 ᴄᴜʀʀᴇɴᴛ ʟɪᴍɪᴛ: `{limit}` ᴄʜᴀʀᴀᴄᴛᴇʀꜱ"
            )

        num = int(parts[1].strip())
        if not (50 <= num <= 4000):
            return await message.reply_text("⚠️ ᴛʜᴇ ʟɪᴍɪᴛ ꜱʜᴏᴜʟᴅ ʙᴇ ʙᴇᴛᴡᴇᴇɴ 50 ᴛᴏ 2000")

        await db.set_longlimit(message.chat.id, num)
        await message.reply_text(f"✅ ʟᴏɴɢ ᴍᴇꜱꜱᴀɢᴇ ʟɪᴍɪᴛ ꜱᴇᴛ: `{num}` ᴄʜᴀʀᴀᴄᴛᴇʀꜱ")


    # ==========================================================
    # Enforce long message — group messages check karo
    # ==========================================================

    @app.on_message(filters.group & filters.text & ~filters.service, group=4)
    async def enforce_longmsg(client, message: Message):
        try:
            member = await client.get_chat_member(message.chat.id, message.from_user.id)
            if member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                return
        except:
            return

        mode = await db.get_longmode(message.chat.id)
        if mode == "off":
            return

        limit = await db.get_longlimit(message.chat.id)
        if not message.text or len(message.text) <= limit:
            return

        await message.delete()

        if mode == "manual":
            await client.send_message(
                message.chat.id,
                f"⚠️ {message.from_user.mention}, ʏᴏᴜʀ ᴍᴇꜱꜱᴀɢᴇ ᴡᴀꜱ ᴠᴇʀʏ ʟᴏɴɢ ({len(message.text)} ᴄʜᴀʀꜱ).\n"
                f"ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇꜱ ꜱᴍᴀʟʟᴇʀ ᴛʜᴀɴ {limit} ᴄʜᴀʀᴀᴄᴛᴇʀꜱ."
            )
        elif mode == "automatic":
            link = await upload_to_telegraph(
                f"ᴍᴇꜱꜱᴀɢᴇ ʙʏ {message.from_user.first_name}",
                message.text
            )
            if link:
                await client.send_message(
                    message.chat.id,
                    f"📄 {message.from_user.mention}'ꜱ ʟᴇɴɢᴛʜ ᴍᴇꜱꜱᴀɢᴇ ɢᴏᴛ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ:\n{link}"
                )


    # ==========================================================
    # /nophone
    # ==========================================================

    @app.on_message(filters.group & filters.command("nophone"))
    async def nophone_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text("❌ ᴏɴʟʏ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")

        parts = message.text.split(maxsplit=1)
        if len(parts) < 2 or parts[1].lower() not in ["on", "off"]:
            status = await db.get_nophone_status(message.chat.id)
            current = "🟢 ᴏɴ" if status else "🔴 ᴏꜰꜰ"
            return await message.reply_text(
                f"⚙️ ᴜꜱᴀɢᴇ: `/nophone ᴏɴ` ʏᴀ `/nophone ᴏꜰꜰ`\n\n📊 ᴄᴜʀʀᴇɴᴛ: {current}"
            )

        status = parts[1].lower() == "on"
        await db.set_nophone_status(message.chat.id, status)
        await message.reply_text(
            "✅ **ᴘʜᴏɴᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴏɴ!**\n\nᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ʟɪᴋᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ. 📵"
            if status else
            "⚠️ **ᴘʜᴏɴᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴏꜰꜰ!**"
        )


    # ==========================================================
    # Enforce phone
    # ==========================================================

    @app.on_message(filters.group & filters.text & ~filters.service, group=5)
    async def enforce_nophone(client, message: Message):
        try:
            member = await client.get_chat_member(message.chat.id, message.from_user.id)
            if member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                return
        except:
            return

        if not await db.get_nophone_status(message.chat.id):
            return

        if message.text and PHONE_PATTERN.search(message.text):
            await message.delete()


    # ==========================================================
    # /nohashtags
    # ==========================================================

    @app.on_message(filters.group & filters.command("nohashtags"))
    async def nohashtags_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text("❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴜꜱᴇ ᴛʜᴏꜱ ᴄᴏᴍᴍᴀɴᴅ ʙᴇʙᴇ.")

        parts = message.text.split(maxsplit=1)
        if len(parts) < 2 or parts[1].lower() not in ["on", "off"]:
            status = await db.get_nohashtag_status(message.chat.id)
            current = "🟢 ᴏɴ" if status else "🔴 ᴏꜰꜰ"
            return await message.reply_text(
                f"⚙️ ᴜꜱᴀɢᴇ: `/nohashtags ᴏɴ` ʏᴀ `/nohashtags ᴏꜰꜰ`\n\n📊 ᴄᴜʀʀᴇɴᴛ: {current}"
            )

        status = parts[1].lower() == "on"
        await db.set_nohashtag_status(message.chat.id, status)
        await message.reply_text(
            "✅ **ʜᴀꜱʜᴛᴀɢ ꜰɪʟᴛᴇʀ ᴏɴ!**\n\nɴᴏᴡ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪᴛʜ ʜᴀꜱʜᴛᴀɢꜱ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ. 🚫#"
            if status else
            "⚠️ **ʜᴀꜱʜᴛᴀɢ ꜰɪʟᴛᴇʀ ᴏꜰꜰ!**"
        )


    # ==========================================================
    # Enforce hashtag
    # ==========================================================

    @app.on_message(filters.group & filters.text & ~filters.service, group=6)
    async def enforce_nohashtag(client, message: Message):
        try:
            member = await client.get_chat_member(message.chat.id, message.from_user.id)
            if member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                return
        except:
            return

        if not await db.get_nohashtag_status(message.chat.id):
            return

        if message.text and HASHTAG_PATTERN.search(message.text):
            await message.delete()
