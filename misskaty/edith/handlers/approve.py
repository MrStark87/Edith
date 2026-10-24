# ============================================================
# Group Manager Bot — Approve / Free Users
# Author: Mr. Stark
# ============================================================

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus, ParseMode
import logging
from misskaty.edith import db

logger = logging.getLogger(__name__)


async def is_power(client, chat_id: int, user_id: int) -> bool:
    member = await client.get_chat_member(chat_id, user_id)
    return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]


async def extract_target_user(client, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user:
        return message.reply_to_message.from_user

    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        return None

    arg = parts[1].strip()
    try:
        if arg.startswith("@"):
            return await client.get_users(arg)
        elif arg.lstrip("-").isdigit():
            return await client.get_users(int(arg))
    except Exception:
        return None
    return None


from misskaty.ui.help_texts import APPROVE_HELP_TEXT  # noqa: E402


def register_approve_handler(app: Client):

    # ==========================================================
    # /free or /approve — same action, multiple command names
    # ==========================================================

    @app.on_message(filters.group & filters.command(["free", "approve"]))
    async def approve_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text(
                "❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.", parse_mode=ParseMode.HTML
            )

        user = await extract_target_user(client, message)
        if not user:
            return await message.reply_text(
                "⚙️ ᴜꜱᴀɢᴇ: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇ <code>/free @ᴜꜱᴇʀ</code>",
                parse_mode=ParseMode.HTML
            )

        already = await db.is_approved(message.chat.id, user.id)
        if already:
            return await message.reply_text(
                f"⚠️ {user.mention} ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀᴘᴘʀᴏᴠᴇᴅ.", parse_mode=ParseMode.HTML
            )

        await db.approve_user(message.chat.id, user.id)
        await message.reply_text(
            f"🕊 {user.mention} ʜᴀꜱ ʙᴇᴇɴ ᴀᴘᴘʀᴏᴠᴇᴅ ɪɴ {message.chat.title}!\n"
            f"➻ 𝘁𝗵𝗲𝘆 𝘄𝗶𝗹𝗹 𝗻𝗼𝘄 𝗯𝗲 𝗶𝗴𝗻𝗼𝗿𝗲𝗱 𝗯𝘆 𝗮𝘂𝘁𝗼𝗺𝗮𝘁𝗲𝗱 𝗮𝗱𝗺𝗶𝗻 𝗮𝗰𝘁𝗶𝗼𝗻𝘀 𝗹𝗶𝗸𝗲. "
            f"ʟᴏᴄᴋꜱ, ʙʟᴏᴄᴋʟɪꜱᴛꜱ, ʙɪᴏʟɪɴᴋ ᴇᴛᴄ."
            f"",
            parse_mode=ParseMode.HTML
        )


    # ==========================================================
    # /unfree or /unapprove — same action, multiple command names
    # ==========================================================

    @app.on_message(filters.group & filters.command(["unfree", "unapprove"]))
    async def unapprove_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text(
                "❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.", parse_mode=ParseMode.HTML
            )

        user = await extract_target_user(client, message)
        if not user:
            return await message.reply_text(
                "⚙️ ᴜꜱᴀɢᴇ: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇ <code>/unfree @ᴜꜱᴇʀ</code>",
                parse_mode=ParseMode.HTML
            )

        removed = await db.unapprove_user(message.chat.id, user.id)
        if removed:
            await message.reply_text(
                f"🔒 {user.mention} ʜᴀꜱ ʙᴇᴇɴ ᴜɴᴀᴘᴘʀᴏᴠᴇᴅ ɪɴ {message.chat.title}.\n"
                f"➻ 𝗯𝗼𝘁 𝗿𝗲𝘀𝘁𝗿𝗶𝗰𝘁𝗶𝗼𝗻𝘀 𝘄𝗶𝗹𝗹 𝗻𝗼𝘄 𝗮𝗽𝗽𝗹𝘆 𝘁𝗼 𝘁𝗵𝗲𝗺 𝗮𝗴𝗮𝗶𝗻."
                f"",
                parse_mode=ParseMode.HTML
            )
        else:
            await message.reply_text(
                f"⚠️ {user.mention} ᴡᴀꜱ ɴᴏᴛ ᴀᴘᴘʀᴏᴠᴇᴅ.", parse_mode=ParseMode.HTML
            )


    # ==========================================================
    # /approved — list approved users
    # ==========================================================

    @app.on_message(filters.group & filters.command("approved"))
    async def approved_list_cmd(client, message: Message):
        users = await db.get_approved_users(message.chat.id)

        if not users:
            return await message.reply_text(
                "📭 ɴᴏ ᴀᴘᴘʀᴏᴠᴇᴅ ᴜꜱᴇʀꜱ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ.", parse_mode=ParseMode.HTML
            )

        lines = []
        for uid in users:
            try:
                u = await client.get_users(uid)
                lines.append(f"• {u.mention} — <code>{uid}</code>")
            except Exception:
                lines.append(f"• <code>{uid}</code>")

        await message.reply_text(
            "🕊 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 𝗨𝘀𝗲𝗿𝘀:\n\n" + "\n".join(lines),
            parse_mode=ParseMode.HTML
        )
