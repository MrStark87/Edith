from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    ChatJoinRequest,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from database import dbname
from misskaty import app
from misskaty.core.decorator.permissions import adminsOnly, member_permissions
from misskaty.vars import COMMAND_HANDLER, SUDO, OWNER_ID
from misskaty.ui import buttons as UIB

approvaldb = dbname["autoapprove"]

# For /help menu
__MODULE__ = "Autoapprove"
from misskaty.ui.help_texts import HELP_TEXTS  # noqa: E402

__HELP__ = HELP_TEXTS["autoapprove_help"]


@app.on_message(filters.command("autoapprove", COMMAND_HANDLER) & filters.group)
@adminsOnly("can_change_info")
async def approval_command(_, message: Message):
    chat_id = message.chat.id
    if (await approvaldb.count_documents({"chat_id": chat_id})) > 0:
        keyboard_OFF = UIB.autoapprove__approval_command_1()
        await message.reply(
            "**Autoapproval for this chat: Enabled.**",
            reply_markup=keyboard_OFF,
        )
    else:
        keyboard_ON = UIB.autoapprove__approval_command_2()
        await message.reply(
            "**Autoapproval for this chat: Disabled.**",
            reply_markup=keyboard_ON,
        )


@app.on_callback_query(filters.regex(r"^approval_(on|off)$"))
async def approval_cb(_, cb: CallbackQuery):
    chat_id = cb.message.chat.id
    from_user = cb.from_user

    permissions = await member_permissions(chat_id, from_user.id)
    permission = "can_restrict_members"
    if permission not in permissions:
        if from_user.id not in SUDO or from_user.id != OWNER_ID:
            return await cb.answer(
                f"You don't have the required permission.\n Permission: {permission}",
                show_alert=True,
            )

    parts = cb.data.split("_", 1)
    if len(parts) != 2:
        return await cb.answer()
    option = parts[1]

    if option == "on":
        if await approvaldb.count_documents({"chat_id": chat_id}) == 0:
            approvaldb.insert_one({"chat_id": chat_id})
            keyboard_off = UIB.autoapprove__approval_cb_1()
            await cb.edit_message_text(
                "**Autoapproval for this chat: Enabled.**",
                reply_markup=keyboard_off,
            )
    elif option == "off":
        if await approvaldb.count_documents({"chat_id": chat_id}) > 0:
            approvaldb.delete_one({"chat_id": chat_id})
            keyboard_on = UIB.autoapprove__approval_cb_2()
            await cb.edit_message_text(
                "**Autoapproval for this chat: Disabled.**",
                reply_markup=keyboard_on,
            )
    return await cb.answer()


@app.on_chat_join_request(filters.group)
async def accept(_, message: ChatJoinRequest):
    chat = message.chat
    user = message.from_user
    if (await approvaldb.count_documents({"chat_id": chat.id})) > 0:
        await app.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
