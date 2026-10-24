# ============================================================
# Group Manager Bot — Blacklisted Users
# Author: Mr. Stark
# ============================================================

from pyrogram import Client, filters, enums
from pyrogram.types import Message
import logging
from pyrogram.enums import ChatMemberStatus
from misskaty.edith import db

logger = logging.getLogger(__name__)


async def is_power(client, chat_id: int, user_id: int) -> bool:
    member = await client.get_chat_member(chat_id, user_id)
    return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]


async def extract_user_id(client, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user:
        return message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name

    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        return None, None

    arg = parts[1].strip()
    try:
        if arg.startswith("@"):
            user = await client.get_users(arg)
            return user.id, user.first_name
        elif arg.lstrip("-").isdigit():
            user = await client.get_users(int(arg))
            return user.id, user.first_name
    except Exception:
        pass
    return None, None

from misskaty.ui.help_texts import BLACKUSER_HELP_TEXT  # noqa: E402


def register_blackuser_handler(app: Client):

    # ==========================================================
    # /blackuser
    # ==========================================================

    @app.on_message(filters.group & filters.command("blackuser"))
    async def blackuser_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text(
                "❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.",
                parse_mode=enums.ParseMode.HTML
            )

        user_id, first_name = await extract_user_id(client, message)
        if not user_id:
            return await message.reply_text(
                "⚙️ ᴜꜱᴀɢᴇ: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇ <code>/blackuser &lt;ᴜꜱᴇʀɪᴅ/@ᴜꜱᴇʀɴᴀᴍᴇ&gt;</code>",
                parse_mode=enums.ParseMode.HTML
            )

        # Admins cannot be blacklisted
        try:
            target = await client.get_chat_member(message.chat.id, user_id)
            if target.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                return await message.reply_text(
                    "⚠️ ᴄᴀɴɴᴏᴛ ʙʟᴀᴄᴋʟɪꜱᴛ ᴀɴ ᴀᴅᴍɪɴ.",
                    parse_mode=enums.ParseMode.HTML
                )
        except Exception:
            pass

        existing = await db.get_blacklisted_users(message.chat.id)
        if user_id in existing:
            return await message.reply_text(
                f"⚠️ ᴜꜱᴇʀ <code>{user_id}</code> ɪꜱ ᴀʟʀᴇᴀᴅʏ ʙʟᴀᴄᴋʟɪꜱᴛᴇᴅ.",
                parse_mode=enums.ParseMode.HTML
            )

        await db.add_blacklisted_user(message.chat.id, user_id)
        await message.reply_text(
            f"🚷 {first_name} (<code>{user_id}</code>) ʜᴀꜱ ʙᴇᴇɴ ʙʟᴀᴄᴋʟɪꜱᴛᴇᴅ.\n\n"
            f"ᴀʟʟ ᴛʜᴇɪʀ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ.",
            parse_mode=enums.ParseMode.HTML
        )


    # ==========================================================
    # /rmblackuser
    # ==========================================================

    @app.on_message(filters.group & filters.command("rmblackuser"))
    async def rmblackuser_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text(
                "❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.",
                parse_mode=enums.ParseMode.HTML
            )

        user_id, first_name = await extract_user_id(client, message)
        if not user_id:
            return await message.reply_text(
                "⚙️ ᴜꜱᴀɢᴇ: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇ <code>/rmblackuser &lt;ᴜꜱᴇʀɪᴅ/@ᴜꜱᴇʀɴᴀᴍᴇ&gt;</code>",
                parse_mode=enums.ParseMode.HTML
            )

        removed = await db.remove_blacklisted_user(message.chat.id, user_id)
        if removed:
            await message.reply_text(
                f"✅ {first_name} (<code>{user_id}</code>) ʀᴇᴍᴏᴠᴇᴅ ꜰʀᴏᴍ ʙʟᴀᴄᴋʟɪꜱᴛ.",
                parse_mode=enums.ParseMode.HTML
            )
        else:
            await message.reply_text(
                f"⚠️ ᴜꜱᴇʀ <code>{user_id}</code> ᴡᴀꜱ ɴᴏᴛ ɪɴ ᴛʜᴇ ʙʟᴀᴄᴋʟɪꜱᴛ.",
                parse_mode=enums.ParseMode.HTML
            )


    # ==========================================================
    # /blacklistusers
    # ==========================================================

    @app.on_message(filters.group & filters.command("blacklistusers"))
    async def blacklistusers_cmd(client, message: Message):
        users = await db.get_blacklisted_users(message.chat.id)

        if not users:
            return await message.reply_text(
                "📭 ɴᴏ ʙʟᴀᴄᴋʟɪꜱᴛᴇᴅ ᴜꜱᴇʀꜱ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ.",
                parse_mode=enums.ParseMode.HTML
            )

        lines = []
        for uid in users:
            try:
                user = await client.get_users(uid)
                lines.append(f"• <a href='tg://user?id={uid}'>{user.first_name}</a> — <code>{uid}</code>")
            except Exception:
                lines.append(f"• <code>{uid}</code>")

        await message.reply_text(
            f"🚷 𝗕𝗹𝗮𝗰𝗸𝗹𝗶𝘀𝘁𝗲𝗱 𝗨𝘀𝗲𝗿𝘀:\n\n" + "\n".join(lines),
            parse_mode=enums.ParseMode.HTML
        )


    # ==========================================================
    # Enforce — delete all messages from blacklisted users
    # ==========================================================

    @app.on_message(filters.group & ~filters.service, group=13)
    async def enforce_blackuser(client, message: Message):
        if not message.from_user:
            return

        blacklisted = await db.get_blacklisted_users(message.chat.id)

        if message.from_user.id in blacklisted:
            try:
                await message.delete()
            except Exception as e:
                logger.error(f"ʙʟᴀᴄᴋᴜꜱᴇʀ ᴅᴇʟᴇᴛᴇ ᴇʀʀᴏʀ: {e}")
