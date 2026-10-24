# ============================================================
#  Edith — Group Manager Suite loader
#  Owner : Mister Stark
#  Edith ke saare group-management modules yaha register hote hain.
# ============================================================
import functools
from logging import getLogger

from misskaty import app

LOGGER = getLogger("Edith.Suite")


class _EdithApp:
    """Edith handlers ke liye thin proxy.

    Restriction handlers (anti-link, anti-flood, locks, abuse ...) ko approved
    users ke liye skip karta hai — bina MissKaty ke dusre handlers ko rokhe.
    """

    def __init__(self, client):
        self._client = client

    def __getattr__(self, name):
        return getattr(self._client, name)

    def on_message(self, flt=None, group: int = 0):
        deco = self._client.on_message(flt, group)

        def wrapper(func):
            if group == 0:
                return deco(func)

            @functools.wraps(func)
            async def inner(client, message, *args, **kwargs):
                if (
                    message.from_user
                    and message.chat
                    and message.chat.type.name in ("GROUP", "SUPERGROUP")
                    and not getattr(message, "command", None)
                    and not getattr(message, "service", None)
                ):
                    from misskaty.edith import db

                    if await db.is_approved(message.chat.id, message.from_user.id):
                        return
                return await func(client, message, *args, **kwargs)

            return deco(inner)

        return wrapper


_proxy = _EdithApp(app)

# (module, register function) — order Edith ke original main.py jaisa
_MODULES = [
    ("warns", "register_warns_handler"),
    ("captcha", "register_captcha_handler"),
    ("forward", "register_forward_handler"),
    ("fancy_text", "register_fancy_text_handler"),
    ("anti_sticker", "register_anti_sticker_handler"),
    ("anti_link", "register_anti_link_handler"),
    ("disable", "register_disable_handler"),
    ("autolock", "register_autolock_handler"),
    ("approve", "register_approve_handler"),
    ("antiflood", "register_antiflood_handler"),
    ("groupinfo", "register_groupinfo_handler"),
    ("couple", "register_couple_handler"),
    ("group_commands", "register_group_commands"),
    ("abuse", "register_abuse_handler"),
    ("fsub", "register_fsub_handler"),
    ("tools", "register_tools_handler"),
    ("utility", "register_utility_handler"),
    ("cmddeleter", "register_cmddeleter_handler"),
    ("mediadelete", "register_mediadelete_handler"),
    ("zombie", "register_zombie_handler"),
    ("tagall", "register_tagall_handler"),
    ("promote", "register_promote_handler"),
    ("cleaner", "register_cleaner_handler"),
    ("joinrequest", "register_joinrequest_handler"),
    ("ghost", "register_ghost_handler"),
    ("antiraid", "register_antiraid_handler"),
    ("blackuser", "register_blackuser_handler"),
    ("welcome", "register_welcome_handler"),
    ("admin_tag", "register_admin_tag_handler"),
    ("logger", "register_logger_handler"),
]

import importlib

for _mod, _fn in _MODULES:
    try:
        getattr(importlib.import_module(f"misskaty.edith.handlers.{_mod}"), _fn)(_proxy)
    except Exception as e:  # ek module fail ho to baaki chalte rahein
        LOGGER.error("Edith module %s load nahi hua: %s", _mod, e, exc_info=True)
