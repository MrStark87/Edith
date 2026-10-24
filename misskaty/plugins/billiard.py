
from pyrogram import enums, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    WebAppInfo,
)

from misskaty import app
from misskaty.core.decorator import capture_err
from misskaty.vars import BILLIARD_URL, COMMAND_HANDLER
from misskaty.ui import buttons as UIB

__MODULE__ = "Billiard"
from misskaty.ui.help_texts import HELP_TEXTS  # noqa: E402

__HELP__ = HELP_TEXTS["games_help"]


@app.on_message(filters.command(["billiard", "pool", "biliard"], COMMAND_HANDLER))
@capture_err
async def billiard_cmd(_, message: Message):
    if not BILLIARD_URL:
        return await message.reply("⚠️ BILLIARD_GAME_URL is not set in misskaty/vars.py.")
    billiard_url = BILLIARD_URL
    text = (
        "<emoji id=\"5935847413859225147\">🎱</emoji> <b>Edith 8-Ball Pool Mini App</b>\n\n"
        "Play billiards right inside Telegram!\n\n"
        "• <b>Realistic 2D Physics</b>: ball collisions and cushion bounces\n"
        "• <b>Aim & Laser Guide</b>: precise aim line with ghost ball projection\n"
        "• <b>Power Control</b>: pull the cue back to set the power\n"
        "• <b>Haptic & Sound FX</b>: ball hit sounds and native phone vibration\n\n"
        "Tap the button below to start playing:"
    )
    keyboard = UIB.billiard__billiard_cmd_1(billiard_url=billiard_url)
    await message.reply(text, reply_markup=keyboard)
    
