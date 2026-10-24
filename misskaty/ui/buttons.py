# ============================================================
#  EDITH — INLINE BUTTONS  (sirf yahi file edit karo)
#  Owner : Mister Stark
#
#  - Saare inline keyboards / buttons ke labels, colors (style), rows yaha hain.
#  - Plugins ke keyboards/buttons yaha functions me hain (UIB.<function> se call hote hain).
#  - Naya menu/keyboard banana ho to bhi yahi function likho.
#  - Help menu me kaunsa button kis category me jayega -> HELP_CATEGORIES.
#  - ButtonStyle: PRIMARY (blue) / SUCCESS (green) / DANGER (red)
# ============================================================
from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram import enums
from pyrogram.types import WebAppInfo

PRIMARY = ButtonStyle.PRIMARY
SUCCESS = ButtonStyle.SUCCESS
DANGER = ButtonStyle.DANGER

# ------------------------------------------------------------
#  HELP MENU DATA
#  category -> (title, [(button label, help key), ...])
#  help key = help_texts.HELP_TEXTS ki key
# ------------------------------------------------------------
HELP_CATEGORIES = {
    "moderation": ("ᴍᴏᴅᴇʀᴀᴛɪᴏɴ", [
        ("🔮 ᴍᴏᴅᴇʀᴀᴛɪᴏɴ ⌯", "moderation"),
        ("⚠️ ᴡᴀʀɴꜱ ⌯", "warns_help"),
        ("🚷 ʙʟ ᴜꜱᴇʀ ⌯", "blackuser_help"),
        ("🚫 ʙʟ ᴡᴏʀᴅꜱ ⌯", "blacklist_help"),
        ("🤬 ᴀʙᴜꜱᴇ ⌯", "abuse_help"),
        ("🗑️ ᴄᴍᴅ ᴅᴇʟ ⌯", "cmd_help"),
        ("🚮 ᴍᴇᴅɪᴀ ᴅᴇʟ ⌯", "mediadelete_help"),
        ("🆘 ᴀᴅᴍɪɴ ᴛᴀɢ ⌯", "admin_tag_help"),
        ("👮🏻 ᴘʀᴏᴍᴏᴛɪᴏɴ ⌯", "promote_help"),
        ("🛠️ ᴀᴅᴍɪɴ ᴛᴏᴏʟꜱ ⌯", "admin_help"),
        ("⌛ ʟᴏɴɢ ʟɪᴍɪᴛ ⌯", "longmsg_help"),
        ("#️⃣ ʜᴀꜱʜᴛᴀɢ ⌯", "hashtag_help"),
        ("🌐 ꜰᴇᴅᴇʀᴀᴛɪᴏɴ ⌯", "federation_help"),
        ("🧹 ɪɴᴋɪᴄᴋ ⌯", "inkick_help"),
    ]),
    "security": ("ꜱᴇᴄᴜʀɪᴛʏ", [
        ("🔐 ʟᴏᴄᴋꜱ ⌯", "locks"),
        ("🕐 ᴀᴜᴛᴏ ʟᴏᴄᴋ ⌯", "autolock_help"),
        ("🔡 ᴄᴀᴘᴛᴄʜᴀ ⌯", "captcha_help"),
        ("〽️ ʙɪᴏ ʟɪɴᴋ ⌯", "biolink"),
        ("🔗 ᴀɴᴛɪ ʟɪɴᴋ ⌯", "anti_link_help"),
        ("🪠 ꜰ-ꜱᴜʙ ⌯", "fsub_help"),
        ("🧴 ᴄʟᴇᴀɴᴇʀ ⌯", "cleaner_help"),
        ("📵 ᴘʜᴏɴᴇ ⌯", "phone_help"),
        ("🎭 ᴀɴᴛɪ ꜱᴛɪᴄᴋᴇʀ ⌯", "anti_sticker_help"),
        ("🧟 ᴢᴏᴍʙɪᴇꜱ ⌯", "zombie_help"),
        ("👻 ɢʜᴏꜱᴛ ⌯", "ghost_help"),
        ("🤿 ꜰɪʟᴛᴇʀꜱ ⌯", "filters_help"),
        ("⛩️ ᴊᴏɪɴ ʀᴇǫᴜᴇꜱᴛ ⌯", "joinrequest_help"),
        ("🛡️ ᴀɴᴛɪ ʀᴀɪᴅ ⌯", "antiraid_help"),
        ("🌊 ᴀɴᴛɪ ꜰʟᴏᴏᴅ ⌯", "antiflood_help"),
        ("⚙️ ᴅɪꜱᴀʙʟᴇ ⌯", "disable_help"),
        ("🪭 ꜰᴀɴᴄʏ ᴛᴇxᴛ ⌯", "fancy_text_help"),
        ("🌙 ɴɪɢʜᴛ ᴍᴏᴅᴇ ⌯", "nightmode_help"),
        ("✅ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴇ ⌯", "autoapprove_help"),
        ("🕵️ ꜱᴀɴɢᴍᴀᴛᴀ ⌯", "sangmata_help"),
        ("🕊 ᴀᴘᴘʀᴏᴠᴇ ⌯", "approve_help"),
    ]),
    "utility": ("ᴜᴛɪʟɪᴛʏ", [
        ("💌 ɢʀᴇᴇᴛɪɴɢꜱ ⌯", "greetings"),
        ("📝 ɴᴏᴛᴇꜱ ⌯", "notes_help"),
        ("📑 ʀᴜʟᴇꜱ ⌯", "rules_help"),
        ("⚙️ ᴜᴛɪʟɪᴛʏ ⌯", "utility_help"),
        ("🔖 ᴛᴀɢ ᴀʟʟ ⌯", "tagall_help"),
        ("📤 ꜰᴏʀᴡᴀʀᴅ ⌯", "forward_help"),
        ("💤 ᴀꜰᴋ ⌯", "afk_help"),
        ("⭐ ᴋᴀʀᴍᴀ ⌯", "karma_help"),
        ("🎀 ᴊᴏɪɴ/ʟᴇᴀᴠᴇ ⌯", "join_help"),
    ]),
    "groups": ("ɢʀᴏᴜᴘꜱ", [
        ("👥 ɢʀᴏᴜᴘ ⌯", "groupinfo_help"),
        ("🔗 ɪɴᴠɪᴛᴇ ʟɪɴᴋ ⌯", "linkinfo_help"),
    ]),
    "tools": ("ᴀɪ & ᴛᴏᴏʟꜱ", [
        ("🤖 ᴇᴅɪᴛʜ ᴀɪ ⌯", "ai_help"),
        ("🧰 ᴍɪꜱᴄ ᴛᴏᴏʟꜱ ⌯", "misc_help"),
        ("🔎 ꜱᴇᴀʀᴄʜ ⌯", "search_help"),
        ("🔍 ᴏᴄʀ ⌯", "ocr_help"),
        ("📋 ᴘᴀꜱᴛᴇ ⌯", "paste_help"),
        ("✍️ ɴᴜʟɪꜱ ⌯", "nulis_help"),
        ("📸 ᴡᴇʙ ꜱꜱ ⌯", "webss_help"),
        ("💻 ᴄᴏᴅᴇ ᴛᴇꜱᴛᴇʀ ⌯", "codetester_help"),
        ("💱 ᴄᴜʀʀᴇɴᴄʏ ⌯", "currency_help"),
        ("🔑 ꜱᴇꜱꜱɪᴏɴ ⌯", "session_help"),
        ("🔗 ʙʏᴘᴀꜱꜱ ⌯", "bypass_help"),
        ("⌨️ ɪɴʟɪɴᴇ ⌯", "inline_help"),
    ]),
    "media": ("ᴍᴇᴅɪᴀ", [
        ("📥 ꜱᴏᴄɪᴀʟ ᴅʟ ⌯", "sosmed_help"),
        ("🎞️ ᴍᴇᴅɪᴀ ᴛᴏᴏʟꜱ ⌯", "mediatool_help"),
        ("🎧 ᴇxᴛʀᴀᴄᴛᴏʀ ⌯", "mediaextract_help"),
        ("🎭 ꜱᴛɪᴄᴋᴇʀꜱ ⌯", "stickers_help"),
        ("💬 ǫᴜᴏᴛʟʏ ⌯", "quotly_help"),
        ("🎬 ᴍᴏᴠɪᴇ ꜱᴄʀᴀᴘᴇʀ ⌯", "scraper_help"),
        ("🕌 ᴘʀᴀʏᴇʀ ⌯", "prayer_help"),
    ]),
    "fun": ("ꜰᴜɴ", [
        ("🎮 ꜰᴜɴ ⌯", "fun_help"),
        ("🎱 ʙɪʟʟɪᴀʀᴅ ⌯", "billiard_help"),
        ("💞 ᴄᴏᴜᴘʟᴇ ⌯", "couple_help"),
    ]),
    "owner": ("ᴏᴡɴᴇʀ", [
        ("👑 ᴏᴡɴᴇʀ ⌯", "owner_help"),
        ("📊 ʙᴏᴛ ɪɴꜰᴏ ⌯", "stats_help"),
    ]),
}

# Help menu ke main buttons (2 per row). (label, category)
HELP_MENU_LAYOUT = [
    [("🔮 ᴍᴏᴅᴇʀᴀᴛɪᴏɴ", "moderation"), ("🛡️ ꜱᴇᴄᴜʀɪᴛʏ", "security")],
    [("⚙️ ᴜᴛɪʟɪᴛʏ", "utility"), ("👥 ɢʀᴏᴜᴘꜱ", "groups")],
    [("🤖 ᴀɪ & ᴛᴏᴏʟꜱ", "tools"), ("🎬 ᴍᴇᴅɪᴀ", "media")],
    [("🎮 ꜰᴜɴ", "fun"), ("👑 ᴏᴡɴᴇʀ", "owner")],
]


def category_of(key: str):
    for cat, (_, items) in HELP_CATEGORIES.items():
        if any(k == key for _, k in items):
            return cat
    return "utility"


# ------------------------------------------------------------
#  START / GROUP / PRIVACY BUTTONS
# ------------------------------------------------------------
def start_menu(bot_username, support_url, update_url):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("✙ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✙", url=f"https://t.me/{bot_username}?startgroup=true", style=PRIMARY)],
        [
            InlineKeyboardButton("⌯ ꜱᴜᴘᴘᴏʀᴛ ⌯", url=support_url, style=SUCCESS),
            InlineKeyboardButton("⌯ ᴜᴘᴅᴀᴛᴇ ⌯", url=update_url, style=SUCCESS),
        ],
        [InlineKeyboardButton("⌯ ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ⌯", callback_data="help", style=PRIMARY)],
        [InlineKeyboardButton("⌯ ꜱʏꜱᴛᴇᴍ ꜱᴛᴀᴛꜱ ⌯", callback_data="stats_callback", style=SUCCESS)],
    ])


def group_start(bot_username, support_url):
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("✙ ᴀᴅᴅ ᴍᴇ ✙", url=f"https://t.me/{bot_username}?startgroup=true", style=PRIMARY),
        InlineKeyboardButton("⌯ ꜱᴜᴘᴘᴏʀᴛ ⌯", url=support_url, style=SUCCESS),
    ]])


def group_help(bot_username, payload="help"):
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("⌯ ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ⌯", url=f"https://t.me/{bot_username}?start={payload}", style=PRIMARY),
    ]])


def privacy(url):
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("⌯ ᴘʀɪᴠᴀᴄʏ ᴘᴏʟɪᴄʏ 🔏 ⌯", url=url, style=PRIMARY),
    ]])


# ------------------------------------------------------------
#  HELP MENU BUTTONS
# ------------------------------------------------------------
def help_menu():
    rows = [
        [InlineKeyboardButton(label, callback_data=f"help_cat|{cat}|0", style=PRIMARY) for label, cat in row]
        for row in HELP_MENU_LAYOUT
    ]
    rows.append([
        InlineKeyboardButton("🏠 ʙᴀᴄᴋ", callback_data="back_to_start", style=DANGER),
        InlineKeyboardButton("✖ ᴄʟᴏꜱᴇ", callback_data="help_close", style=DANGER),
    ])
    return InlineKeyboardMarkup(rows)


def help_category(category, page=0):
    """Category ke saare buttons ek saath (2 per row). Neeche sirf Back + Close (red)."""
    items = HELP_CATEGORIES.get(category, ("", []))[1]
    rows = []
    for i in range(0, len(items), 2):
        rows.append([
            InlineKeyboardButton(label, callback_data=f"hm|{key}|{category}|0", style=PRIMARY)
            for label, key in items[i:i + 2]
        ])
    rows.append([
        InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help_categories", style=DANGER),
        InlineKeyboardButton("✖ ᴄʟᴏꜱᴇ", callback_data="help_close", style=DANGER),
    ])
    return InlineKeyboardMarkup(rows)


def help_back(category, page=0):
    """Kisi bhi help detail ke neeche: ek step peeche (category page) + home."""
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data=f"help_cat|{category}|{page}", style=PRIMARY),
        InlineKeyboardButton("🏠 ʜᴏᴍᴇ", callback_data="back_to_start", style=DANGER),
    ]])


# ============================================================
#  PLUGIN BUTTONS  (auto-moved from plugins — har function ek keyboard/button)
#  Function ke arguments wahi values hain jo plugin call karte waqt deta hai.
# ============================================================


# ---- edith/handlers/autolock.py --------------------------
def edith_autolock__build_ampm_keyboard_1(action, hour):
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("☀️ ᴀᴍ", callback_data=f"al_ap_{action}_{hour}_AM", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton("🌙 ᴘᴍ", callback_data=f"al_ap_{action}_{hour}_PM", style=ButtonStyle.PRIMARY),
        ]
    ])

def edith_autolock__build_hour_keyboard_1(action, n):
    return InlineKeyboardButton(str(n), callback_data=f"al_h_{action}_{n}")


# ---- edith/handlers/captcha.py ---------------------------
def edith_captcha__captcha_join_handler_1(opt, user):
    return InlineKeyboardButton(str(opt), callback_data=f"cap:{user.id}:{opt}")


# ---- edith/handlers/cleaner.py ---------------------------
def edith_cleaner__setcleandelay_cmd_1():
    return InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("1 ᴍɪɴ",  callback_data="cleantime_60", style=ButtonStyle.PRIMARY),
                    InlineKeyboardButton("5 ᴍɪɴ",  callback_data="cleantime_300", style=ButtonStyle.PRIMARY),
                    InlineKeyboardButton("15 ᴍɪɴ", callback_data="cleantime_900", style=ButtonStyle.PRIMARY),
                ],
                [
                    InlineKeyboardButton("1 ʜʀ",  callback_data="cleantime_3600", style=ButtonStyle.PRIMARY),
                    InlineKeyboardButton("6 ʜʀ",  callback_data="cleantime_21600", style=ButtonStyle.PRIMARY),
                    InlineKeyboardButton("24 ʜʀ", callback_data="cleantime_86400", style=ButtonStyle.PRIMARY),
                ],
            ])


# ---- edith/handlers/couple.py ----------------------------
def edith_couple__couple_cmd_1(BOT_USERNAME):
    return InlineKeyboardMarkup([[
                        InlineKeyboardButton(
                            text="Aᴅᴅ ᴍᴇ 🌋",
                            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                        )
                    ]])

def edith_couple__couple_cmd_2(BOT_USERNAME):
    return InlineKeyboardMarkup([[
                            InlineKeyboardButton(
                                text="Aᴅᴅ ᴍᴇ🌋",
                                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                            )
                        ]])


# ---- edith/handlers/fsub.py ------------------------------
def edith_fsub__enforce_fsub_1(link, title):
    return InlineKeyboardButton(f"📢 ᴊᴏɪɴ: {title}", url=link, style=ButtonStyle.PRIMARY)


# ---- edith/handlers/group_commands.py --------------------
def edith_group_commands___biolink_settings_markup_1(chat_id):
    return InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🚫 ʙᴀɴ", callback_data=f"bc_action_{chat_id}_ban", style=ButtonStyle.DANGER),
                InlineKeyboardButton("🔇 ᴍᴜᴛᴇ", callback_data=f"bc_action_{chat_id}_mute", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton("🗑 ᴅᴇʟᴇᴛᴇ", callback_data=f"bc_action_{chat_id}_delete", style=ButtonStyle.PRIMARY),
            ]
        ])

def edith_group_commands__bioconfig_action_callback_1(action, chat_id):
    return InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("3️⃣ 3 ᴡᴀʀɴꜱ", callback_data=f"bc_warn_{chat_id}_{action}_3", style=ButtonStyle.PRIMARY),
                    InlineKeyboardButton("4️⃣ 4 ᴡᴀʀɴꜱ", callback_data=f"bc_warn_{chat_id}_{action}_4", style=ButtonStyle.PRIMARY),
                    InlineKeyboardButton("5️⃣ 5 ᴡᴀʀɴꜱ", callback_data=f"bc_warn_{chat_id}_{action}_5", style=ButtonStyle.PRIMARY),
                ],
                [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data=f"bc_back_{chat_id}", style=ButtonStyle.PRIMARY)]
            ])


# ---- edith/handlers/joinrequest.py -----------------------
def edith_joinrequest__handle_join_request_1(chat_id, user):
    return InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "ᴀᴘᴘʀᴏᴠᴇ",
                        callback_data=(
                            f"jr_approve:{chat_id}:{user.id}"
                        )
                    ),
                    InlineKeyboardButton(
                        "ᴅᴇᴄʟɪɴᴇ",
                        callback_data=(
                            f"jr_decline:{chat_id}:{user.id}"
                        )
                    ),
                ]
            ])


# ---- edith/handlers/welcome.py ---------------------------
def edith_welcome___build_markup_1(buttons):
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(b["text"], url=b["url"], style=ButtonStyle.PRIMARY)] for b in buttons]
    )

def edith_welcome___send_panel_1(user_id):
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📄 ᴛᴇxᴛ",        callback_data=f"ws_text_{user_id}", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton("📸 ᴍᴇᴅɪᴀ",       callback_data=f"ws_media_{user_id}", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton("🔘 ʙᴜᴛᴛᴏɴꜱ", callback_data=f"ws_urlbtn_{user_id}", style=ButtonStyle.PRIMARY),
        ],
        [
            InlineKeyboardButton("🕵️ ᴘʀᴇᴠɪᴇᴡ", callback_data=f"ws_preview_{user_id}", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton("💾 ꜱᴀᴠᴇ",    callback_data=f"ws_save_{user_id}", style=ButtonStyle.PRIMARY),
        ],
        [InlineKeyboardButton("🚮 ᴄʟᴇᴀʀ ᴀʟʟ", callback_data=f"ws_clear_{user_id}", style=ButtonStyle.PRIMARY)]
    ])

def edith_welcome__welcome_toggle_1(deep_link):
    return InlineKeyboardMarkup([
                    [InlineKeyboardButton("⚙️ ꜱᴇᴛ ʏᴏᴜʀ ᴡᴇʟᴄᴏᴍᴇ", url=deep_link, style=ButtonStyle.PRIMARY)]
                ])

def edith_welcome__setwelcome_group_1(deep_link):
    return InlineKeyboardMarkup([
                [InlineKeyboardButton("ꜱᴇᴛ ʏᴏᴜʀ ᴡᴇʟᴄᴏᴍᴇ ɪɴ ᴘᴍ", url=deep_link, style=ButtonStyle.PRIMARY)]
            ])


# ---- plugins/anime.py ------------------------------------
def anime__anime_search_1(info):
    return InlineKeyboardButton("More info", url=info, style=enums.ButtonStyle.PRIMARY)

def anime__anime_search_2(trailer):
    return InlineKeyboardButton("Trailer 🎬", url=trailer, style=enums.ButtonStyle.SUCCESS)

def anime__anime_search_3(info):
    return InlineKeyboardButton("More info", url=info, style=enums.ButtonStyle.PRIMARY)


# ---- plugins/autoapprove.py ------------------------------
def autoapprove__approval_command_1():
    return InlineKeyboardMarkup(
            [[InlineKeyboardButton("Turn OFF", callback_data="approval_off")]]
        )

def autoapprove__approval_command_2():
    return InlineKeyboardMarkup(
            [[InlineKeyboardButton("Turn ON", callback_data="approval_on")]]
        )

def autoapprove__approval_cb_1():
    return InlineKeyboardMarkup(
                [[InlineKeyboardButton("Turn OFF", callback_data="approval_off")]]
            )

def autoapprove__approval_cb_2():
    return InlineKeyboardMarkup(
                [[InlineKeyboardButton("Turn ON", callback_data="approval_on")]]
            )


# ---- plugins/ban_user_or_chat.py -------------------------
def ban_user_or_chat__grp_bd_1(SUPPORT_CHAT):
    return InlineKeyboardButton("Support", url=f"https://t.me/{SUPPORT_CHAT}")

def ban_user_or_chat__disable_chat_1(SUPPORT_CHAT):
    return InlineKeyboardButton("Support", url=f"https://t.me/{SUPPORT_CHAT}")


# ---- plugins/billiard.py ---------------------------------
def billiard__billiard_cmd_1(billiard_url):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🎱 Mainkan Biliar",
                    web_app=WebAppInfo(url=billiard_url),
                    style=enums.ButtonStyle.SUCCESS,
                )
            ]
        ]
    )


# ---- plugins/bypass.py -----------------------------------
def bypass__bypass_1(result):
    return InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Open Link", url=result, style=enums.ButtonStyle.PRIMARY),
                        InlineKeyboardButton("Raw Link", url=f"{result}/raw", style=enums.ButtonStyle.SUCCESS),
                    ]
                ]
            )


# ---- plugins/copy_forward.py -----------------------------
def copy_forward__copymsg_1(BOT_USERNAME):
    return InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="💬 Chat Aku Yahh",
                                url=f"https://t.me/{BOT_USERNAME}",
                            )
                        ]
                    ]
                )

def copy_forward__forwardmsg_1(BOT_USERNAME):
    return InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="💬 Chat Aku Yahh",
                                url=f"https://t.me/{BOT_USERNAME}",
                            )
                        ]
                    ]
                )


# ---- plugins/dev.py --------------------------------------
def dev__log_file_1(ctx, strings):
    return InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                strings("cl_btn"),
                                f"close#{ctx.from_user.id}",
                            )
                        ]
                    ]
                )

def dev__shell_cmd_1(ctx, self, strings):
    return InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text=strings("cl_btn"),
                                callback_data=f"close#{ctx.from_user.id if ctx.from_user else self.me.id}",
                            )
                        ]
                    ]
                )

def dev__shell_cmd_2(ctx, self, strings):
    return InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=strings("cl_btn"),
                            callback_data=f"close#{ctx.from_user.id if ctx.from_user else self.me.id}",
                        )
                    ]
                ]
            )

def dev__cmd_eval_1(ctx, self, strings):
    return InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text=strings("cl_btn"),
                                callback_data=f"close#{ctx.from_user.id if ctx.from_user else self.me.id}",
                            )
                        ]
                    ]
                )

def dev__cmd_eval_2(ctx, self, strings):
    return InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=strings("cl_btn"),
                            callback_data=f"close#{ctx.from_user.id if ctx.from_user else self.me.id}",
                        )
                    ]
                ]
            )


# ---- plugins/federation.py -------------------------------
def federation__del_fed_1(fed_id):
    return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚠️ Delete Federation ⚠️",
                        callback_data=f"rmfed_{fed_id}",
                    )
                ],
                [InlineKeyboardButton("Cancel", callback_data="rmfed_cancel")],
            ]
        )

def federation__fedtransfer_1(fed_id, user_id):
    return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚠️ Transfer Federation ⚠️",
                        callback_data=f"trfed_{user_id}|{fed_id}",
                    )
                ],
                [InlineKeyboardButton("Cancel", callback_data="trfed_cancel")],
            ]
        )

def federation__fed_owner_help_1():
    return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="hm|federation_help|moderation|0"
                    ),
                ]
            ]
        )


# ---- plugins/filters.py ----------------------------------
def filters__stop_all_1():
    return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("YES, DO IT", callback_data="stop_yes"),
                    InlineKeyboardButton("Cancel", callback_data="stop_no"),
                ]
            ]
        )


# ---- plugins/fun.py --------------------------------------
def fun__batu_gunting_kertas_1(game_id):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🪨 Batu", callback_data=f"rps:{game_id}:batu", style=enums.ButtonStyle.PRIMARY),
                InlineKeyboardButton("✂️ Gunting", callback_data=f"rps:{game_id}:gunting", style=enums.ButtonStyle.PRIMARY),
                InlineKeyboardButton("📄 Kertas", callback_data=f"rps:{game_id}:kertas", style=enums.ButtonStyle.PRIMARY),
            ],
            [InlineKeyboardButton("❌ Batalkan", callback_data=f"rps:{game_id}:stop", style=enums.ButtonStyle.DANGER)],
        ]
    )

def fun__build_tebak_angka_keyboard_1(game_id, nomor):
    return InlineKeyboardButton(str(nomor), callback_data=f"ga:{game_id}:{nomor}")

def fun__build_tebak_angka_keyboard_2(game_id):
    return InlineKeyboardButton("🛑 Berhenti", callback_data=f"ga:{game_id}:stop", style=enums.ButtonStyle.DANGER)


# ---- plugins/grup_tools.py -------------------------------
def grup_tools__leave_a_chat_1(SUPPORT_CHAT):
    return InlineKeyboardButton("Support", url=f"https://t.me/{SUPPORT_CHAT}")


# ---- plugins/imdb_search.py ------------------------------
def imdb_search___imdb_settings_keyboard_1(uid):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🎛 Edit Layout", callback_data=f"imdblayoutmenu#{uid}"),
                InlineKeyboardButton("📝 IMDb By", callback_data=f"imdby#{uid}"),
            ],
            [
                InlineKeyboardButton(
                    "🧩 Custom Layout", callback_data=f"imdbtemplatemenu#{uid}"
                ),
                InlineKeyboardButton("🚩 Language", callback_data=f"imdbsetlang#{uid}"),
            ],
            [InlineKeyboardButton("Close", callback_data=f"close#{uid}", icon_custom_emoji_id=5985346521103604145, style=enums.ButtonStyle.DANGER)],
        ]
    )

def imdb_search__imdb_choose_1(IMDB_CUSTOM_EMOJI, ctx, ranval):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🇺🇸 English",
                    callback_data=f"imdbcari#eng#{ranval}#{ctx.from_user.id}",
                    style=enums.ButtonStyle.PRIMARY,
                ),
                InlineKeyboardButton(
                    "🇮🇩 Indonesia",
                    callback_data=f"imdbcari#ind#{ranval}#{ctx.from_user.id}",
                    style=enums.ButtonStyle.PRIMARY,
                ),
            ],
            [
                InlineKeyboardButton(
                    "🚩 Set Default Language", callback_data=f"imdbset#{ctx.from_user.id}"
                )
            ],
            [
                InlineKeyboardButton(
                    "Close",
                    callback_data=f"close#{ctx.from_user.id}",
                    icon_custom_emoji_id=IMDB_CUSTOM_EMOJI["close"],
                    style=enums.ButtonStyle.DANGER,
                )
            ],
        ]
    )

def imdb_search__imdb_lang_menu_1(query):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🇺🇸 English", callback_data=f"setimdb#eng#{query.from_user.id}", style=enums.ButtonStyle.PRIMARY),
                InlineKeyboardButton("🇮🇩 Indonesia", callback_data=f"setimdb#ind#{query.from_user.id}", style=enums.ButtonStyle.PRIMARY),
            ]
        ]
    )

def imdb_search__imdb_template_menu_1(IMDB_CUSTOM_EMOJI, query):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("↩️ Back", callback_data=f"imdbset#{query.from_user.id}", style=enums.ButtonStyle.PRIMARY),
                InlineKeyboardButton(
                    "Close",
                    callback_data=f"close#{query.from_user.id}",
                    icon_custom_emoji_id=IMDB_CUSTOM_EMOJI["close"],
                    style=enums.ButtonStyle.DANGER,
                ),
            ]
        ]
    )

def imdb_search__imdb_by_menu_1(query):
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("↩️ Back", callback_data=f"imdbset#{query.from_user.id}", style=enums.ButtonStyle.PRIMARY)]
        ]
    )

def imdb_search__imdbsetlang_1(query):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "↩️ Back", callback_data=f"imdbset#{query.from_user.id}"
                )
            ]
        ]
    )

def imdb_search___build_imdb_result_1(close_btn, imdb_url):
    return InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("🎬 Open IMDB", url=imdb_url, style=enums.ButtonStyle.PRIMARY)],
                        [close_btn],
                    ]
                )

def imdb_search___build_imdb_result_2(IMDB_CUSTOM_EMOJI, uid):
    return InlineKeyboardButton(
        "Close",
        callback_data=f"close#{uid}",
        icon_custom_emoji_id=IMDB_CUSTOM_EMOJI["close"],
        style=enums.ButtonStyle.DANGER,
    )

def imdb_search___layout_keyboard_1(_layout_field_label, enabled, key, uid):
    return InlineKeyboardButton(
                _layout_field_label(key, enabled),
                callback_data=f"imdblayouttoggle#{key}#{uid}",
            )

def imdb_search___layout_keyboard_2(uid):
    return InlineKeyboardButton("🔄 Reset", callback_data=f"imdblayoutreset#{uid}", style=enums.ButtonStyle.DANGER)

def imdb_search___layout_keyboard_3(uid):
    return InlineKeyboardButton("↩️ Back", callback_data=f"imdbset#{uid}", style=enums.ButtonStyle.PRIMARY)

def imdb_search___layout_keyboard_4(IMDB_CUSTOM_EMOJI, uid):
    return InlineKeyboardButton(
                "Close",
                callback_data=f"close#{uid}",
                icon_custom_emoji_id=IMDB_CUSTOM_EMOJI["close"],
                style=enums.ButtonStyle.DANGER,
            )

def imdb_search__imdb_lang_menu_2(query):
    return InlineKeyboardButton("↩️ Back", callback_data=f"imdbset#{query.from_user.id}", style=enums.ButtonStyle.PRIMARY)

def imdb_search__imdb_lang_menu_3(query):
    return InlineKeyboardButton(
                    "🗑 Remove UserSetting", callback_data=f"setimdb#rm#{query.from_user.id}", style=enums.ButtonStyle.DANGER
                )

def imdb_search___imdb_search_1(is_id, movieID, num, uid):
    return InlineKeyboardButton(
                        text=num,
                        callback_data=f"imdbres_{'id' if is_id else 'en'}#{uid}#{movieID}",
                    )

def imdb_search___imdb_search_2(uid):
    return InlineKeyboardButton(
                        text="🚩 Language",
                        callback_data=f"imdbsetlang#{uid}",
                    )

def imdb_search___imdb_search_3(IMDB_CUSTOM_EMOJI, uid):
    return InlineKeyboardButton(
                        text="Close",
                        callback_data=f"close#{uid}",
                        icon_custom_emoji_id=IMDB_CUSTOM_EMOJI["close"],
                        style=enums.ButtonStyle.DANGER,
                    )

def imdb_search___build_imdb_result_3(imdb_url):
    return InlineKeyboardButton("🎬 Open IMDB", url=imdb_url, style=enums.ButtonStyle.PRIMARY)

def imdb_search___build_imdb_result_4(trailer_url):
    return InlineKeyboardButton("▶️ Trailer", url=trailer_url, style=enums.ButtonStyle.SUCCESS)


# ---- plugins/inline_search.py ----------------------------
def inline_search__inline_menu_1(i):
    return InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="Open Website", url=i["link"])]]
                    )

def inline_search__inline_menu_2(inline_query):
    return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Show Message 🔐", callback_data=f"prvtmsg({inline_query.id})"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Destroy☠️ this msg",
                        callback_data=f"destroy({inline_query.id})",
                    )
                ],
            ]
        )

def inline_search__inline_menu_3(link):
    return InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="Open Github Link", url=link)]]
                    )

def inline_search__inline_menu_4(link):
    return InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="Open Link", url=link)]]
                    )

def inline_search__inline_menu_5(link):
    return InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="Watch Video 📹", url=link)]]
                    )

def inline_search__inline_menu_6(imdb_id, inline_query):
    return InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Get IMDB details",
                            callback_data=f"imdbinl#{inline_query.from_user.id}#{imdb_id}",
                        )
                    ]
                ]
            )

def inline_search__imdb_inl_1(url):
    return InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "🎬 Open IMDB",
                                    url=url,
                                )
                            ]
                        ]
                    )

def inline_search__inline_menu_7():
    return InlineKeyboardButton("Stats", callback_data="stats_callback")

def inline_search__inline_menu_8():
    return InlineKeyboardButton("Go Inline!", switch_inline_query_current_chat="")

def inline_search__inline_menu_9(i):
    return InlineKeyboardButton(text=i, switch_inline_query_current_chat=i)

def inline_search__imdb_inl_2(url):
    return InlineKeyboardButton("🎬 Buka IMDB", url=url)

def inline_search__imdb_inl_3(trailer_url):
    return InlineKeyboardButton("▶️ Trailer", url=trailer_url)


# ---- plugins/json.py -------------------------------------
def json__jsonify_1(message):
    return InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="❌ Close",
                            callback_data=f"close#{message.from_user.id if message.from_user else 2024984460}",
                        )
                    ]
                ]
            )


# ---- plugins/lang_setting.py -----------------------------
def lang_setting__apply_language_change_1(strings):
    return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        strings("back_btn", context="general"),
                        callback_data="start_back",
                        style=enums.ButtonStyle.PRIMARY,
                    )
                ]
            ]
        )

def lang_setting__chlang_1(gen_langs_kb, strings):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            *gen_langs_kb(),
            [
                InlineKeyboardButton(
                    strings("back_btn", context="general"), callback_data="start_back", style=enums.ButtonStyle.PRIMARY
                )
            ],
        ]
    )

def lang_setting__gen_langs_kb_1(lang, langs):
    return InlineKeyboardButton(
                f"{lang['language_flag']} {lang['language_name']}",
                callback_data=f"setlangsel {langs[0]}",
            )

def lang_setting__gen_langs_kb_2(lang, langs):
    return InlineKeyboardButton(
                    f"{lang['language_flag']} {lang['language_name']}",
                    callback_data=f"setlangsel {langs[0]}",
                    style=enums.ButtonStyle.PRIMARY,
                )


# ---- plugins/media_extractor.py --------------------------
def media_extractor___cancel_markup_1(label, message_id, user_id):
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(label, callback_data=f"extractcancel#{message_id}#{user_id}", style=enums.ButtonStyle.DANGER)]]
    )

def media_extractor__ceksub_1(owner_id, strings):
    return InlineKeyboardButton(strings("cancel_btn"), callback_data=f"close#{owner_id}", style=enums.ButtonStyle.DANGER)

def media_extractor__ceksub_2(StreamExtractHelper, lang, mapping, owner_id, stream_name, stream_type):
    return InlineKeyboardButton(
                    f"0:{mapping}({lang}): {stream_type}: {stream_name}",
                    callback_data=StreamExtractHelper.build_callback(owner_id, lang, mapping, stream_name),
                )


# ---- plugins/mediainfo.py --------------------------------
def mediainfo___mi_cancel_markup_1(gid, label, uid):
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(label, callback_data=f"miocancel#{gid}#{uid}", style=enums.ButtonStyle.DANGER)]]
    )

def mediainfo___send_result_1(link, strings):
    return InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=strings("viweb"), url=link, style=enums.ButtonStyle.PRIMARY)]]
        )

def mediainfo___send_result_2(link, strings):
    return InlineKeyboardMarkup(
                [[InlineKeyboardButton(text=strings("viweb"), url=link, style=enums.ButtonStyle.PRIMARY)]]
            )


# ---- plugins/misc_tools.py -------------------------------
def misc_tools__calc_btn_1(uid):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("DEL", callback_data=f"calc|{uid}|DEL"),
                InlineKeyboardButton("AC", callback_data=f"calc|{uid}|AC"),
                InlineKeyboardButton("(", callback_data=f"calc|{uid}|("),
                InlineKeyboardButton(")", callback_data=f"calc|{uid}|)"),
            ],
            [
                InlineKeyboardButton("7", callback_data=f"calc|{uid}|7"),
                InlineKeyboardButton("8", callback_data=f"calc|{uid}|8"),
                InlineKeyboardButton("9", callback_data=f"calc|{uid}|9"),
                InlineKeyboardButton("÷", callback_data=f"calc|{uid}|/"),
            ],
            [
                InlineKeyboardButton("4", callback_data=f"calc|{uid}|4"),
                InlineKeyboardButton("5", callback_data=f"calc|{uid}|5"),
                InlineKeyboardButton("6", callback_data=f"calc|{uid}|6"),
                InlineKeyboardButton("×", callback_data=f"calc|{uid}|*"),
            ],
            [
                InlineKeyboardButton("1", callback_data=f"calc|{uid}|1"),
                InlineKeyboardButton("2", callback_data=f"calc|{uid}|2"),
                InlineKeyboardButton("3", callback_data=f"calc|{uid}|3"),
                InlineKeyboardButton("-", callback_data=f"calc|{uid}|-"),
            ],
            [
                InlineKeyboardButton(".", callback_data=f"calc|{uid}|."),
                InlineKeyboardButton("0", callback_data=f"calc|{uid}|0"),
                InlineKeyboardButton("=", callback_data=f"calc|{uid}|="),
                InlineKeyboardButton("+", callback_data=f"calc|{uid}|+"),
            ],
        ]
    )

def misc_tools__kbbi_search_1(parse):
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Open in Web", url=parse.get("link"))]]
    )

def misc_tools__mdl_callback_1(res):
    return InlineKeyboardMarkup(
                [[InlineKeyboardButton("🎬 Open MyDramaList", url=res["link"])]]
            )

def misc_tools__who_is_1(message):
    return InlineKeyboardButton(
                    "🔐 Close", callback_data=f"close#{message.from_user.id}"
                )

def misc_tools__who_is_2(message):
    return InlineKeyboardButton(
                    "🔐 Close", callback_data=f"close#{message.from_user.id}"
                )

def misc_tools__mdlsearch_1(idx, k, message, movie):
    return InlineKeyboardButton(
                    text=f"{idx+1}. {movie.get('title')} ({movie.get('year')})".strip(),
                    callback_data=f"mdls#{message.from_user.id}#{k.id}#{idx}",
                )


# ---- plugins/nightmodev2.py ------------------------------
def nightmodev2__module_1():
    return InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="❤️", callback_data="nightmd")]]
)


# ---- plugins/notes.py ------------------------------------
def notes__delete_all_1():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("YES, DO IT", callback_data="delete_yes"),
                InlineKeyboardButton("Cancel", callback_data="delete_no"),
            ]
        ]
    )


# ---- plugins/paste.py ------------------------------------
def paste__telegraph_paste_1(url):
    return InlineKeyboardButton("Open Link", url=url, style=enums.ButtonStyle.PRIMARY)

def paste__telegraph_paste_2(url):
    return InlineKeyboardButton(
                "Share Link", url=f"https://telegram.me/share/url?url={url}", style=enums.ButtonStyle.SUCCESS
            )

def paste__wastepaste_1(url):
    return InlineKeyboardButton("Open Link", url=url, style=enums.ButtonStyle.PRIMARY)

def paste__wastepaste_2(url):
    return InlineKeyboardButton(
                "Share Link", url=f"https://telegram.me/share/url?url={url}", style=enums.ButtonStyle.SUCCESS
            )

def paste__nekopaste_1(url):
    return InlineKeyboardButton("Open Link", url=url, style=enums.ButtonStyle.PRIMARY)

def paste__nekopaste_2(url):
    return InlineKeyboardButton(
                "Share Link", url=f"https://telegram.me/share/url?url={url}", style=enums.ButtonStyle.SUCCESS
            )

def paste__spacebinn_1(url):
    return InlineKeyboardButton("Open Link", url=url, style=enums.ButtonStyle.PRIMARY)

def paste__spacebinn_2(url):
    return InlineKeyboardButton(
                "Share Link", url=f"https://telegram.me/share/url?url={url}", style=enums.ButtonStyle.SUCCESS
            )

def paste__rentrypaste_1(url):
    return InlineKeyboardButton("Open Link", url=url, style=enums.ButtonStyle.PRIMARY)

def paste__rentrypaste_2(url):
    return InlineKeyboardButton(
                "Share Link", url=f"https://telegram.me/share/url?url={url}", style=enums.ButtonStyle.SUCCESS
            )

def paste__imgbb_upload_1(url):
    return InlineKeyboardButton("Open Link", url=url, style=enums.ButtonStyle.PRIMARY)

def paste__imgbb_upload_2(url):
    return InlineKeyboardButton(
                    "Share Link", url=f"https://telegram.me/share/url?url={url}", style=enums.ButtonStyle.SUCCESS
                )


# ---- plugins/prayer_reminder.py --------------------------
def prayer_reminder___panel_markup_1(status_text, toggle_style, user_id):
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(status_text, callback_data=f"prtoggle#{user_id}", style=toggle_style)],
            [InlineKeyboardButton("📍 Set target chat/topic ini", callback_data=f"prtarget#{user_id}", style=enums.ButtonStyle.PRIMARY)],
            [InlineKeyboardButton("🧪 Test reminder", callback_data=f"prtest#{user_id}", style=enums.ButtonStyle.SUCCESS)],
            [InlineKeyboardButton("❌ Close", callback_data=f"prclose#{user_id}", style=enums.ButtonStyle.DANGER)],
        ]
    )

def prayer_reminder___city_markup_1(user_id):
    return InlineKeyboardButton("↩️ Panel", callback_data=f"prpanel#{user_id}", style=enums.ButtonStyle.PRIMARY)

def prayer_reminder___city_markup_2(city, user_id):
    return InlineKeyboardButton(
                    city["lokasi"][:35], callback_data=f"prcity#{user_id}#{city['id']}"
                )


# ---- plugins/rules.py ------------------------------------
def rules__rules_cmd_1(BOT_USERNAME, btn_name, chat_id):
    return InlineKeyboardMarkup(
            [[InlineKeyboardButton(btn_name, url=f"https://t.me/{BOT_USERNAME}?start=btnrules_{chat_id}")]]
        )


# ---- plugins/session_generator.py ------------------------
def session_generator__module_1():
    return InlineKeyboardButton("Pyrogram", callback_data="pyrogram", style=enums.ButtonStyle.PRIMARY)

def session_generator__module_2():
    return InlineKeyboardButton("Telethon", callback_data="telethon", style=enums.ButtonStyle.PRIMARY)

def session_generator__module_3():
    return InlineKeyboardButton("Pyrogram Bot", callback_data="pyrogram_bot", style=enums.ButtonStyle.PRIMARY)

def session_generator__module_4():
    return InlineKeyboardButton("Telethon Bot", callback_data="telethon_bot", style=enums.ButtonStyle.PRIMARY)

def session_generator__module_5():
    return InlineKeyboardButton(text="🙄 Generate Session 🙄", callback_data="genstring", style=enums.ButtonStyle.PRIMARY)


# ---- plugins/sosmed_tools.py -----------------------------
def sosmed_tools__upload_1(text):
    return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📥 Download 📥", url=f"{text['data']['file']['url']['full']}"
                    )
                ]
            ]
        )


# ---- plugins/stickers.py ---------------------------------
def stickers__kang_sticker_1(self, strings):
    return InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    strings("click_me"),
                                    url=f"https://t.me/{self.me.username}?start",
                                )
                            ]
                        ]
                    )

def stickers__kang_sticker_2(packname, strings):
    return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=strings("viewpack"),
                        url=f"https://t.me/addstickers/{packname}",
                    )
                ]
            ]
        )


# ---- plugins/ubot_plugin.py ------------------------------
def ubot_plugin__mentioned_1(cid, message):
    return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="💬 Lihat Pesan",
                        url=f"https://t.me/c/{str(cid)[4:]}/{message.id}",
                    )
                ]
            ]
        )


# ---- plugins/web_scraper.py ------------------------------
def web_scraper__build_web_domain_menu_1(key, uid):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "👁 View", callback_data=f"webdomainview#{key}#{uid}", style=enums.ButtonStyle.PRIMARY
                ),
                InlineKeyboardButton(
                    "✏️ Edit", callback_data=f"webdomainedit#{key}#{uid}", style=enums.ButtonStyle.SUCCESS
                ),
            ],
            [InlineKeyboardButton("↩️ Back", callback_data=f"webdomainback#{uid}", style=enums.ButtonStyle.PRIMARY)],
            [InlineKeyboardButton("❌ Close", callback_data=f"close#{uid}", style=enums.ButtonStyle.DANGER)],
        ]
    )

def web_scraper__build_web_buttons_1(key, uid):
    return InlineKeyboardButton(key, callback_data=f"webdomain#{key}#{uid}")

def web_scraper__build_web_buttons_2(uid):
    return InlineKeyboardButton("❌ Close", callback_data=f"close#{uid}", style=enums.ButtonStyle.DANGER)


# ---- plugins/ytdl_plugins.py -----------------------------
def ytdl_plugins__ytsearch_1(results, search_key, strings):
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(f"1/{len(results)}", callback_data=f"ytdl_scroll|{search_key}|0")],
            [InlineKeyboardButton(strings("dl_btn"), callback_data=f"yt_gen|{search_key}|0", style=enums.ButtonStyle.SUCCESS)],
        ]
    )

def ytdl_plugins__ytdl_download_callback_1(job_id):
    return InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data=f"yt_cancel|{job_id}", style=enums.ButtonStyle.DANGER)]])

def ytdl_plugins__ytdl_scroll_callback_1(page, scroll_btn, search_key, strings):
    return InlineKeyboardMarkup(scroll_btn + [[InlineKeyboardButton(strings("dl_btn"), callback_data=f"yt_gen|{search_key}|{page}", style=enums.ButtonStyle.SUCCESS)]])

def ytdl_plugins__ytdl_scroll_callback_2(page, results, search_key):
    return InlineKeyboardButton(f"{page + 1}/{len(results)}", callback_data=f"ytdl_scroll|{search_key}|{page}")

def ytdl_plugins__quality_markup_1(cache_key):
    return InlineKeyboardButton("🎧 Audio AAC", callback_data=f"yt_audio|{cache_key}", style=enums.ButtonStyle.SUCCESS)

def ytdl_plugins__ytdl_pick_step_1(cache_key):
    return InlineKeyboardButton("⬅️ Back", callback_data=f"yt_back|{cache_key}", style=enums.ButtonStyle.PRIMARY)

def ytdl_plugins__ytdl_scroll_callback_3(page, search_key, strings):
    return InlineKeyboardButton(strings("back"), callback_data=f"ytdl_scroll|{search_key}|{page - 1}", style=enums.ButtonStyle.PRIMARY)

def ytdl_plugins__ytdl_scroll_callback_4(page, search_key):
    return InlineKeyboardButton("Next", callback_data=f"ytdl_scroll|{search_key}|{page + 1}", style=enums.ButtonStyle.PRIMARY)

def ytdl_plugins__quality_markup_2(cache_key, label, res):
    return InlineKeyboardButton(label, callback_data=f"yt_res|{cache_key}|{res}")

def ytdl_plugins__ytdl_pick_step_2(cache_key):
    return InlineKeyboardButton("⬅️ Back", callback_data=f"yt_back|{cache_key}", style=enums.ButtonStyle.PRIMARY)

def ytdl_plugins__ytdl_pick_step_3(cache_key, label, opt):
    return InlineKeyboardButton(label, callback_data=f"yt_dl|{cache_key}|a|{opt['bitrate']}")

def ytdl_plugins__ytdl_pick_step_4(cache_key, idx, label, res):
    return InlineKeyboardButton(label, callback_data=f"yt_dl|{cache_key}|v|{res}|{idx}")

