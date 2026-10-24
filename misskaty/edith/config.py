# ============================================================
#  Edith group-manager modules ka config — sab values
#  misskaty/vars.py se aati hain (wahi ek jagah edit karo).
# ============================================================
from misskaty import BOT_USERNAME
from misskaty.vars import (
    DATABASE_URI as MONGO_URI,
    EDITH_DB_NAME as DB_NAME,
    LOG_CHANNEL as LOG_CHANNEL_ID,
    OWNER_ID,
    PRIVACY_IMAGE,
    START_IMAGE,
    SUPPORT_GROUP,
    UPDATE_CHANNEL,
)

__all__ = [
    "BOT_USERNAME", "MONGO_URI", "DB_NAME", "LOG_CHANNEL_ID", "OWNER_ID",
    "PRIVACY_IMAGE", "START_IMAGE", "SUPPORT_GROUP", "UPDATE_CHANNEL",
]
