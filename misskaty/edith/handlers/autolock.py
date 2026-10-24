# ============================================================
# Group Manager Bot — Auto Lock (Scheduled Daily Lock/Unlock)
# Author: Mr. Stark
# ============================================================

from pyrogram import Client, filters, enums
from pyrogram.enums import ButtonStyle
from pyrogram.types import Message, ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from datetime import datetime
import asyncio
import logging
from misskaty.edith import db
from misskaty.ui import buttons as UIB

logger = logging.getLogger(__name__)

ALL_LOCK_TYPES = ["url", "username", "forward", "edit", "text", "media", "sticker", "files", "music"]

FULL_LOCKED = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_other_messages=False,
    can_send_polls=False,
    can_add_web_page_previews=False,
)

FULL_OPEN = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_other_messages=True,
    can_send_polls=True,
    can_add_web_page_previews=True,
)


async def is_power(client, chat_id: int, user_id: int) -> bool:
    member = await client.get_chat_member(chat_id, user_id)
    return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]


def hour12_label(hour24: int) -> str:
    """24ʜ -> '10:00 ᴘᴍ' ꜱᴛʏʟᴇ ʟᴀʙᴇʟ"""
    ampm = "AM" if hour24 < 12 else "PM"
    h12 = hour24 % 12
    if h12 == 0:
        h12 = 12
    return f"{h12}:00 {ampm}"


def build_hour_keyboard(action: str) -> InlineKeyboardMarkup:
    rows = []
    nums = list(range(1, 13))
    for i in range(0, 12, 4):
        row = [
            UIB.edith_autolock__build_hour_keyboard_1(action=action, n=n)
            for n in nums[i:i + 4]
        ]
        rows.append(row)
    return InlineKeyboardMarkup(rows)


def build_ampm_keyboard(action: str, hour: int) -> InlineKeyboardMarkup:
    return UIB.edith_autolock__build_ampm_keyboard_1(action=action, hour=hour)


from misskaty.ui.help_texts import AUTOLOCK_HELP_TEXT  # noqa: E402


def register_autolock_handler(app: Client):

    # ==========================================================
    # /autolock on/off — start the hour picker
    # ==========================================================

    @app.on_message(filters.group & filters.command("autolock"))
    async def autolock_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text(
                "❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.", parse_mode=enums.ParseMode.HTML
            )

        parts = message.text.split(maxsplit=1)
        if len(parts) < 2 or parts[1].lower() not in ["on", "off"]:
            return await message.reply_text(
                "⚙️ ᴜꜱᴀɢᴇ: <code>/autolock ᴏɴ</code> ᴏʀ <code>/autolock ᴏꜰꜰ</code>\n\n"
                "<code>ᴏɴ</code> → ꜱᴇᴛꜱ ᴛʜᴇ ᴅᴀɪʟʏ ʟᴏᴄᴋ ᴛɪᴍᴇ.\n"
                "<code>ᴏꜰꜰ</code> → ꜱᴇᴛꜱ ᴛʜᴇ ᴅᴀɪʟʏ ᴜɴʟᴏᴄᴋ ᴛɪᴍᴇ."
                "",
                parse_mode=enums.ParseMode.HTML
            )

        action = parts[1].lower()
        label = "🔒 ʟᴏᴄᴋ" if action == "on" else "🔓 ᴜɴʟᴏᴄᴋ"

        await message.reply_text(
            f"⏰ 𝗦𝗲𝘁 𝗱𝗮𝗶𝗹𝘆 {label} ᴛɪᴍᴇ\n\nᴄʜᴏᴏꜱᴇ ᴛʜᴇ ʜᴏᴜʀ:",
            reply_markup=build_hour_keyboard(action),
            parse_mode=enums.ParseMode.HTML
        )


    # ==========================================================
    # Hour selected -> ask AM/PM
    # ==========================================================

    @app.on_callback_query(filters.regex(r"^al_h_(on|off)_(\d+)$"))
    async def autolock_hour_callback(client, callback_query):
        action = callback_query.matches[0].group(1)
        hour = int(callback_query.matches[0].group(2))
        chat_id = callback_query.message.chat.id

        if not await is_power(client, chat_id, callback_query.from_user.id):
            return await callback_query.answer("❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴄᴏɴꜰɪɢᴜʀᴇ ᴛʜɪꜱ.", show_alert=True)

        label = "🔒 ʟᴏᴄᴋ" if action == "on" else "🔓 ᴜɴʟᴏᴄᴋ"
        await callback_query.message.edit_text(
            f"⏰ 𝘀𝗲𝘁 𝗱𝗮𝗶𝗹𝘆 {label} ᴛɪᴍᴇ\n\n"
            f"ʜᴏᴜʀ: {hour}\n→ ɴᴏᴡ ᴄʜᴏᴏꜱᴇ ᴀᴍ ᴏʀ ᴘᴍ:",
            reply_markup=build_ampm_keyboard(action, hour),
            parse_mode=enums.ParseMode.HTML
        )
        await callback_query.answer()


    # ==========================================================
    # AM/PM selected -> save schedule
    # ==========================================================

    @app.on_callback_query(filters.regex(r"^al_ap_(on|off)_(\d+)_(AM|PM)$"))
    async def autolock_ampm_callback(client, callback_query):
        action = callback_query.matches[0].group(1)
        hour12 = int(callback_query.matches[0].group(2))
        ampm = callback_query.matches[0].group(3)
        chat_id = callback_query.message.chat.id

        if not await is_power(client, chat_id, callback_query.from_user.id):
            return await callback_query.answer("❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴄᴏɴꜰɪɢᴜʀᴇ ᴛʜɪꜱ.", show_alert=True)

        if ampm == "AM":
            hour24 = 0 if hour12 == 12 else hour12
        else:
            hour24 = 12 if hour12 == 12 else hour12 + 12

        if action == "on":
            await db.set_autolock_hour(chat_id, hour24)
            await callback_query.message.edit_text(
                f"✅ 𝗱𝗮𝗶𝗹𝘆 𝗮𝘂𝘁𝗼-𝗹𝗼𝗰𝗸 𝘀𝗲𝘁!\n\n"
                f"→ ɢʀᴏᴜᴘ ᴡɪʟʟ ʙᴇ ꜰᴜʟʟʏ ʟᴏᴄᴋᴇᴅ ᴇᴠᴇʀʏ ᴅᴀʏ ᴀᴛ\n"
                f"{hour12_label(hour24)}.",
                parse_mode=enums.ParseMode.HTML
            )
        else:
            await db.set_autounlock_hour(chat_id, hour24)
            await callback_query.message.edit_text(
                f"✅ 𝗱𝗮𝗶𝗹𝘆 𝗮𝘂𝘁𝗼-𝘂𝗻𝗹𝗼𝗰𝗸 𝘀𝗲𝘁!\n\n"
                f"→ ɢʀᴏᴜᴘ ᴡɪʟʟ ʙᴇ ꜰᴜʟʟʏ ᴜɴʟᴏᴄᴋᴇᴅ ᴇᴠᴇʀʏ ᴅᴀʏ ᴀᴛ\n"
                f"{hour12_label(hour24)}.",
                parse_mode=enums.ParseMode.HTML
            )

        await callback_query.answer("✅ ꜱᴀᴠᴇᴅ!")


    # ==========================================================
    # /autolockstatus
    # ==========================================================

    @app.on_message(filters.group & filters.command("autolockstatus"))
    async def autolockstatus_cmd(client, message: Message):
        lock_hour = await db.get_autolock_hour(message.chat.id)
        unlock_hour = await db.get_autounlock_hour(message.chat.id)

        lock_text = hour12_label(lock_hour) if lock_hour is not None else "ɴᴏᴛ ꜱᴇᴛ"
        unlock_text = hour12_label(unlock_hour) if unlock_hour is not None else "ɴᴏᴛ ꜱᴇᴛ (ᴍᴀɴᴜᴀʟ ᴜɴʟᴏᴄᴋ ᴏɴʟʏ)"

        await message.reply_text(
            f"╔════════════════╗\n"
            f"  🕐 ᴀᴜᴛᴏ ʟᴏᴄᴋ ꜱᴛᴀᴛᴜꜱ\n"
            f"╚════════════════╝\n\n"
            f"🔒 ᴅᴀɪʟʏ ʟᴏᴄᴋ ᴛɪᴍᴇ: {lock_text}\n"
            f"🔓 ᴅᴀɪʟʏ ᴜɴʟᴏᴄᴋ ᴛɪᴍᴇ: {unlock_text}"
            "",
            parse_mode=enums.ParseMode.HTML
        )


    # ==========================================================
    # /autolockclear
    # ==========================================================

    @app.on_message(filters.group & filters.command("autolockclear"))
    async def autolockclear_cmd(client, message: Message):
        if not await is_power(client, message.chat.id, message.from_user.id):
            return await message.reply_text(
                "❌ ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.", parse_mode=enums.ParseMode.HTML
            )

        await db.clear_autolock_schedule(message.chat.id)
        await message.reply_text(
            "✅ ᴀᴜᴛᴏ-ʟᴏᴄᴋ ꜱᴄʜᴇᴅᴜʟᴇ ᴄʟᴇᴀʀᴇᴅ ꜰᴏʀ ᴛʜɪꜱ ɢʀᴏᴜᴘ.",
            parse_mode=enums.ParseMode.HTML
        )


    # ==========================================================
    # Background scheduler — Fixed for Pyrogram Lifecycle
    # ==========================================================

    async def _scheduler_loop():
        # 🟢 Sabse important fix: Jab tak bot connected nahi hota, loop wait karega
        while not app.is_connected:
            await asyncio.sleep(1)
        
        logger.info("⏰ ᴀᴜᴛᴏ-ʟᴏᴄᴋ ꜱᴄʜᴇᴅᴜʟᴇʀ ʟᴏᴏᴘ ꜱᴛᴀʀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ.")
        
        while True:
            try:
                now = datetime.now()
                today_str = now.strftime("%Y-%m-%d")

                # Har minute database check karega
                chats = await db.get_all_autolock_chats()
                if chats:
                    for chat in chats:
                        chat_id = chat.get("chat_id")
                        lock_hour = chat.get("lock_hour")
                        unlock_hour = chat.get("unlock_hour")
                        last_lock = chat.get("last_lock_date")
                        last_unlock = chat.get("last_unlock_date")

                        # Lock Trigger logic
                        if lock_hour is not None and lock_hour == now.hour and last_lock != today_str:
                            try:
                                await app.set_chat_permissions(chat_id, FULL_LOCKED)
                                for lt in ALL_LOCK_TYPES:
                                    await db.set_lock(chat_id, lt, True)
                                await app.send_message(
                                    chat_id,
                                    "🔒 𝗮𝘂𝘁𝗼-𝗹𝗼𝗰𝗸 𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲𝗱!\n\n"
                                    "→ ᴛʜᴇ ɢʀᴏᴜᴘ ɪꜱ ɴᴏᴡ ꜰᴜʟʟʏ ʟᴏᴄᴋᴇᴅ."
                                    "",
                                    parse_mode=enums.ParseMode.HTML
                                )
                                await db.set_last_lock_date(chat_id, today_str)
                            except Exception as e:
                                logger.error(f"ᴀᴜᴛᴏʟᴏᴄᴋ ᴛʀɪɢɢᴇʀ ᴇʀʀᴏʀ {chat_id}: {e}")

                        # Unlock Trigger logic
                        if unlock_hour is not None and unlock_hour == now.hour and last_unlock != today_str:
                            try:
                                await app.set_chat_permissions(chat_id, FULL_OPEN)
                                for lt in ALL_LOCK_TYPES:
                                    await db.set_lock(chat_id, lt, False)
                                await app.send_message(
                                    chat_id,
                                    "🔓 𝗮𝘂𝘁𝗼-𝘂𝗻𝗹𝗼𝗰𝗸 𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲𝗱!\n\n"
                                    "→ ᴛʜᴇ ɢʀᴏᴜᴘ ɪꜱ ɴᴏᴡ ꜰᴜʟʟʏ ᴏᴘᴇɴ."
                                    "",
                                    parse_mode=enums.ParseMode.HTML
                                )
                                await db.set_last_unlock_date(chat_id, today_str)
                            except Exception as e:
                                logger.error(f"ᴀᴜᴛᴏᴜɴʟᴏᴄᴋ ᴛʀɪɢɢᴇʀ ᴇʀʀᴏʀ {chat_id}: {e}")

            except Exception as e:
                logger.error(f"ᴀᴜᴛᴏʟᴏᴄᴋ ꜱᴄʜᴇᴅᴜʟᴇʀ ʟᴏᴏᴘ ᴇʀʀᴏʀ: {e}")

            # Har 60 seconds (1 minute) me check karega
            await asyncio.sleep(60)

    # Yeh task ab Pyrogram ke active loop ke saath properly attach ho jayega
    loop = asyncio.get_event_loop()
    loop.create_task(_scheduler_loop())
