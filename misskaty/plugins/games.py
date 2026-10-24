# ============================================================
#  EDITH — Mini App Games  (/game , /shoot)
#  Owner : Mister Stark
#  Game links  ->  misskaty/vars.py  (BILLIARD_GAME_URL, SHOOTER_GAME_URL)
#  Buttons     ->  misskaty/ui/buttons.py
# ============================================================
from pyrogram import enums, filters
from pyrogram.types import Message

from misskaty import app
from misskaty.core.decorator import capture_err
from misskaty.ui import buttons as UIB
from misskaty.ui.help_texts import HELP_TEXTS
from misskaty.vars import BILLIARD_URL, COMMAND_HANDLER, SHOOTER_GAME_URL

__MODULE__ = "Games"
__HELP__ = HELP_TEXTS["games_help"]

HTML = enums.ParseMode.HTML


@app.on_message(filters.command("game", COMMAND_HANDLER))
@capture_err
async def game_menu(_, message: Message):
    if not (BILLIARD_URL or SHOOTER_GAME_URL):
        return await message.reply("⚠️ Game links are not set in misskaty/vars.py.")
    await message.reply_text(
        "🎮 <b>Here are my games</b>\n\nChoose a game below and play right inside Telegram:",
        reply_markup=UIB.games_menu(billiard_url=BILLIARD_URL, shooter_url=SHOOTER_GAME_URL),
        parse_mode=HTML,
    )


@app.on_message(filters.command("shoot", COMMAND_HANDLER))
@capture_err
async def shoot_cmd(_, message: Message):
    if not SHOOTER_GAME_URL:
        return await message.reply("⚠️ SHOOTER_GAME_URL is not set in misskaty/vars.py.")
    await message.reply_text(
        "🚀 <b>Edith Space Shooter Mini App</b>\n\n"
        "Fly your ship, shoot down the enemies and beat your high score!\n\n"
        "Tap the button below to start playing:",
        reply_markup=UIB.shooter_play(shooter_url=SHOOTER_GAME_URL),
        parse_mode=HTML,
    )
    
