"""
MIT License

Copyright (c) 2023 TheHamkerCat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import asyncio
import contextlib
import os
import re
from logging import getLogger
from time import time

from pyrogram import Client, enums, filters
from pyrogram import types as pyro_types
from pyrogram.errors import (
    ChatAdminRequired,
    FloodWait,
    PeerIdInvalid,
    UsernameNotOccupied,
)
from pyrogram.types import ChatMember, ChatPrivileges, Message

from database.warn_db import add_warn, get_warn, remove_warns
from misskaty import app
from misskaty.core.decorator.errors import capture_err
from misskaty.core.decorator.permissions import (
    admins_in_chat,
    list_admins,
    member_permissions,
)
from misskaty.core.keyboard import ikb
from misskaty.helper.functions import (
    extract_user,
    extract_user_and_reason,
    int_to_alpha,
    time_converter,
)
from misskaty.helper.localization import use_chat_lang
from misskaty.helper.chat_permissions import empty_chat_permissions
from misskaty.vars import COMMAND_HANDLER, SUDO, OWNER_ID

LOGGER = getLogger("Edith")

__MODULE__ = "Admin"
from misskaty.ui.help_texts import HELP_TEXTS  # noqa: E402

__HELP__ = HELP_TEXTS["admin_help"]


class AdminHelper:
    """Shared helpers for admin actions."""

    @staticmethod
    def is_self(client: Client, user_id: int) -> bool:
        return user_id == client.me.id

    @staticmethod
    def is_sudo_or_owner(user_id: int) -> bool:
        return user_id in SUDO or user_id == OWNER_ID

    @staticmethod
    async def is_admin(chat_id: int, user_id: int) -> bool:
        return user_id in await list_admins(chat_id)

    @staticmethod
    async def safe_api(coro, *, on_not_admin: str | None = None):
        try:
            return await coro, None
        except ChatAdminRequired:
            return None, on_not_admin or "Please give me proper admin permissions."
        except FloodWait as e:
            await asyncio.sleep(e.value)
            return await coro, None
        except Exception as exc:
            return None, str(exc)

    @staticmethod
    async def ensure_restrict_permission(chat_id: int, client: Client, strings) -> bool:
        perms = await member_permissions(chat_id, client.me.id)
        if "can_restrict_members" not in perms:
            await strings("no_ban_permission")
            return False
        return True


# Admin cache reload
@app.on_chat_member_updated(filters.group, group=5)
async def admin_cache_func(_, cmu):
    if cmu.old_chat_member and cmu.old_chat_member.promoted_by:
        try:
            admins_in_chat[cmu.chat.id] = {
                "last_updated_at": time(),
                "data": [
                    member.user.id
                    async for member in app.get_chat_members(
                        cmu.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
                    )
                ],
            }
            LOGGER.info(f"Updated admin cache for {cmu.chat.id} [{cmu.chat.title}]")
        except Exception:
            pass










# Ban users listed in a message
@app.on_message(
    (filters.user(SUDO) | filters.user(OWNER_ID)) & filters.command("listban", COMMAND_HANDLER) & filters.group
)
@use_chat_lang()
async def list_ban_(c, message, strings):
    userid, msglink_reason = await extract_user_and_reason(message)
    if not userid or not msglink_reason:
        return await message.reply_text(strings("give_idban_with_msg_link"))
    if len(msglink_reason.split(" ")) == 1:
        return await message.reply_text(strings("give_reason_list_ban"))
    lreason = msglink_reason.split()
    messagelink, reason = lreason[0], " ".join(lreason[1:])
    if not re.search(r"(https?://)?t(telegram)?\.me/\w+/\d+", messagelink):
        return await message.reply_text(strings("invalid_tg_link"))
    if AdminHelper.is_self(c, userid):
        return await message.reply_text(strings("ban_self_err"))
    if AdminHelper.is_sudo_or_owner(userid):
        return await message.reply_text(strings("ban_sudo_err"))
    splitted = messagelink.split("/")
    uname, mid = splitted[-2], int(splitted[-1])
    m = await message.reply_text(strings("multiple_ban_progress"))
    try:
        msgtext = (await app.get_messages(uname, mid)).text
        gusernames = re.findall(r"@\w+", msgtext)
    except Exception:
        return await m.edit_text(strings("failed_get_uname"))
    count = 0
    for username in gusernames:
        try:
            await app.ban_chat_member(username.strip("@"), userid)
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception:
            continue
        count += 1
    mention = (await app.get_users(userid)).mention
    msg = strings("listban_msg").format(
        mention=mention, uid=userid, frus=message.from_user.mention, ct=count, reas=reason
    )
    await m.edit_text(msg)


# Unban users listed in a message
@app.on_message(
    (filters.user(SUDO) | filters.user(OWNER_ID)) & filters.command("listunban", COMMAND_HANDLER) & filters.group
)
@use_chat_lang()
async def list_unban(_, message, strings):
    userid, msglink = await extract_user_and_reason(message)
    if not userid or not msglink:
        return await message.reply_text(strings("give_idunban_with_msg_link"))
    if not re.search(r"(https?://)?t(telegram)?\.me/\w+/\d+", msglink):
        return await message.reply_text(strings("invalid_tg_link"))
    splitted = msglink.split("/")
    uname, mid = splitted[-2], int(splitted[-1])
    m = await message.reply_text(strings("multiple_unban_progress"))
    try:
        msgtext = (await app.get_messages(uname, mid)).text
        gusernames = re.findall(r"@\w+", msgtext)
    except Exception:
        return await m.edit_text(strings("failed_get_uname"))
    count = 0
    for username in gusernames:
        try:
            await app.unban_chat_member(username.strip("@"), userid)
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception:
            continue
        count += 1
    mention = (await app.get_users(userid)).mention
    msg = strings("listunban_msg").format(
        mention=mention, uid=userid, frus=message.from_user.mention, ct=count
    )
    await m.edit_text(msg)
















@app.on_callback_query(filters.regex("unwarn_"))
@use_chat_lang()
async def remove_warning(_, cq, strings):
    from_user = cq.from_user
    chat_id = cq.message.chat.id
    permissions = await member_permissions(chat_id, from_user.id)
    if "can_restrict_members" not in permissions:
        return await cq.answer(
            strings("no_permission_error").format(permissions=permissions),
            show_alert=True,
        )
    user_id = int(cq.data.split("_")[1])
    warns = await get_warn(chat_id, await int_to_alpha(user_id))
    warns = warns["warns"] if warns else 0
    if not warns or warns == 0:
        return await cq.answer(
            strings("user_no_warn").format(
                mention=(
                    cq.message.reply_to_message.from_user.mention
                    if cq.message.reply_to_message and cq.message.reply_to_message.from_user
                    else f"<code>{user_id}</code>"
                )
            )
        )
    warn = {"warns": warns - 1}
    await add_warn(chat_id, await int_to_alpha(user_id), warn)
    text = (cq.message.text.markdown or "") if cq.message.text else ""
    text = f"~~{text}~~\n\n"
    text += strings("unwarn_msg").format(mention=from_user.mention)
    await cq.message.edit(text)


@app.on_callback_query(filters.regex("unmute_"))
@use_chat_lang()
async def unmute_user(_, cq, strings):
    from_user = cq.from_user
    chat_id = cq.message.chat.id
    permissions = await member_permissions(chat_id, from_user.id)
    if "can_restrict_members" not in permissions:
        return await cq.answer(
            strings("no_permission_error").format(permissions=permissions),
            show_alert=True,
        )
    user_id = int(cq.data.split("_")[1])
    text = (cq.message.text.markdown or "") if cq.message.text else ""
    text = f"~~{text}~~\n\n"
    text += strings("rmmute_msg").format(mention=from_user.mention)
    _, err = await AdminHelper.safe_api(cq.message.chat.unban_member(user_id))
    if err:
        return await cq.answer(str(err))
    await cq.message.edit(text)


@app.on_callback_query(filters.regex("unban_"))
@use_chat_lang()
async def unban_user(_, cq, strings):
    from_user = cq.from_user
    chat_id = cq.message.chat.id
    permissions = await member_permissions(chat_id, from_user.id)
    if "can_restrict_members" not in permissions:
        return await cq.answer(
            strings("no_permission_error").format(permissions=permissions),
            show_alert=True,
        )
    user_id = int(cq.data.split("_")[1])
    text = (cq.message.text.markdown or "") if cq.message.text else ""
    text = f"~~{text}~~\n\n"
    text += strings("unban_msg").format(mention=from_user.mention)
    _, err = await AdminHelper.safe_api(cq.message.chat.unban_member(user_id))
    if err:
        return await cq.answer(str(err))
    await cq.message.edit(text)






# Report User in Group
@app.on_message(
    (
        filters.command("report", COMMAND_HANDLER)
        | filters.command(["admins", "admin"], prefixes="@")
    )
    & filters.group
)
@capture_err
@use_chat_lang()
async def report_user(_, ctx: Message, strings) -> Message:
    if len(ctx.text.split()) <= 1 and not ctx.reply_to_message:
        return await ctx.reply(strings("report_no_reply"))
    reply = ctx.reply_to_message if ctx.reply_to_message else ctx
    if reply.from_user:
        reply_id = reply.from_user.id
        user_mention = reply.from_user.mention
    elif reply.sender_chat:
        reply_id = reply.sender_chat.id
        user_mention = reply.sender_chat.title or "Anon"
    else:
        return await ctx.reply(strings("report_no_reply"))
    user_id = ctx.from_user.id if ctx.from_user else ctx.sender_chat.id
    if reply_id == user_id:
        return await ctx.reply(strings("report_self_err"))

    list_of_admins = await list_admins(ctx.chat.id)
    linked_chat = (await app.get_chat(ctx.chat.id)).linked_chat
    if linked_chat is None:
        if reply_id in list_of_admins or reply_id == ctx.chat.id:
            return await ctx.reply(strings("reported_is_admin"))
    elif (
        reply_id in list_of_admins
        or reply_id == ctx.chat.id
        or reply_id == linked_chat.id
    ):
        return await ctx.reply(strings("reported_is_admin"))
    text = strings("report_msg").format(user_mention=user_mention)
    admin_data = [
        m
        async for m in app.get_chat_members(
            ctx.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
        )
    ]
    for admin in admin_data:
        if admin.user.is_bot or admin.user.is_deleted:
            continue
        text += f"<a href='tg://user?id={admin.user.id}'>\u2063</a>"
    await reply.reply(text)


@app.on_cmd("set_chat_title", self_admin=True, group_only=True)
@app.adminsOnly("can_change_info")
@use_chat_lang()
async def set_chat_title(_, ctx: Message, strings):
    if len(ctx.command) < 2:
        return await ctx.reply_text(f"**Usage:**\n/{ctx.command[0]} NEW NAME")
    old_title = ctx.chat.title
    new_title = ctx.text.split(None, 1)[1]
    _, err = await AdminHelper.safe_api(ctx.chat.set_title(new_title))
    if err:
        return await ctx.reply(err)
    await ctx.reply_text(
        strings("chat_title_changed").format(old=old_title, new=new_title)
    )


@app.on_cmd("set_user_title", self_admin=True, group_only=True)
@app.adminsOnly("can_change_info")
@use_chat_lang()
async def set_user_title(_, ctx: Message, strings):
    if not ctx.reply_to_message:
        return await ctx.reply_text("Reply to user's message to set his admin title")
    if not ctx.reply_to_message.from_user:
        return await ctx.reply_text("I can't change admin title of an unknown entity")
    if len(ctx.command) < 2:
        return await ctx.reply_text(
            "**Usage:**\n/set_user_title NEW ADMINISTRATOR TITLE"
        )
    title = ctx.text.split(None, 1)[1]
    from_user = ctx.reply_to_message.from_user
    _, err = await AdminHelper.safe_api(app.set_administrator_title(ctx.chat.id, from_user.id, title))
    if err:
        return await ctx.reply(err)
    await ctx.reply_text(
        strings("user_title_changed").format(mention=from_user.mention, title=title)
    )


@app.on_cmd("set_chat_photo", self_admin=True, group_only=True)
@app.adminsOnly("can_change_info")
@use_chat_lang()
async def set_chat_photo(_, ctx: Message, strings):
    reply = ctx.reply_to_message

    if not reply:
        return await ctx.reply_text("Reply to a photo to set it as chat_photo")

    file = reply.document or reply.photo
    if not file:
        return await ctx.reply_text(
            "Reply to a photo or document to set it as chat_photo"
        )

    if file.file_size > 5000000:
        return await ctx.reply("File size too large.")

    photo = await reply.download()
    _, err = await AdminHelper.safe_api(ctx.chat.set_photo(photo=photo))
    try:
        if err:
            return await ctx.reply(f"Failed changed group photo. ERROR: {err}")
        await ctx.reply_text(strings("chat_photo_changed"))
    finally:
        with contextlib.suppress(FileNotFoundError):
            os.remove(photo)


@app.on_message(filters.group & filters.command("mentionall", COMMAND_HANDLER))
async def mentionall(client: Client, msg: Message):
    if not msg.from_user:
        return
    member = await msg.chat.get_member(msg.from_user.id)
    if member.status not in (
        enums.ChatMemberStatus.OWNER,
        enums.ChatMemberStatus.ADMINISTRATOR,
    ):
        return await client.send_message(
            msg.chat.id,
            "Admins only can do that !",
            reply_parameters=pyro_types.ReplyParameters(message_id=msg.id),
        )
    total = []
    async for m in client.get_chat_members(msg.chat.id):
        if not m.user or m.user.is_deleted:
            continue
        total.append(f"@{m.user.username}" if m.user.username else m.user.mention())

    if not total:
        return await msg.reply("No mentionable members found.")

    NUM = 4
    for i in range(0, len(total), NUM):
        text = "\n".join(total[i : i + NUM])
        try:
            await client.send_message(
                msg.chat.id,
                text,
                message_thread_id=msg.message_thread_id,
            )
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception as err:
            LOGGER.warning(f"mentionall chunk failed: {err}")
