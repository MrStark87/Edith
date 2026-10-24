# ============================================================
# Group Manager Bot — Command Deleter
# Author: Mr. Stark
# ============================================================

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from misskaty.edith import db
import re
import logging

logger = logging.getLogger(__name__)


async def is_power(client, chat_id: int, user_id: int) -> bool:
    member = await client.get_chat_member(chat_id, user_id)
    return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]


# Command pattern — /, !, . se shuru hone wale
CMD_PATTERN = re.compile(r"^[/!.]")


# ==========================================================
# Help Text
# ==========================================================

from misskaty.ui.help_texts import CMDDELETER_HELP_TEXT  # noqa: E402


def register_cmddeleter_handler(app: Client):

    # ==========================================================
    # /cmd on/off
    # ==========================================================

    @app.on_message(filters.group & filters.command("cmd"))
    async def cmd_toggle(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text("❌ ᴏɴʟʏ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ. .")

        parts = message.text.split(maxsplit=1)
        if len(parts) < 2 or parts[1].lower() not in ["on", "off"]:
            status = await db.get_cmddeleter_status(message.chat.id)
            current = "🟢 ᴏɴ" if status else "🔴 ᴏꜰꜰ"
            return await message.reply_text(
                f"⚙️ ᴜꜱᴀɢᴇ: `/cmd ᴏɴ` ʏᴀ `/cmd ᴏꜰꜰ`\n\n📊 ᴄᴜʀʀᴇɴᴛ: {current}"
            )

        status = parts[1].lower() == "on"
        await db.set_cmddeleter_status(message.chat.id, status)

        if status:
            await message.reply_text(
                "✅ **ᴄᴏᴍᴍᴀɴᴅ ᴅᴇʟᴇᴛᴇʀ ᴏɴ!**\n\n"
                "ɴᴏᴡ /! . ᴄᴏᴍᴍᴀɴᴅꜱ ꜱᴛᴀʀᴛɪɴɢ ꜰʀᴏᴍ ᴛʜɪꜱ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ.."
            )
        else:
            await message.reply_text("⚠️ **ᴄᴏᴍᴍᴀɴᴅ ᴅᴇʟᴇᴛᴇʀ ᴏꜰꜰ!**")


    # ==========================================================
    # Enforce — commands detect karke delete karo
    # ==========================================================

    @app.on_message(filters.group & ~filters.service, group=50)
    async def enforce_cmddeleter(client, message: Message):
        if not await db.get_cmddeleter_status(message.chat.id):
            return

        text = message.text or message.caption or ""
        if text and CMD_PATTERN.match(text):
            try:
                await message.delete()
            except Exception as e:
                logger.error(f"ᴄᴍᴅ ᴅᴇʟᴇᴛᴇʀ ᴇʀʀᴏʀ: {e}")
            
