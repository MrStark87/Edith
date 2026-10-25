# ============================================================
#  EDITH — HELP TEXTS  (sirf yahi file edit karo)
#  Owner : Mister Stark
#
#  - Har help text Edith ke format me hai: header box + <blockquote expandable>.
#  - Saare texts parse_mode=enums.ParseMode.HTML ke saath bheje jaate hain.
#  - Text badalna ho to bas yaha string edit karo — kisi plugin me haath nahi lagana.
#  - Naya module add karna ho: yaha text likho, HELP_TEXTS me key daalo,
#    aur buttons.py ke HELP_CATEGORIES me ek (label, key) jodo.
# ============================================================

# ------------------------------------------------------------
#  START / HELP MENU TEXTS   ({...} wale fields code bharta hai)
# ------------------------------------------------------------
START_TEXT = """
<blockquote expandable><b>💐 ɢʀєєᴛɪηɢꜱ {user} 🥀</b></blockquote>
<b>💮 ʏσᴜ ᴧʀє ᴜꜱɪηɢ <a href='{bot_link}'>𝐄ᴅɪᴛʜ 𝐒ᴇᴄᴜʀɪᴛʏ 𝐁ᴏᴛ 🤖</a> — ʏσᴜʀ ɢʀσᴜᴘ ᴧᴅᴠᴧηᴄєᴅ ꜱєᴄᴜʀɪᴛʏ ᴧηᴅ ᴍᴧηᴧɢєᴍєηᴛ ʙσᴛ.</b>

<b>➣ <u>ɪ ᴄᴧη ʜєʟᴘ ʏσᴜ ᴡɪᴛʜ:</u></b>
<blockquote expandable><b>⦸ 𝐀ɴᴛɪ 𝐀ʙᴜꜱᴇ & 𝐀ɴᴛɪ 𝐑ᴀɪᴅ.</b>

<b>♧ 𝐁ɪᴏʟɪɴᴋ 𝐏ʀᴏᴛᴇᴄᴛɪᴏɴ & 𝐋ɪɴᴋ 𝐏ʀᴏᴛᴇᴄᴛɪᴏɴ.</b>

<b>♙ 𝐆ʀᴏᴜᴘ 𝐋ᴏᴄᴋ, 𝐁ᴜʟᴋ 𝐏ᴜʀɢɪɴɢ, 𝐂ᴏᴍᴍᴀɴᴅꜱ 𝐃ᴇʟᴇᴛᴇ.</b></blockquote>

<b>⇩</b> ɴєєᴅ ʜєʟᴘ? ᴜꜱє ᴛʜє ʙᴜᴛᴛᴏɴ ʙєʟᴏᴡ σʀ ꜱєηᴅ /help
"""

GROUP_START_TEXT = """<emoji id=5440431182602842059>👋</emoji> <b>𝐇ᴇʏ! 𝐈'ᴍ 𝐄ᴅɪᴛʜ</b>
<b>❍ 𝐘ᴏᴜʀ ꜱᴍᴧʀᴛ ɢʀσᴜᴘ ᴍᴧηᴧɢєʀ ʙσᴛ.</b>

<b>➻ 𝐀ᴅᴅ ᴍє ᴛσ ʏσᴜʀ ɢʀσᴜᴘ ᴧηᴅ ᴋєєᴘ ɪᴛ ꜱᴧꜰє</b> <emoji id=5017108172138087141>🛡️</emoji>"""

GROUP_HELP_TEXT = """<emoji id=5231102735817918643>👇</emoji> <b>𝐂ʟɪᴄᴋ ση ᴛʜє ʙᴜᴛᴛση ʙєʟσᴡ ᴛσ ɢєᴛ ᴍʏ ʜєʟᴘ ᴍєηᴜ ɪη ʏσᴜʀ 𝐏𝐌.</b>"""

PRIVACY_TEXT = """<emoji id=5956561916573782596>📄</emoji> <b>𝐏ʀɪᴠᴀᴄʏ 𝐏ᴏʟɪᴄʏ ꜰσʀ - <a href="{bot_link}">𝐄𝐃𝐈𝐓𝐇</a></b>
<b>𝐘ᴏᴜʀ ᴘʀɪᴠᴧᴄʏ ɪꜱ ɪᴍᴘσʀᴛᴧηᴛ ᴛσ ᴜꜱ. 𝐓ᴏ ʟєᴧʀη ᴍσʀє ᴧʙσᴜᴛ ʜσᴡ ᴡє ᴄσʟʟєᴄᴛ, ᴜꜱє, ᴧηᴅ ᴘʀσᴛєᴄᴛ ʏσᴜʀ ᴅᴧᴛᴧ, ᴘʟєᴧꜱє ʀєᴠɪєᴡ σᴜʀ <a href="{privacy_url}">𝐏ʀɪᴠᴀᴄʏ 𝐏ᴏʟɪᴄʏ</a>.</b>
<b>𝐈ꜰ ʏσᴜ ʜᴧᴠє ᴧηʏ ǫᴜєꜱᴛɪσηꜱ σʀ ᴄσηᴄєʀηꜱ, ꜰєєʟ ꜰʀєє ᴛσ ʀєᴧᴄʜ σᴜᴛ ᴛσ σᴜʀ <a href="{support_url}">ꜱᴜᴘᴘσʀᴛ ᴛєᴧᴍ</a>.</b>"""

HELP_MENU_TEXT = """<b>❖ 𝐂ʜᴏᴏꜱᴇ ᴧ ᴍσᴅᴜʟє ᴛσ ɢєᴛ ɪᴛꜱ ᴄσᴍᴍᴧηᴅꜱ ᴧηᴅ ᴜꜱᴧɢє</b>

<b>➥ 𝐀ꜱᴋ ʏσᴜʀ ᴅσᴜʙᴛꜱ ᴧᴛ <a href='{support_url}'>ꜱᴜᴘᴘσʀᴛ ᴄʜᴧᴛ</a></b>
<b>𝐀ʟʟ ᴄσᴍᴍᴧηᴅꜱ ᴄᴧη ʙє ᴜꜱєᴅ ᴡɪᴛʜ</b> : <code>/</code>"""

HELP_CATEGORY_TEXT = """<b>❖ {category} ᴄσᴍᴍᴧηᴅꜱ</b>

<b>➥ 𝐀ꜱᴋ ʏσᴜʀ ᴅσᴜʙᴛꜱ ᴧᴛ <a href='{support_url}'>ꜱᴜᴘᴘσʀᴛ ᴄʜᴧᴛ</a></b>"""

HELP_NOT_FOUND_TEXT = """⚠️ <b>𝐇ᴇʟᴘ ησᴛ ꜰσᴜηᴅ.</b>"""


# ------------------------------------------------------------
#  HELP DOCS  (yaha edit karo — table me bhi aur Edith box format me bhi yahi se banta hai)
#
#  "key": {
#      "emoji": "...", "title": "...",
#      "sections": [ ("Section name", [("/command args", "description"), ...]), ... ],
#  }
#  Notes ke liye left me "•" ya "Label" likho. Left column /command ho to table me <code> me aata hai.
# ------------------------------------------------------------
HELP_DOCS = {
    'moderation': {
        "emoji": '🔮',
        "title": 'Moderation',
        "sections": [
            ('Commands', [
                ('/kick', 'Remove a user from the group'),
                ('/ban', 'Ban a user permanently'),
                ('/unban', 'Lift a ban'),
                ('/mute', 'Stop a user from sending messages'),
                ('/unmute', 'Allow a muted user to talk again'),
                ('/tmute <time>', 'Temporary mute (1m – 24h)'),
                ('/tban <time>', 'Temporary ban (1m – 24h)'),
                ('/dkick', 'Kick the replied user and delete their message'),
                ('/skick', 'Silent kick, the command message is deleted'),
                ('/dmute', 'Mute the replied user and delete their message'),
                ('/dban', 'Ban the replied user and delete their message'),
                ('/dwarn', 'Warn the replied user and delete their message'),
            ]),
        ],
    },
    'warns_help': {
        "emoji": '⚠️',
        "title": 'Warn System',
        "sections": [
            ('Commands', [
                ('/warn [reason]', 'Warn a user'),
                ('/dwarn', 'Warn a user and delete their message'),
                ('/warns', 'View warn history of a user'),
                ('/unwarn', 'Remove one warn'),
                ('/resetwarns', 'Clear all warns of a user'),
                ('/setwarnlimit [1-10]', 'Set how many warns trigger the action'),
                ('/setwarnaction mute|kick|ban', 'Set what happens when the limit is reached'),
            ]),
            ('Defaults', [
                ('Warn limit', '3 warns'),
                ('Warn action', 'Mute'),
                ('After action', 'Warns are reset'),
                ('/warns', 'Shows the last 5 reasons'),
            ]),
        ],
    },
    'blackuser_help': {
        "emoji": '🚷',
        "title": 'Blacklisted Users',
        "sections": [
            ('Commands', [
                ('/blackuser <userid>', 'Add a user to the blacklist'),
                ('/rmblackuser <userid>', 'Remove a user from the blacklist'),
                ('/blacklistusers', 'Show all blacklisted users'),
            ]),
            ('Notes', [
                ('Effect', 'All messages of blacklisted users are deleted automatically (text, media, stickers, gifs)'),
                ('Admins', 'Admins are never affected'),
                ('Access', 'Only admins can configure this'),
            ]),
        ],
    },
    'abuse_help': {
        "emoji": '🤬',
        "title": 'Abuse Detection',
        "sections": [
            ('Commands', [
                ('/noabuse on', 'Enable abuse detection'),
                ('/noabuse off', 'Disable abuse detection'),
            ]),
            ('Notes', [
                ('Action', 'Abusive message is deleted instantly'),
                ('Warning', 'A warning is sent and removed after 5 seconds'),
                ('Admins', 'Admins are not affected'),
            ]),
        ],
    },
    'cmd_help': {
        "emoji": '🗑️',
        "title": 'Command Deleter',
        "sections": [
            ('Commands', [
                ('/cmd on', 'Auto delete command messages'),
                ('/cmd off', 'Stop deleting command messages'),
            ]),
            ('How it works', [
                ('Trigger', 'Messages starting with /  !  or .'),
                ('Action', 'The message is deleted instantly'),
                ('Admins', 'Admin commands are deleted too'),
                ('Access', 'Only admins can configure this'),
            ]),
        ],
    },
    'mediadelete_help': {
        "emoji": '🎬',
        "title": 'Media Auto-Delete',
        "sections": [
            ('Commands', [
                ('/mediadelete on', 'Enable media auto-delete'),
                ('/mediadelete off', 'Disable media auto-delete'),
                ('/setmediadelay <time>', 'Set the delay before deletion'),
            ]),
            ('Time format', [
                ('5m', '5 minutes'),
                ('1h', '1 hour'),
                ('12h', '12 hours'),
                ('24h', '24 hours'),
                ('Range', '1m to 24h (default 5m)'),
            ]),
            ('Applies to', [
                ('Media types', 'Photos, videos, stickers, gifs, animations, locations and polls'),
                ('Access', 'Only admins can configure this'),
            ]),
        ],
    },
    'admin_tag_help': {
        "emoji": '🆘',
        "title": '@Admin System',
        "sections": [
            ('How to use', [
                ('@admin', 'Type it in the group to tag all admins at once'),
                ('@admins', 'Same as @admin'),
            ]),
            ('Admin commands', [
                ('/admintag on', 'Enable @admin tagging'),
                ('/admintag off', 'Disable @admin tagging'),
            ]),
            ('Notes', [
                ('Who can use', 'All group members'),
                ('Bots', 'Bots are not tagged'),
                ('Default', 'On'),
            ]),
        ],
    },
    'promote_help': {
        "emoji": '👮',
        "title": 'Promote System',
        "sections": [
            ('Commands', [
                ('/cofounder', 'Make a co-founder (can set cofounders, mods, helpers, ban users, all admin permissions)'),
                ('/admin or /promote {name}', 'Make an admin (delete msgs, pin, invite, manage group, custom title)'),
                ('/mod', 'Make a moderator (ban, kick, mute, info; cannot delete messages)'),
                ('/fullpromote {name}', 'Make a full admin with all permissions and custom title'),
                ('/demote', 'Remove admin rights'),
                ('/staff', 'Show all staff members'),
            ]),
        ],
    },
    'longmsg_help': {
        "emoji": '📄',
        "title": 'Long Message',
        "sections": [
            ('Commands', [
                ('/echo <text>', 'Reply with the same text; long text becomes a Telegraph link'),
                ('/setlongmode off', 'No action on long messages'),
                ('/setlongmode manual', 'Delete the message and warn the user'),
                ('/setlongmode automatic', 'Delete and create a Telegraph link (default)'),
                ('/setlonglimit <50-2000>', 'Set the character limit (default 800)'),
            ]),
            ('Notes', [
                ('Access', 'Only admins can set mode and limit'),
            ]),
        ],
    },
    'hashtag_help': {
        "emoji": '#️⃣',
        "title": 'Hashtag Filter',
        "sections": [
            ('Commands', [
                ('/nohashtags on', 'Delete hashtag messages'),
                ('/nohashtags off', 'Allow hashtag messages'),
            ]),
            ('Detection examples', [
                ('#join', 'Any word starting with #'),
                ('#promotion', 'Deleted automatically'),
                ('Access', 'Only admins can configure this'),
            ]),
        ],
    },
    'locks': {
        "emoji": '🔐',
        "title": 'Locks System',
        "sections": [
            ('Commands', [
                ('/lock <type>', 'Enable a lock'),
                ('/unlock <type>', 'Disable a lock'),
                ('/locks', 'Show active locks'),
                ('/lockall', 'Lock everything'),
                ('/unlockall', 'Unlock everything'),
            ]),
            ('Available types', [
                ('Content', 'url, text, sticker, media, music, files, emoji'),
                ('Other', 'username, forward, edit'),
            ]),
        ],
    },
    'autolock_help': {
        "emoji": '🕐',
        "title": 'Auto Lock',
        "sections": [
            ('Commands', [
                ('/autolock on', 'Set the daily lock time'),
                ('/autolock off', 'Set the daily unlock time'),
                ('/autolockstatus', 'Show the current schedule'),
                ('/autolockclear', 'Remove the schedule'),
            ]),
            ('How it works', [
                ('Setup', 'Pick an hour (1-12), then am/pm'),
                ('Lock time', 'The whole group is locked automatically every day'),
                ('Unlock time', 'The group reopens automatically (if not set, admins unlock manually)'),
                ('Timezone', 'Times follow the server clock, not your local timezone'),
                ('Access', 'Only admins can configure this'),
            ]),
        ],
    },
    'captcha_help': {
        "emoji": '🔡',
        "title": 'Captcha System',
        "sections": [
            ('Commands', [
                ('/captcha on', 'Enable captcha'),
                ('/captcha off', 'Disable captcha'),
                ('/captchatime <seconds>', 'Set the answer timeout'),
            ]),
            ('How it works', [
                ('Join', 'New member is muted instantly'),
                ('Verify', 'Must solve a math question to get unmuted'),
                ('Fail', 'Wrong answer or timeout kicks the member'),
            ]),
        ],
    },
    'biolink': {
        "emoji": '🔗',
        "title": 'Biolink Protection',
        "sections": [
            ('Info', [
                ('•', 'Blocks users who have links in their bio.'),
            ]),
            ('Commands', [
                ('/biolink on', 'Protection on ✅'),
                ('/biolink off', 'Protection off ❌'),
                ('/bioconfig', 'Configure action'),
            ]),
            ('Notes', [
                ('•', 'Bio link detected → message deleted'),
                ('•', 'Admins are not affected'),
                ('•', 'Bot needs delete messages permission'),
            ]),
        ],
    },
    'anti_link_help': {
        "emoji": '🔗',
        "title": 'Anti Link System',
        "sections": [
            ('Main commands', [
                ('/nolink on', 'Block all links ❌'),
                ('/nolink off', 'Allow all links ✅'),
            ]),
            ('Whitelist / blacklist', [
                ('/allowlink {url}', 'Allow specific link'),
                ('/rmallowlink {url}', 'Remove from allowed list'),
                ('/blocklink {url}', 'Block specific link'),
                ('/rmblocklink {url}', 'Remove from blocked list'),
                ('/allowedlinks', 'List allowed links'),
                ('/blockedlinks', 'List blocked links'),
            ]),
            ('Warn system', [
                ('/linkwarn on', 'Warn + action on limit'),
                ('/linkwarn off', 'Only delete + notify'),
            ]),
            ('Notes', [
                ('•', 'Admins are not affected'),
                ('•', 'Tg links match specific usernames!'),
            ]),
        ],
    },
    'fsub_help': {
        "emoji": '🪠',
        "title": 'Force-Subscribe',
        "sections": [
            ('Commands', [
                ('/addfsub @channel or -100xxxx', 'Require members to join this channel'),
                ('/removefsub @channel or -100xxxx', 'Remove a required channel'),
                ('/fsublist', 'List required channels'),
            ]),
            ('Notes', [
                ('Effect', 'Users who have not joined the channels cannot send messages'),
                ('Bot', 'Bot must be admin in the channel'),
            ]),
        ],
    },
    'cleaner_help': {
        "emoji": '🧹',
        "title": 'Message Cleaner',
        "sections": [
            ('Commands', [
                ('/cleaner on', 'Enable auto-delete'),
                ('/cleaner off', 'Disable auto-delete'),
                ('/setcleandelay <time>', 'Set the deletion delay (5m, 1h, 12h, 24h)'),
                ('/cleanstatus', 'Show current settings'),
            ]),
            ('Notes', [
                ('Time range', '1m to 24h (default 5m)'),
                ('Applies to', 'All text and media of regular users'),
                ('Admins', 'Admin messages are never deleted'),
                ('Commands', 'Command messages auto-clean after 8 seconds'),
                ('Access', 'Only admins can configure this'),
            ]),
        ],
    },
    'phone_help': {
        "emoji": '📞',
        "title": 'Phone Protection',
        "sections": [
            ('Commands', [
                ('/nophone on', 'Delete messages containing phone numbers'),
                ('/nophone off', 'Allow phone numbers'),
            ]),
            ('Detection examples', [
                ('+91 9876543210', 'International format'),
                ('+1-234-567-8900', 'With dashes'),
                ('919876543210', 'Plain digits'),
                ('Access', 'Only admins can configure this'),
            ]),
        ],
    },
    'anti_sticker_help': {
        "emoji": '🎭',
        "title": 'Anti Sticker',
        "sections": [
            ('Commands', [
                ('/banpack', 'Reply to a sticker to ban its whole pack'),
                ('/unbanpack <packname>', 'Unban a pack'),
                ('/bannedpacks', 'List all banned packs'),
                ('/clearbanpacks', 'Clear all banned packs'),
                ('/antisticker on', 'Block every sticker'),
                ('/antisticker off', 'Allow all stickers'),
            ]),
            ('Notes', [
                ('Admins', 'Admins are not affected'),
            ]),
        ],
    },
    'zombie_help': {
        "emoji": '🧟',
        "title": 'Remove Deleted Accounts',
        "sections": [
            ('Commands', [
                ('/zombie', 'Scan the group and remove all deleted accounts instantly'),
            ]),
            ('Notes', [
                ('Bot', 'Bot must be admin with ban permission'),
                ('Access', 'Only admins can use this command'),
                ('Effect', 'All deleted Telegram accounts are removed immediately'),
            ]),
        ],
    },
    'ghost_help': {
        "emoji": '👻',
        "title": 'Ghost Mode',
        "sections": [
            ('Commands', [
                ('/ghostmode on', 'Enable ghost mode ✅'),
                ('/ghostmode off', 'Disable ghost mode ❌'),
            ]),
            ('What gets deleted', [
                ('•', 'User joined the group'),
                ('•', 'User left the group'),
                ('•', 'User was removed'),
                ('•', 'Group title changed'),
                ('•', 'Group photo changed'),
                ('•', 'Pinned message notifications'),
                ('•', 'Video chat started / ended'),
                ('•', '👮 Only admins can configure this.'),
            ]),
        ],
    },
    'joinrequest_help': {
        "emoji": '⛩️',
        "title": 'Auto Accept Join Requests',
        "sections": [
            ('Commands', [
                ('/acceptall on', 'Auto accept join requests'),
                ('/acceptall off', 'Stop auto accepting'),
                ('/notification on', 'Send join request notifications'),
                ('/notification off', 'Do not send join request notifications'),
            ]),
            ('Notes', [
                ('When off', 'Bot posts a join request notification with approve / decline buttons for admins'),
                ('Notification off', 'No join request message is sent in the group'),
                ('Bot', 'Bot must be admin with approval rights'),
                ('Access', 'Only admins can use these commands'),
            ]),
        ],
    },
    'antiraid_help': {
        "emoji": '🛡️',
        "title": 'Anti Raid',
        "sections": [
            ('Commands', [
                ('/antiraid on', 'Auto mute new members'),
                ('/antiraid off', 'Disable auto mute'),
                ('/raiddelay <time>', 'Set the mute duration'),
            ]),
            ('Time format', [
                ('30s / 5m / 1h', 'Seconds, minutes, hours'),
                ('0', 'Permanent (an admin must unmute)'),
                ('Example', '/raiddelay 30s mutes new members for 30 seconds'),
                ('Access', 'Only admins can configure this'),
            ]),
        ],
    },
    'antiflood_help': {
        "emoji": '🌊',
        "title": 'Anti Flood',
        "sections": [
            ('Commands', [
                ('/antiflood on', 'Enable anti flood'),
                ('/antiflood off', 'Disable anti flood'),
                ('/setflood <number>', 'Messages allowed per 10 seconds'),
                ('/floodaction <mute/kick/ban/warn>', 'Action to take'),
                ('/floodtime <time>', 'Mute / ban duration'),
                ('/floodmode <strict/normal>', 'Detection mode'),
                ('/flood', 'View current settings'),
                ('/floodwhitelist <add/remove/list>', 'Exempt users'),
            ]),
            ('Modes', [
                ('normal', 'Any rapid messages count'),
                ('strict', 'Only repeated / same messages count'),
                ('Access', 'Only admins can configure this'),
            ]),
        ],
    },
    'disable_help': {
        "emoji": '🚫',
        "title": 'Disable Commands',
        "sections": [
            ('Commands', [
                ('/disable <command>', 'Disable a command for members'),
                ('/enable <command>', 'Re-enable a command'),
                ('/disabled', 'List disabled commands'),
            ]),
            ('Notes', [
                ('Effect', 'Regular members cannot use disabled commands; admins are never affected'),
                ('Disableable', 'rules, notes, id, chatinfo, info, report, fsublist, filters, blacklist, ai, ask'),
                ('Access', 'Only admins can configure this'),
            ]),
        ],
    },
    'fancy_text_help': {
        "emoji": '🔡',
        "title": 'Fancy Text Protection',
        "sections": [
            ('Commands', [
                ('/fancytext on', 'Allow fancy text (no action)'),
                ('/fancytext off', 'Block fancy text (delete + warn)'),
            ]),
            ('How it works', [
                ('On', 'Users can use fancy fonts freely'),
                ('Off', 'Fancy text is deleted and the user gets a warn'),
                ('Warn limit', 'When the limit is reached the warn action runs automatically'),
            ]),
        ],
    },
    'approve_help': {
        "emoji": '🕊',
        "title": 'Approve System',
        "sections": [
            ('Commands', [
                ('/free or /approve', 'Approve a user (reply, @user or ID)'),
                ('/unfree or /unapprove', 'Remove approval from a user'),
                ('/approved', 'List all approved users'),
            ]),
            ('Notes', [
                ('Effect', 'Approved users are ignored by every automated bot restriction'),
                ('Access', 'Only admins can approve / unapprove'),
            ]),
        ],
    },
    'greetings': {
        "emoji": '👋',
        "title": 'Welcome System',
        "sections": [
            ('Commands', [
                ('/welcome on', 'Enable welcome message'),
                ('/welcome off', 'Disable welcome message'),
                ('/setwelcome', 'Open the setup panel in PM (text, media, buttons)'),
                ('/resetwelcome', 'Reset to the default welcome'),
                ('/previewwelcome', 'Preview the current welcome'),
            ]),
            ('Placeholders', [
                ('{id}', 'User id'),
                ('{name}', 'First name'),
                ('{surname}', 'Last name'),
                ('{namesurname}', 'Full name'),
                ('{mention}', 'Clickable mention'),
                ('{username}', '@username'),
                ('{groupname}', 'Group name'),
            ]),
            ('Notes', [
                ('Formatting', 'HTML formatting and URL buttons are supported'),
            ]),
        ],
    },
    'utility_help': {
        "emoji": '⚙️',
        "title": 'Utility',
        "sections": [
            ('Commands', [
                ('/chatinfo', 'Get group details, id & member count'),
                ('/id', 'Get your id or reply to get user id'),
                ('/info', 'Get detailed user information & bio'),
                ('/ping', 'Check bot response speed'),
                ('/pin, /unpin', 'Reply to pin/unpin a message'),
                ('/pin silent', 'Pin without notification'),
                ('/del, /purge', 'Delete messages, from replied msg to now'),
                ('/purgeme', 'Delete your own recent messages'),
                ('/cleanservice on/off', 'Enable, disable auto delete for join/leave messages'),
                ('/calc <expr>', 'Built-in calculator for quick math'),
                ('/carbon <text>', 'Convert code or text into carbon image'),
            ]),
        ],
    },
    'tagall_help': {
        "emoji": '🔖',
        "title": 'Tag All',
        "sections": [
            ('Commands', [
                ('/tagall', 'Tag all members'),
                ('/tagall {message}', 'Tag with custom message'),
                ('/stoptag', 'Stop tagging'),
            ]),
            ('Notes', [
                ('•', 'Admin only'),
                ('•', '1 emoji = 1 person mention'),
                ('•', '5 people per message'),
                ('•', 'Bots & deleted accounts skipped'),
            ]),
        ],
    },
    'forward_help': {
        "emoji": '↩️',
        "title": 'Forward Protection',
        "sections": [
            ('Commands', [
                ('/forwarding on', 'Allow forwards ✅'),
                ('/forwarding off', 'Block forwards ❌'),
            ]),
            ('How it works', [
                ('On', 'All forwards allowed'),
                ('Off', 'Forwarded msg deleted + warn'),
                ('•', 'Warn limit reached → ban/kick/mute'),
            ]),
        ],
    },
    'groupinfo_help': {
        "emoji": '👥',
        "title": 'Group Identity',
        "sections": [
            ('Commands', [
                ('/setname {text}', 'Set / change the group name'),
                ('/setbio {text}', 'Set / change the group description'),
                ('/groupinfo', 'Show group id, owner and member stats'),
                ('/setdp', 'Reply to an image to set it as group photo (aliases: /setpfp, /setimage)'),
                ('/link', 'Generate a new invite link (aliases: /givelink, /invitelink)'),
            ]),
            ('Notes', [
                ('Access', 'Admin only, group only'),
                ('Bot rights', "'Change group info' and 'Invite users'"),
            ]),
        ],
    },
    'linkinfo_help': {
        "emoji": '🔗',
        "title": 'Invite Link',
        "sections": [
            ('Commands', [
                ('/link', 'Generate a brand new invite link (aliases: /givelink, /invitelink)'),
            ]),
            ('Notes', [
                ('Access', 'Admin only, group only'),
                ('Bot rights', "'Invite users via link'"),
                ('Main link', 'Each run creates a fresh link without revoking the main one'),
            ]),
        ],
    },
    'join_help': {
        "emoji": '🎀',
        "title": 'Join/Leave Deleter',
        "sections": [
            ('Commands', [
                ('/cleanservice on', 'Enable auto delete for join/leave messages'),
                ('/cleanservice off', 'Disable auto delete for join/leave messages'),
            ]),
        ],
    },
    'admin_help': {
        "emoji": '🛠️',
        "title": 'Admin Tools',
        "sections": [
            ('Commands', [
                ('/listban', 'Ban a user from groups listed in a message'),
                ('/listunban', 'Unban a user from groups listed in a message'),
                ('/ban_ghosts', 'Ban deleted accounts'),
                ('/report | @admins | @admin', 'Report a message to admins'),
                ('/set_chat_title', 'Change the name of a group/channel'),
                ('/set_chat_photo', 'Change the pfp of a group/channel'),
                ('/set_user_title', 'Change the administrator title of an admin'),
                ('/mentionall', 'Mention all members in a group'),
            ]),
        ],
    },
    'blacklist_help': {
        "emoji": '🚫',
        "title": 'Blacklist Words',
        "sections": [
            ('Commands', [
                ('/blacklisted', 'Get all the blacklisted words in the chat.'),
                ('/blacklist [WORD|SENTENCE]', 'Blacklist a word or a sentence.'),
                ('/whitelist [WORD|SENTENCE]', 'Whitelist a word or a sentence.'),
            ]),
        ],
    },
    'federation_help': {
        "emoji": '🌐',
        "title": 'Federation',
        "sections": [
            ('Owner', [
                ('/newfed <name>', 'Create a federation'),
                ('/renamefed', 'Rename the federation'),
                ('/delfed', 'Delete the federation'),
                ('/fpromote', 'Promote a federation admin'),
                ('/fdemote', 'Demote a federation admin'),
                ('/fedtransfer', 'Transfer ownership'),
            ]),
            ('Admin', [
                ('/fban', 'Federation ban a user'),
                ('/unfban', 'Federation unban a user'),
                ('/sfban', 'Silent federation ban'),
                ('/sunfban', 'Silent federation unban'),
                ('/setfedlog', 'Set the log chat'),
                ('/unsetfedlog', 'Remove the log chat'),
                ('/fedinfo', 'Federation info'),
                ('/fedadmins', 'List federation admins'),
                ('/fedchats', 'List federation chats'),
            ]),
            ('Chat', [
                ('/joinfed', 'Join a federation'),
                ('/leavefed', 'Leave the federation'),
                ('/chatfed', "Show the chat's federation"),
                ('/fedstat', 'User federation status'),
                ('/myfeds', 'Your federations'),
            ]),
            ('About', [
                ('Purpose', 'Ban a spammer in one chat and it applies to all chats in the federation'),
            ]),
        ],
    },
    'inkick_help': {
        "emoji": '🧹',
        "title": 'Inkick',
        "sections": [
            ('Commands', [
                ('/instatus', 'View member status in group.'),
                ('/ban_ghosts', 'Remove deleted account from group.'),
            ]),
        ],
    },
    'nightmode_help': {
        "emoji": '🌙',
        "title": 'Night Mode',
        "sections": [
            ('Commands', [
                ('/nightmode -s=23:53 -e=6h', 'Lock the chat every day from 23:53 for 6 hours'),
                ('/nightmode -s=23:50 -e=120m', 'Lock the chat every day from 23:50 for 120 minutes'),
                ('/nightmode -d', 'Disable night mode'),
            ]),
            ('Flags', [
                ('-s', 'Start time (24 hour format)'),
                ('-e', 'Duration (hours / minutes)'),
                ('-d', 'Disable'),
            ]),
        ],
    },
    'autoapprove_help': {
        "emoji": '✅',
        "title": 'Auto Approve',
        "sections": [
            ('Commands', [
                ('/autoapprove', 'Auto accept join requests sent via your group invite link'),
            ]),
        ],
    },
    'sangmata_help': {
        "emoji": '🕵️',
        "title": 'Sangmata',
        "sections": [
            ('Commands', [
                ('/sangmata_set [on/off]', 'Enable / disable sangmata in groups'),
            ]),
            ('About', [
                ('Feature', 'Detects changes of username, first name and last name of a user'),
            ]),
        ],
    },
    'filters_help': {
        "emoji": '🤿',
        "title": 'Filters',
        "sections": [
            ('Commands', [
                ('/filters', 'List all filters'),
                ('/filter <name>', 'Save a filter (reply to a message)'),
                ('/addfilter <name>', 'Same as /filter'),
                ('/stop <name>', 'Stop a filter'),
                ('/stopfilter <name>', 'Same as /stop'),
                ('/stopall', 'Delete all filters'),
            ]),
            ('Supported types', [
                ('Media', 'Text, animation, photo, document, video, video note, audio, voice'),
                ('Multi-word', '/filter Hey_there'),
            ]),
            ('Formatting', [
                ('Text styles', '*bold* _italic_ __underline__ ~strike~ ||spoiler||'),
                ('Button', '[Open](buttonurl://https://example.com)'),
                ('Same row button', '[Two](buttonurl://https://example.com:same)'),
                ('Note button', '[Open Note](buttonurl://#notename)'),
            ]),
            ('Fillings', [
                ('User', '{first} {last} {fullname} {username} {mention} {id} {chatname}'),
                ('Options', '{rules} {rules:same} {preview} {preview:top} {nonotif} {protect} {mediaspoiler}'),
            ]),
        ],
    },
    'notes_help': {
        "emoji": '📝',
        "title": 'Notes System',
        "sections": [
            ('Commands', [
                ('/notes', 'List all notes'),
                ('/save <name>', 'Save a note (reply to a message)'),
                ('/addnote <name>', 'Same as /save'),
                ('#name', 'Get a note'),
                ('/delnote <name>', 'Delete a note'),
                ('/deleteall', 'Delete all notes'),
            ]),
            ('Supported types', [
                ('Media', 'Text, animation, photo, document, video, video note, audio, voice'),
                ('New caption', '/save name new caption'),
            ]),
            ('Formatting', [
                ('Text styles', '*bold* _italic_ __underline__ ~strike~ ||spoiler||'),
                ('Button', '[Open](buttonurl://https://example.com)'),
                ('Same row button', '[Two](buttonurl://https://example.com:same)'),
            ]),
            ('Fillings', [
                ('User', '{first} {last} {fullname} {username} {mention} {id} {chatname}'),
                ('Options', '{rules} {rules:same} {preview} {preview:top} {nonotif} {protect} {mediaspoiler}'),
            ]),
        ],
    },
    'rules_help': {
        "emoji": '📑',
        "title": 'Rules',
        "sections": [
            ('User', [
                ('/rules', 'Check the current chat rules'),
                ('/rules noformat', 'Raw rules text'),
            ]),
            ('Admin', [
                ('/setrules <text>', 'Set rules (markdown, buttons, fillings)'),
                ('/privaterules <on/off>', 'Send rules in pm'),
                ('/resetrules', 'Reset rules'),
                ('/setrulesbutton <name>', 'Button name for {rules}'),
                ('/resetrulesbutton', 'Reset button name'),
            ]),
        ],
    },
    'afk_help': {
        "emoji": '💤',
        "title": 'AFK',
        "sections": [
            ('Commands', [
                ('/afk [reason]', 'Tell others you are away from keyboard'),
                ('/afk [reply to media]', 'Go AFK with a media message'),
                ('/afkdel', 'Toggle auto delete of AFK messages (group admins, default enabled)'),
            ]),
            ('Notes', [
                ('Return', 'Type anything in the group to remove your AFK status'),
            ]),
        ],
    },
    'karma_help': {
        "emoji": '⭐',
        "title": 'Karma',
        "sections": [
            ('Commands', [
                ('/karma', 'View karma of group members'),
                ('/karma_toggle [enable/disable]', 'Enable / disable karma'),
            ]),
            ('Notes', [
                ('Give karma', 'Give reputation to other people in the group'),
            ]),
        ],
    },
    'ai_help': {
        "emoji": '🤖',
        "title": 'Edith AI',
        "sections": [
            ('Commands', [
                ('/ai <question>', 'Chat with Edith (remembers the recent chat)'),
                ('/ask <question>', 'Quick answer without memory'),
                ('/ai or /ask (reply)', 'Reply to a message to give it as context'),
            ]),
            ('Examples', [
                ('/ai What is Python?', 'Chat style question'),
                ('/ask Capital of India?', 'One-shot question'),
            ]),
        ],
    },
    'misc_help': {
        "emoji": '🧰',
        "title": 'Misc Tools',
        "sections": [
            ('Commands', [
                ('/carbon [text or reply to text or caption]', 'Make beautiful snippet code on carbon from text.'),
                ('/removebg [Reply to image]', 'Remove background from image.'),
                ('/calc', 'Simple math calculator using inline buttons.'),
                ('/kbbi [keyword]', 'Search definition on kbbi (for indonesian people)'),
                ('/sof [query]', 'Search your problem in stackoverflow.'),
                ('/google [query]', 'Search using google search.'),
                ('(/tr, /trans, /translate) [lang code]', 'Translate text using google translate.'),
                ('/tts', 'Convert text to voice.'),
                ('/imdb [query]', 'Find movie details from imdb.com (available in english and indonesia version).'),
                ('/readqr [reply to photo]', 'Read qr code from photo.'),
                ('/createqr [text]', 'Convert text to qr code.'),
                ('/anime [query]', 'Search title in myanimelist.'),
                ('/info', 'Get info user with pic and full description if user set profile picture.'),
                ('/id', 'Get simple user id.'),
            ]),
        ],
    },
    'ocr_help': {
        "emoji": '🔍',
        "title": 'Ocr',
        "sections": [
            ('Commands', [
                ('/ocr [reply to photo]', 'Read text from image'),
            ]),
        ],
    },
    'paste_help': {
        "emoji": '📋',
        "title": 'Paste',
        "sections": [
            ('Commands', [
                ('/paste [Text/Reply To Message]', 'Post text to my pastebin.'),
                ('/sbin [Text/Reply To Message]', 'Post text to spacebin.'),
                ('/neko [Text/Reply To Message]', 'Post text to nekobin.'),
                ('/tgraph [Text/Reply To Message]', 'Post text to telegraph.'),
                ('/imgbb [Images]', 'Upload image to imgbb.'),
                ('/rentry [Text/Reply To Message]', 'Post text to rentry using markdown style.'),
            ]),
        ],
    },
    'nulis_help': {
        "emoji": '✍️',
        "title": 'Nulis',
        "sections": [
            ('Commands', [
                ('/nulis [reply to msg or after cmd]', 'For those who are lazy to write'),
            ]),
        ],
    },
    'webss_help': {
        "emoji": '📸',
        "title": 'Web Screenshot',
        "sections": [
            ('Commands', [
                ('/webss [URL]', 'Take a screenshot of a webpage.'),
                ('/webss [URL] -f', 'Capture full scrollable page.'),
            ]),
        ],
    },
    'mediatool_help': {
        "emoji": '🎞️',
        "title": 'Media Tools',
        "sections": [
            ('Commands', [
                ('/genss [reply to video]', 'Generate screenshot from video. (support tg media and direct url)'),
                ('/mediainfo [link/reply to TG Video]', 'Get mediainfo from file.'),
            ]),
        ],
    },
    'mediaextract_help': {
        "emoji": '🎧',
        "title": 'Media Extractor',
        "sections": [
            ('Commands', [
                ('/extractmedia [URL]', 'Extract subtitle or audio from video using link. (not support tg file to reduce bandwith usage.)'),
                ('/converttosrt [Reply to .ass or .vtt TG File]', 'Convert from .ass or .vtt to srt'),
                ('/converttoass [Reply to .srt or .vtt TG File]', 'Convert from .srt or .vtt to srt'),
            ]),
        ],
    },
    'stickers_help': {
        "emoji": '🎭',
        "title": 'Stickers',
        "sections": [
            ('Commands', [
                ('/kang [Reply to sticker]', 'Add sticker to your pack.'),
                ('/unkang [Reply to sticker]', 'Remove sticker from your pack (only can remove sticker that added by this bot.).'),
                ('/getsticker', 'Convert sticker to png.'),
                ('/stickerid', 'View sticker id'),
            ]),
        ],
    },
    'sosmed_help': {
        "emoji": '📥',
        "title": 'Social Downloader',
        "sections": [
            ('Commands', [
                ('/igdl [link] or /instadl [link]', 'Instagram post / reel as a rich slideshow'),
                ('/tiktokdl [link] or /ttdl [link]', 'TikTok video / photo as a rich slideshow'),
                ('/fbdl [link]', 'Facebook post / reel / video as a rich slideshow'),
                ('/twitterdl [link]', 'Download video from Twitter / X'),
                ('/ytdown [url]', 'Download video / audio with yt-dlp'),
                ('/download [url or reply file]', 'Download to the server (owner only)'),
                ('/anon [reply file]', 'Upload a file to anonfiles'),
            ]),
            ('Notes', [
                ('Facebook metrics', 'Reactions / comments / shares need a facebook cookies.txt'),
            ]),
        ],
    },
    'quotly_help': {
        "emoji": '💬',
        "title": 'Quotly',
        "sections": [
            ('Commands', [
                ('/q [n]', 'Generate quote sticker from message(s)'),
                ('/qr', 'Quote with reply'),
                ('/memify [text]', 'Reply to sticker to add text'),
            ]),
        ],
    },
    'search_help': {
        "emoji": '🔎',
        "title": 'Search',
        "sections": [
            ('Commands', [
                ('/imdb [query]', 'Movie details from IMDb'),
                ('/imdbset', 'Change IMDb language / layout'),
                ('/anime [query]', 'Search myanimelist'),
                ('/ud [word]', 'Urban dictionary'),
                ('/pypi [package]', 'Search PyPI'),
                ('/ytsearch [query]', 'Search YouTube'),
            ]),
        ],
    },
    'inline_help': {
        "emoji": '⌨️',
        "title": 'Inline Mode',
        "sections": [
            ('Inline queries (type @botusername first)', [
                ('imdb [query]', 'Search movie details on imdb.com'),
                ('pypi [query]', 'Search packages on PyPI'),
                ('git [query]', 'Search on git'),
                ('google [query]', 'Search on google'),
                ('info [user id/username]', 'Check info about a user'),
            ]),
        ],
    },
    'scraper_help': {
        "emoji": '🎬',
        "title": 'Movie Scraper',
        "sections": [
            ('Commands', [
                ('/melongmovie [query]', 'Scrape melongmovie'),
                ('/lk21 [query]', 'Scrape layarkaca21'),
                ('/pahe [query]', 'Scrape pahe.li'),
                ('/terbit21 [query]', 'Scrape terbit21'),
                ('/savefilm21 [query]', 'Scrape savefilm21'),
                ('/movieku [query]', 'Scrape movieku.cc'),
                ('/kusonime [query]', 'Scrape kusonime'),
                ('/lendrive [query]', 'Scrape lendrive'),
                ('/klikxxi [query]', 'Scrape klikxxi (gomov)'),
                ('/samehadaku [query]', 'Scrape samehadaku'),
                ('/nodrakor [query]', 'Scrape nodrakor'),
                ('/nunadrama [query]', 'Scrape nunadrama'),
                ('/dutamovie [query]', 'Scrape dutamovie'),
                ('/pusatfilm [query]', 'Scrape pusatfilm21'),
                ('/oppaweb [query]', 'Scrape oppaweb'),
                ('/webdomain', 'Edit scraper domains with buttons (owner only)'),
            ]),
        ],
    },
    'prayer_help': {
        "emoji": '🕌',
        "title": 'Prayer Reminder',
        "sections": [
            ('Commands', [
                ('/prayerreminder', 'Open the settings panel'),
                ('/prayerreminder sura', 'Search a city and pick it with buttons'),
                ('/prayerreminder test', 'Send a sample reminder'),
            ]),
            ('Notes', [
                ('Storage', 'Settings are saved per chat'),
                ('Data source', 'api.myquran.com'),
            ]),
        ],
    },
    'fun_help': {
        "emoji": '🎮',
        "title": 'Fun',
        "sections": [
            ('Commands', [
                ('/q [int]', 'Generate quotly from message'),
                ('/memify [text]', 'Reply to sticker to give text on sticker.'),
                ('/react [emoji | list of emoji]', 'React to any message (sudo and owner only)'),
                ('/beri [pesan]', 'Giving false hope to someone hehehe'),
                ('/dice', 'Randomly roll the dice'),
                ('/tebakgambar', 'Play "tebak gambar" in any room chat'),
                ('/tebaklontong', 'Play "tebak lontong" in any room chat'),
                ('/tebakkata', 'Play "tebak kata" in any room chat'),
                ('/tebaktebakan', 'Play "tebak tebakan" in any room chat'),
                ('/batu', 'Main batu gunting kertas pakai tombol'),
                ('/tebakangka', 'Tebak angka 1-20 pakai callback button'),
            ]),
        ],
    },
    'games_help': {
        'emoji': '🎮',
        'title': 'Mini App Games',
        'sections': [
            ('Commands', [
                ('/game', 'Open the games menu (Pool and Space Shooter buttons)'),
                ('/billiard or /pool', 'Play 8-Ball Pool mini app'),
                ('/shoot', 'Play Space Shooter mini app'),
            ]),
            ('Setup', [
                ('BILLIARD_GAME_URL', 'Pool mini app link in misskaty/vars.py'),
                ('SHOOTER_GAME_URL', 'Space Shooter mini app link in misskaty/vars.py'),
            ]),
        ],
    },
    'couple_help': {
        "emoji": '💞',
        "title": 'Couple Of The Day',
        "sections": [
            ('Commands', [
                ('/couple', "Pick today's couple in the group"),
            ]),
        ],
    },
    'codetester_help': {
        "emoji": '💻',
        "title": 'Code Tester',
        "sections": [
            ('Commands', [
                ('!<language> <code>', 'Run code via Glot.io, for example: !python print("Hello from Edith")'),
            ]),
            ('Languages', [
                ('a - c', 'assembly, ats, bash, c, clojure, cobol, coffeescript, cpp, crystal, csharp'),
                ('d - j', 'd, elixir, elm, erlang, fsharp, go, groovy, haskell, idris, java, javascript, julia'),
                ('k - p', 'kotlin, lua, mercury, nim, nix, ocaml, perl, php, python'),
                ('r - t', 'raku, ruby, rust, scala, swift, typescript'),
            ]),
        ],
    },
    'session_help': {
        "emoji": '🔑',
        "title": 'Session Generator',
        "sections": [
            ('Commands', [
                ('/genstring', 'Generate string session using this bot. only support pyrogram v2 and telethon.'),
            ]),
        ],
    },
    'owner_help': {
        "emoji": '👑',
        "title": 'Owner Only',
        "sections": [
            ('Commands', [
                ('/run [args]', 'Run eval cmd'),
                ('/shell [args]', 'Run exec/terminal cmd'),
                ('/logs [int]', 'Check bot logs'),
                ('/download [link/reply]', 'Download file to server'),
                ('/restart', 'Update and restart bot'),
                ('/gban', 'Ban a user globally'),
                ('/ungban', 'Remove global ban'),
                ('/banuser [id]', 'Block a user from using the bot'),
                ('/unbanuser [id]', 'Unblock a user'),
                ('/disablechat [id]', 'Blacklist a group'),
                ('/enablechat [id]', 'Remove group blacklist'),
                ('/broadcast', 'Broadcast a message'),
                ('/users', 'List bot users'),
                ('/chats', 'List bot chats'),
                ('/leave [chat id]', 'Leave a chat'),
                ('/webdomain', 'Edit scraper domains'),
            ]),
        ],
    },
    'stats_help': {
        "emoji": '📊',
        "title": 'Bot Info',
        "sections": [
            ('Commands', [
                ('/stats', 'Check bot statistics'),
                ('/ping', 'Check bot latency'),
                ('/ping_dc', 'Check Telegram DC latency'),
                ('/json', 'Telegram message structure in JSON'),
                ('/privacy', 'Privacy policy'),
            ]),
        ],
    },
    'bypass_help': {
        "emoji": '🔗',
        "title": 'Bypass',
        "sections": [
            ('Commands', [
                ('/directurl [link]', 'Bypass url (deprecated)'),
            ]),
        ],
    },
    'currency_help': {
        "emoji": '💱',
        "title": 'Currency',
        "sections": [
            ('Commands', [
                ('/currency [amount] [from] [to]', 'Convert currency'),
            ]),
        ],
    },
}


# ============================================================
#  NEECHE KA CODE MAT BADLO  (docs -> table / plain text builder)
# ============================================================
import html as _html
import re as _re

# ---- font converter: plain English -> Edith font (small caps + bold capitals) ----
_SC = dict(zip("abcdefghijklmnopqrstuvwxyz", "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀꜱᴛᴜᴠᴡxʏᴢ"))
_VA = dict(_SC)
_VA.update({"a": "ᴧ", "e": "є", "n": "η", "o": "σ"})
_SKIP = _re.compile(r"[{}\[\]*_~|=/@\\#<>]|\d|://")
_TOK = _re.compile(r"(<[^>]+>|\{[^}]*\}|&[a-zA-Z]+;|\S+|\s+)")


def _word(w: str) -> str:
    title = w[0].isupper()
    out = []
    for c in w:
        if c.isascii() and c.isalpha():
            if c.isupper():
                out.append(chr(0x1D400 + ord(c) - 65))
            else:
                out.append((_SC if title else _VA)[c])
        else:
            out.append(c)
    return "".join(out)


def _fancy(text: str) -> str:
    """Commands / placeholders / links / numbers jaisa technical text as-it-is rehta hai."""
    res = []
    for tok in _TOK.findall(text):
        if tok.startswith(("<", "{", "&")) or tok.isspace() or _SKIP.search(tok):
            res.append(tok)
        else:
            res.append(_re.sub(r"[A-Za-z]+", lambda m: _word(m.group(0)), tok))
    return "".join(res)


def _esc(s: str) -> str:
    return _html.escape(s, quote=False)


def _is_cmd(s: str) -> bool:
    return s.startswith(("/", "!", "@", "#", "~", ".", "-"))


def _fe(s: str) -> str:
    return _fancy(_esc(s))


def _build_plain(doc: dict) -> str:
    """Edith box format + <blockquote expandable> (handlers aur fallback ke liye)."""
    head = "╔══════════════════╗\n   %s <b>%s</b>\n╚══════════════════╝\n" % (doc["emoji"], _fe(doc["title"]))
    body = []
    for name, rows in doc["sections"]:
        body.append("<b>❖ %s ❖</b>\n" % _fe(name))
        for left, right in rows:
            if left == "•":
                body.append("➻ <b>%s</b>" % _fe(right))
            elif _is_cmd(left):
                body.append("➻ %s%s" % (_esc(left), (" — <b>" + _fe(right) + "</b>") if right else ""))
            else:
                body.append("➻ <b>%s</b>%s" % (_fe(left), (": <b>" + _fe(right) + "</b>") if right else ""))
        body.append("")
    return head + "<blockquote expandable>" + "\n".join(body).strip("\n") + "</blockquote>"


def _build_table(doc: dict) -> str:
    """Rich message HTML table (Command | Description)."""
    tables = []
    for idx, (name, rows) in enumerate(doc["sections"]):
        cap = "%s %s" % (doc["emoji"], _fe(doc["title"])) if idx == 0 else ""
        cap = (cap + " — " if cap else "") + _fe(name) if (idx == 0 and name.lower() not in ("commands", "info")) else (cap or _fe(name))
        cmdlike = sum(1 for l, _ in rows if _is_cmd(l)) >= max(1, len(rows) // 2)
        th = (_fancy("Command"), _fancy("Description")) if cmdlike else (_fancy("Item"), _fancy("Details"))
        raw = name.lower() == "languages"  # identifiers as-is
        trs = []
        for left, right in rows:
            if left == "•":
                lcell, rcell = "•", (_esc(right) if raw else _fe(right))
            else:
                lcell = "<code>%s</code>" % _esc(left) if _is_cmd(left) else (_esc(left) if raw else _fe(left))
                rcell = (_esc(right) if raw else _fe(right)) if right else "—"
            trs.append("<tr><td>%s</td><td>%s</td></tr>" % (lcell, rcell))
        tables.append(
            "<table bordered striped>\n<caption>%s</caption>\n<tr><th>%s</th><th>%s</th></tr>\n%s\n</table>"
            % (cap, th[0], th[1], "\n".join(trs))
        )
    return "\n".join(tables)


HELP_TEXTS = {k: _build_plain(d) for k, d in HELP_DOCS.items()}   # plain (blockquote) text
HELP_TABLES = {k: _build_table(d) for k, d in HELP_DOCS.items()}  # rich-message table html

# handlers jo constants import karte hain (usage replies) — plain text
MODERATION_HELP = HELP_TEXTS["moderation"]
WARNS_HELP = HELP_TEXTS["warns_help"]
BLACKUSER_HELP_TEXT = HELP_TEXTS["blackuser_help"]
ABUSE_HELP = HELP_TEXTS["abuse_help"]
CMDDELETER_HELP_TEXT = HELP_TEXTS["cmd_help"]
MEDIADELETE_HELP_TEXT = HELP_TEXTS["mediadelete_help"]
ADMIN_TAG_HELP_TEXT = HELP_TEXTS["admin_tag_help"]
PROMOTE_HELP_TEXT = HELP_TEXTS["promote_help"]
LONGMSG_HELP_TEXT = HELP_TEXTS["longmsg_help"]
HASHTAG_HELP_TEXT = HELP_TEXTS["hashtag_help"]
LOCKS_HELP = HELP_TEXTS["locks"]
AUTOLOCK_HELP_TEXT = HELP_TEXTS["autolock_help"]
CAPTCHA_HELP_TEXT = HELP_TEXTS["captcha_help"]
BIOLINK_HELP = HELP_TEXTS["biolink"]
ANTI_LINK_HELP_TEXT = HELP_TEXTS["anti_link_help"]
FSUB_HELP = HELP_TEXTS["fsub_help"]
CLEANER_HELP_TEXT = HELP_TEXTS["cleaner_help"]
PHONE_HELP_TEXT = HELP_TEXTS["phone_help"]
ANTI_STICKER_HELP_TEXT = HELP_TEXTS["anti_sticker_help"]
ZOMBIE_HELP_TEXT = HELP_TEXTS["zombie_help"]
GHOST_HELP_TEXT = HELP_TEXTS["ghost_help"]
JOINREQUEST_HELP_TEXT = HELP_TEXTS["joinrequest_help"]
ANTIRAID_HELP_TEXT = HELP_TEXTS["antiraid_help"]
ANTIFLOOD_HELP_TEXT = HELP_TEXTS["antiflood_help"]
DISABLE_HELP_TEXT = HELP_TEXTS["disable_help"]
FANCY_TEXT_HELP_TEXT = HELP_TEXTS["fancy_text_help"]
APPROVE_HELP_TEXT = HELP_TEXTS["approve_help"]
WELCOME_HELP_TEXT = HELP_TEXTS["greetings"]
UTILITY_HELP_TEXT = HELP_TEXTS["utility_help"]
TAGALL_HELP_TEXT = HELP_TEXTS["tagall_help"]
FORWARD_HELP_TEXT = HELP_TEXTS["forward_help"]
GROUPS_HELP_TEXT = HELP_TEXTS["groupinfo_help"]
LINK_HELP_TEXT = HELP_TEXTS["linkinfo_help"]
JOINLEAVE_HELP = HELP_TEXTS["join_help"]
ADMIN_HELP = HELP_TEXTS["admin_help"]
BLACKLIST_HELP = HELP_TEXTS["blacklist_help"]
FEDERATION_HELP = HELP_TEXTS["federation_help"]
INKICK_HELP = HELP_TEXTS["inkick_help"]
NIGHTMODE_HELP = HELP_TEXTS["nightmode_help"]
AUTOAPPROVE_HELP = HELP_TEXTS["autoapprove_help"]
SANGMATA_HELP = HELP_TEXTS["sangmata_help"]
FILTERS_HELP = HELP_TEXTS["filters_help"]
NOTES_HELP = HELP_TEXTS["notes_help"]
RULES_HELP = HELP_TEXTS["rules_help"]
AFK_HELP = HELP_TEXTS["afk_help"]
KARMA_HELP = HELP_TEXTS["karma_help"]
AI_HELP = HELP_TEXTS["ai_help"]
MISC_HELP = HELP_TEXTS["misc_help"]
OCR_HELP = HELP_TEXTS["ocr_help"]
PASTE_HELP = HELP_TEXTS["paste_help"]
NULIS_HELP = HELP_TEXTS["nulis_help"]
WEBSS_HELP = HELP_TEXTS["webss_help"]
MEDIATOOL_HELP = HELP_TEXTS["mediatool_help"]
MEDIAEXTRACT_HELP = HELP_TEXTS["mediaextract_help"]
STICKERS_HELP = HELP_TEXTS["stickers_help"]
SOSMED_HELP = HELP_TEXTS["sosmed_help"]
QUOTLY_HELP = HELP_TEXTS["quotly_help"]
SEARCH_HELP = HELP_TEXTS["search_help"]
INLINE_HELP = HELP_TEXTS["inline_help"]
SCRAPER_HELP = HELP_TEXTS["scraper_help"]
PRAYER_HELP = HELP_TEXTS["prayer_help"]
FUN_HELP = HELP_TEXTS["fun_help"]
GAMES_HELP = HELP_TEXTS["games_help"]
COUPLE_HELP = HELP_TEXTS["couple_help"]
CODETESTER_HELP = HELP_TEXTS["codetester_help"]
SESSION_HELP = HELP_TEXTS["session_help"]
OWNER_HELP = HELP_TEXTS["owner_help"]
STATS_HELP = HELP_TEXTS["stats_help"]
BYPASS_HELP = HELP_TEXTS["bypass_help"]
CURRENCY_HELP = HELP_TEXTS["currency_help"]
