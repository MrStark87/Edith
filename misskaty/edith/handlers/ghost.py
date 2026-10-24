# ============================================================
# Group Manager Bot — Ghost Mode & Privacy
# Author: Mr. Stark
# ============================================================

from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from misskaty.edith import db
import logging

logger = logging.getLogger(__name__)


async def is_power(client, chat_id: int, user_id: int) -> bool:
    member = await client.get_chat_member(chat_id, user_id)
    return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]


from misskaty.ui.help_texts import GHOST_HELP_TEXT  # noqa: E402


def register_ghost_handler(app: Client):

    # ==========================================================
    # /ghostmode on/off
    # ==========================================================

    @app.on_message(filters.group & filters.command("ghostmode"))
    async def ghostmode_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text(
                "❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.",
                parse_mode=enums.ParseMode.HTML
            )

        parts = message.text.split(maxsplit=1)
        if len(parts) < 2 or parts[1].lower() not in ["on", "off"]:
            status = await db.get_ghost_status(message.chat.id)
            current = "🟢 ᴏɴ" if status else "🔴 ᴏꜰꜰ"
            return await message.reply_text(
                f"⚙️ ᴜꜱᴀɢᴇ: <code>/ghostmode ᴏɴ</code> ᴏʀ <code>/ghostmode ᴏꜰꜰ</code>\n\n"
                f"📊 ᴄᴜʀʀᴇɴᴛ: {current}",
                parse_mode=enums.ParseMode.HTML
            )

        status = parts[1].lower() == "on"
        await db.set_ghost_status(message.chat.id, status)

        if status:
            await message.reply_text(
                "👻 𝗚𝗵𝗼𝘀𝘁 𝗠𝗼𝗱𝗲 𝗢𝗡!\n\n"
                "ᴀʟʟ ꜱᴇʀᴠɪᴄᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ.",
                parse_mode=enums.ParseMode.HTML
            )
        else:
            await message.reply_text(
                "⚠️ 𝗚𝗵𝗼𝘀𝘁 𝗠𝗼𝗱𝗲 𝗢𝗙𝗙!",
                parse_mode=enums.ParseMode.HTML
            )


    # ==========================================================
    # Enforce — delete service messages
    # ==========================================================

    @app.on_message(filters.group & filters.service, group=12)
    async def enforce_ghost(client, message: Message):
        if not await db.get_ghost_status(message.chat.id):
            return
        try:
            await message.delete()
        except Exception as e:
            logger.error(f"ɢʜᴏꜱᴛ ᴍᴏᴅᴇ ᴅᴇʟᴇᴛᴇ ᴇʀʀᴏʀ: {e}")


    # ==========================================================
    # /privacy
    # ==========================================================

