# ============================================================
# Group Manager Bot — Zombie Remover
# Author: Mr. Stark
# ============================================================

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
import logging

logger = logging.getLogger(__name__)


async def is_power(client, chat_id: int, user_id: int) -> bool:
    member = await client.get_chat_member(chat_id, user_id)
    return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]


# ==========================================================
# Help Text
# ==========================================================

from misskaty.ui.help_texts import ZOMBIE_HELP_TEXT  # noqa: E402


def register_zombie_handler(app: Client):

    # ==========================================================
    # /zombie — Scan and remove deleted accounts
    # ==========================================================

    @app.on_message(filters.group & filters.command("zombie"))
    async def zombie_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text("❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")

        scanning = await message.reply_text("🔍 ꜱᴄᴀɴɴɪɴɢ ꜰᴏʀ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛꜱ...")

        removed = 0
        failed = 0

        async for member in client.get_chat_members(message.chat.id):
            if member.user.is_deleted:
                try:
                    await client.ban_chat_member(message.chat.id, member.user.id)
                    await client.unban_chat_member(message.chat.id, member.user.id)
                    removed += 1
                except Exception as e:
                    logger.error(f"ᴢᴏᴍʙɪᴇ ʀᴇᴍᴏᴠᴇ ᴇʀʀᴏʀ: {e}")
                    failed += 1

        if removed == 0:
            await scanning.edit_text("✅ ɴᴏ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ.")
        else:
            await scanning.edit_text(
                f"✅ **ᴢᴏᴍʙɪᴇ ꜱᴄᴀɴ ᴄᴏᴍᴘʟᴇᴛᴇ!**\n\n"
                f"🗑️ ʀᴇᴍᴏᴠᴇᴅ: `{removed}` ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛꜱ\n"
                f"❌ ꜰᴀɪʟᴇᴅ: `{failed}`"
            )
