# ============================================================
#  EDITH — Central Config (hardcoded, no .env needed)
#  Owner : Mister Stark
#  Yaha sab values direct bhar do, koi environment variable nahi.
# ============================================================
import sys
from logging import getLogger

LOGGER = getLogger("Edith")

# ---------------------------------------------------------- Telegram core
API_ID = 36469348                          # my.telegram.org se
API_HASH = "0334725d7d237fc177cb798e8b762839"                       # my.telegram.org se
BOT_TOKEN = ""                      # @BotFather se
USER_SESSION = None                 # optional: pyrogram session string (userbot features)

# ---------------------------------------------------------- Database
DATABASE_URI = ""                   # MongoDB connection string
DATABASE_NAME = "EdithDB"           # MissKaty-side modules ka database
EDITH_DB_NAME = "EdithGroupDB"      # Edith group-manager modules ka alag database

# ---------------------------------------------------------- Owner / Sudo
OWNER_ID = 5864182070                        # Mister Stark ka Telegram user id
SUDO = [5864182070]                   # extra sudo users ke ids is list me daalo
OWNER_NAME = "Mister Stark"
BOT_DISPLAY_NAME = "Edith"

# ---------------------------------------------------------- Logs / Channels
LOG_CHANNEL = -1003596436416                     # log channel id (-100...)
LOG_GROUP_ID = None
SUPPORT_CHAT = "CarelessxWorld"                           # username without @
SUPPORT_GROUP = "https://t.me/CarelessxWorld"             # support group link
UPDATE_CHANNEL = "https://t.me/+wQonHdyvZh5mZWM1"         # update channel link
START_IMAGE = "https://files.catbox.moe/v8vvxr.jpg"       # start/help photo
PRIVACY_IMAGE = "https://files.catbox.moe/v8vvxr.jpg"     # /privacy photo
PRIVACY_POLICY_URL = "https://graph.org/Anya-Bots---Privacy-Policy-04-12"

# ---------------------------------------------------------- Runtime
TZ = "Asia/Kolkata"
PORT = 8080
COMMAND_HANDLER = ["!", "/"]
AUTO_RESTART = False
YT_COOKIES = None
WEBAPP_URL = ""

# ---------------------------------------------------------- Mini App Games (Telegram Web Apps)
# Full https link daalo. Khali chhodoge to wo game /game me nahi dikhega.
BILLIARD_GAME_URL = "https://mrstark87.github.io/Pool/"              # Pool / Billiard mini app ka link
SHOOTER_GAME_URL = "https://mrstark87.github.io/Gamee/"               # Space Shooter mini app ka link
BILLIARD_URL = BILLIARD_GAME_URL or (WEBAPP_URL.rstrip("/") + "/billiard" if WEBAPP_URL else "")

# ---------------------------------------------------------- AI (/ai , /ask) — Grok (xAI)
GROK_API_KEY = ""                   # <-- apni Grok API key yaha daalo
GROK_MODEL = "llama-3.1-8b-instant"                     # <-- Grok model name yaha daalo (e.g. grok-...)
GROK_BASE_URL = "https://api.x.ai/v1"

# ---------------------------------------------------------- Optional keys
CURRENCY_API = None

# ---------------------------------------------------------- Payments (optional, Paydisini)
PAYDISINI_KEY = None
PAYDISINI_CHANNEL_ID = "17"

# ---------------------------------------------------------- Auto Forwarder (optional)
FORWARD_FROM_CHAT_ID = []
FORWARD_TO_CHAT_ID = []
FORWARD_FILTERS = ["video", "document"]
BLOCK_FILES_WITHOUT_EXTENSIONS = True
BLOCKED_EXTENSIONS = ["html", "htm", "json", "txt", "php", "gif", "png", "ink", "torrent", "url", "nfo", "xml", "xhtml", "jpg"]
MINIMUM_FILE_SIZE = None

# ---------------------------------------------------------- Sanity check
for _name, _val in (("API_ID", API_ID), ("API_HASH", API_HASH), ("BOT_TOKEN", BOT_TOKEN), ("DATABASE_URI", DATABASE_URI), ("OWNER_ID", OWNER_ID), ("LOG_CHANNEL", LOG_CHANNEL)):
    if not _val:
        LOGGER.error("%s vars.py me set nahi hai! Exiting now", _name)
        sys.exit(1)
