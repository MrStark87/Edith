"""
* @author        Yasir Aris M <yasiramunandar@gmail.com>
* @created       2026-09-16
* @projectName   MissKatyPyro
* Copyright @YasirPedia All rights reserved
"""
from pyrogram import enums, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    WebAppInfo,
)

from misskaty import app
from misskaty.core.decorator import capture_err
from misskaty.vars import COMMAND_HANDLER, WEBAPP_URL
from misskaty.ui import buttons as UIB

__MODULE__ = "Billiard"
from misskaty.ui.help_texts import HELP_TEXTS  # noqa: E402

__HELP__ = HELP_TEXTS["billiard_help"]


@app.on_message(filters.command(["billiard", "pool", "biliard"], COMMAND_HANDLER))
@capture_err
async def billiard_cmd(_, message: Message):
    if not WEBAPP_URL:
        return await message.reply("⚠️ WEBAPP_URL belum diset di environment.")
    billiard_url = f"{WEBAPP_URL.rstrip('/')}/billiard"
    text = (
        "<emoji id=\"5935847413859225147\">🎱</emoji> <b>Edith 8-Ball Pool Mini App</b>\n\n"
        "Mainkan game biliar langsung di dalam Telegram!\n\n"
        "• <b>Fisika 2D Realistis</b>: Tubrukan antar-bola & pantulan ban meja\n"
        "• <b>Aim & Laser Guide</b>: Garis bidik presisi + ghost ball projection\n"
        "• <b>Power Control</b>: Tarik stik biliar ke belakang untuk mengatur power\n"
        "• <b>Haptic & Sound FX</b>: Efek suara benturan bola & getaran HP native\n\n"
        "Klik tombol di bawah untuk mulai bermain:"
    )
    keyboard = UIB.billiard__billiard_cmd_1(billiard_url=billiard_url)
    await message.reply(text, reply_markup=keyboard)
