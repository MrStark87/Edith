# ============================================================
# Group Manager Bot — Utility (Updated)
# Author: Mr. Stark
# ============================================================
import urllib.parse
from pyrogram import Client, filters, enums
from pyrogram.types import (
    Message, InlineKeyboardMarkup, InlineKeyboardButton
)
from pyrogram.enums import ChatMemberStatus, ChatType, ChatMembersFilter
import logging
import asyncio
import time

logger = logging.getLogger(__name__)

# Service messages clear karne ki setting store karne ke liye
# Production me isko database (like MongoDB/SQL) me store karna behtar hota hai
CLEAN_SERVICE_SETTINGS = {}

async def is_power(client, chat_id: int, user_id: int) -> bool:
    member = await client.get_chat_member(chat_id, user_id)
    return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]


from misskaty.ui.help_texts import UTILITY_HELP_TEXT  # noqa: E402


def register_utility_handler(app: Client):

    # ----------------------------------------------------------
    # /chatinfo
    # ----------------------------------------------------------
    @app.on_message(filters.group & filters.command("chatinfo"))
    async def chatinfo_cmd(client, message: Message):
        chat = message.chat
        try:
            count = await client.get_chat_members_count(chat.id)
        except Exception:
            count = "N/A"

        username  = f"@{chat.username}" if chat.username else "ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ"
        chat_type = str(chat.type).replace("ChatType.", "").capitalize()

        await message.reply_text(
            f"<u>𝗰𝗵𝗮𝘁 𝗶𝗻𝗳𝗼<u>\n\n"
            f"𝗻𝗮𝗺𝗲 : {chat.title}\n"
            f"𝗰𝗵𝗮𝘁 𝗶𝗱 : <code>{chat.id}</code>\n"
            f"𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : {username}\n"
            f"𝗺𝗲𝗺𝗯𝗲𝗿 𝗰𝗼𝘂𝗻𝘁 : {count}\n"
            f"𝗰𝗵𝗮𝘁 𝘁𝘆𝗽𝗲 : {chat_type}"
            "",
            parse_mode=enums.ParseMode.HTML
        )

    # ----------------------------------------------------------
    # /id
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # /info [NEW]
    # ----------------------------------------------------------

    # ----------------------------------------------------------
    # /ping [NEW]
    # ----------------------------------------------------------

    # ----------------------------------------------------------
    # /pin [silent]
    # ----------------------------------------------------------
    @app.on_message(filters.group & filters.command("pin"))
    async def pin_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text("❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴘɪɴ ᴍᴇꜱꜱᴀɢᴇꜱ.", parse_mode=enums.ParseMode.HTML)

        if not message.reply_to_message:
            return await message.reply_text("⚠️ ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴘɪɴ.", parse_mode=enums.ParseMode.HTML)

        args = message.text.split(maxsplit=1)
        silent = len(args) > 1 and args[1].strip().lower() == "silent"

        try:
            await client.pin_chat_message(
                message.chat.id,
                message.reply_to_message.id,
                disable_notification=silent
            )
            label = "ꜱɪʟᴇɴᴛʟʏ " if silent else ""
            await message.reply_text(f"📌 ᴍᴇꜱꜱᴀɢᴇ {label}ᴘɪɴɴᴇᴅ!", parse_mode=enums.ParseMode.HTML)
        except Exception as e:
            await message.reply_text(f"❌ ᴄᴏᴜʟᴅ ɴᴏᴛ ᴘɪɴ: {e}", parse_mode=enums.ParseMode.HTML)

    # ----------------------------------------------------------
    # /unpin
    # ----------------------------------------------------------
    @app.on_message(filters.group & filters.command("unpin"))
    async def unpin_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text("❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴜɴᴘɪɴ ᴍᴇꜱꜱᴀɢᴇꜱ.", parse_mode=enums.ParseMode.HTML)

        try:
            if message.reply_to_message:
                await client.unpin_chat_message(
                    message.chat.id, message.reply_to_message.id
                )
                await message.reply_text("📌 ᴍᴇꜱꜱᴀɢᴇ ᴜɴᴘɪɴɴᴇᴅ.", parse_mode=enums.ParseMode.HTML)
            else:
                await client.unpin_all_chat_messages(message.chat.id)
                await message.reply_text("📌 ᴀʟʟ ᴘɪɴɴᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ ᴜɴᴘɪɴɴᴇᴅ.", parse_mode=enums.ParseMode.HTML)
        except Exception as e:
            await message.reply_text(f"❌ ᴄᴏᴜʟᴅ ɴᴏᴛ ᴜɴᴘɪɴ: {e}", parse_mode=enums.ParseMode.HTML)

    # ----------------------------------------------------------
    # /purge
    # ----------------------------------------------------------
    @app.on_message(filters.group & filters.command("purge"))
    async def purge_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text("❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴘᴜʀɢᴇ ᴍᴇꜱꜱᴀɢᴇꜱ.", parse_mode=enums.ParseMode.HTML)

        if not message.reply_to_message:
            return await message.reply_text("⚠️ ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ꜱᴛᴀʀᴛ ᴘᴜʀɢɪɴɢ ꜰʀᴏᴍ.", parse_mode=enums.ParseMode.HTML)

        from_id = message.reply_to_message.id
        to_id   = message.id
        ids     = list(range(from_id, to_id + 1))

        deleted = 0
        for i in range(0, len(ids), 100):
            try:
                await client.delete_messages(message.chat.id, ids[i:i + 100])
                deleted += len(ids[i:i + 100])
            except Exception as e:
                logger.error(f"ᴘᴜʀɢᴇ ʙᴀᴛᴄʜ ᴇʀʀᴏʀ: {e}")

        confirm = await client.send_message(
            message.chat.id,
            f"🗑 {deleted} ᴍᴇꜱꜱᴀɢᴇꜱ ᴅᴇʟᴇᴛᴇᴅ.",
            parse_mode=enums.ParseMode.HTML
        )
        await asyncio.sleep(3)
        try:
            await confirm.delete()
        except Exception:
            pass

    # ----------------------------------------------------------
    # /purgeme [NEW]
    # ----------------------------------------------------------
    @app.on_message(filters.group & filters.command("purgeme"))
    async def purgeme_cmd(client, message: Message):
        user_id = message.from_user.id
        chat_id = message.chat.id
        
        # User ke messages dhoodhne ke liye history search karenge (Max last 100 messages)
        msg_ids_to_delete = []
        async for msg in client.get_chat_history(chat_id, limit=100):
            if msg.from_user and msg.from_user.id == user_id:
                msg_ids_to_delete.append(msg.id)
                
        if not msg_ids_to_delete:
            return await message.reply_text("⚠️ ᴀᴀᴘᴋᴀ ᴋᴏɪ ᴘᴜʀᴀɴᴀ ᴍᴇꜱꜱᴀɢᴇ ɴᴀʜɪ ᴍɪʟᴀ.", parse_mode=enums.ParseMode.HTML)
            
        try:
            await client.delete_messages(chat_id, msg_ids_to_delete)
            confirm = await client.send_message(
                chat_id,
                f"🗑 ᴅᴇʟᴇᴛᴇᴅ {len(msg_ids_to_delete)} ᴏꜰ ʏᴏᴜʀ ʀᴇᴄᴇɴᴛ ᴍᴇꜱꜱᴀɢᴇꜱ.",
                parse_mode=enums.ParseMode.HTML
            )
            await asyncio.sleep(3)
            await confirm.delete()
        except Exception as e:
            logger.error(f"ᴘᴜʀɢᴇᴍᴇ ᴇʀʀᴏʀ: {e}")

    # ----------------------------------------------------------
    # /del
    # ----------------------------------------------------------
    @app.on_message(filters.group & filters.command("del"))
    async def del_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text("❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ.", parse_mode=enums.ParseMode.HTML)

        if not message.reply_to_message:
            return await message.reply_text("⚠️ ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ.", parse_mode=enums.ParseMode.HTML)

        try:
            await message.reply_to_message.delete()
            await message.delete()
        except Exception as e:
            await message.reply_text(f"❌ ᴄᴏᴜʟᴅ ɴᴏᴛ ᴅᴇʟᴇᴛᴇ: {e}", parse_mode=enums.ParseMode.HTML)

    # ----------------------------------------------------------
    # /cleanservice [NEW]
    # ----------------------------------------------------------
    @app.on_message(filters.group & filters.command("cleanservice"))
    async def cleanservice_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text("❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴄʜᴀɴɢᴇ ꜱᴇᴛᴛɪɴɢꜱ.", parse_mode=enums.ParseMode.HTML)

        parts = message.text.split(maxsplit=1)
        if len(parts) < 2:
            current = "ON" if CLEAN_SERVICE_SETTINGS.get(message.chat.id, False) else "OFF"
            return await message.reply_text(
                f"➻ 𝗖𝗹𝗲𝗮𝗻 𝗦𝗲𝗿𝘃𝗶𝗰𝗲 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀\n\n"
                f"ᴄᴜʀʀᴇɴᴛ ꜱᴛᴀᴛᴜꜱ: {current}\n"
                f"ᴜꜱᴀɢᴇ: <code>/cleanservice ᴏɴ</code> ᴏʀ <code>/cleanservice ᴏꜰꜰ</code>"
                f"",
                parse_mode=enums.ParseMode.HTML
            )

        action = parts[1].strip().lower()
        if action == "on":
            CLEAN_SERVICE_SETTINGS[message.chat.id] = True
            await message.reply_text("✅ 𝗖𝗹𝗲𝗮𝗻 𝗦𝗲𝗿𝘃𝗶𝗰𝗲 𝘁𝘂𝗿𝗻𝗲𝗱 𝗢𝗡. ᴊᴏɪɴ/Leave ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇᴅ.", parse_mode=enums.ParseMode.HTML)
        elif action == "off":
            CLEAN_SERVICE_SETTINGS[message.chat.id] = False
            await message.reply_text("❌ 𝗖𝗹𝗲𝗮𝗻 𝗦𝗲𝗿𝘃𝗶𝗰𝗲 𝘁𝘂𝗿𝗻𝗲𝗱 𝗢𝗙𝗙. ᴊᴏɪɴ/Leave ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪʟʟ ɴᴏᴛ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ.", parse_mode=enums.ParseMode.HTML)
        else:
            await message.reply_text("⚠️ ɪɴᴠᴀʟɪᴅ ᴏᴘᴛɪᴏɴ. ᴜꜱᴇ <code>ᴏɴ</code> ᴏʀ <code>ᴏꜰꜰ</code>.", parse_mode=enums.ParseMode.HTML)

    # ----------------------------------------------------------
    # Clean Service Handler Logic [NEW]
    # ----------------------------------------------------------
    @app.on_message(filters.group & (filters.new_chat_members | filters.left_chat_member))
    async def service_msg_cleaner(client, message: Message):
        # Agar is group ke liye Clean Service toggled 'ON' hai to message delete ho jayega
        if CLEAN_SERVICE_SETTINGS.get(message.chat.id, False):
            try:
                await message.delete()
            except Exception as e:
                logger.error(f"ꜰᴀɪʟᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ꜱᴇʀᴠɪᴄᴇ ᴍᴇꜱꜱᴀɢᴇ: {e}")

    # ----------------------------------------------------------
    # /calc — calculator for everyone
    # ----------------------------------------------------------

    # ----------------------------------------------------------
    # /carbon <text> [NEW]
    # ----------------------------------------------------------
