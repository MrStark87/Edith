<div align="center">

# Edith

**A fast, modular Telegram group manager and productivity toolkit.**

Moderation · Security · Utilities · Media · AI · Mini App Games

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-Kurigram-2CA5E0?logo=telegram&logoColor=white)
![Database](https://img.shields.io/badge/Database-MongoDB-47A248?logo=mongodb&logoColor=white)
![License](https://img.shields.io/badge/License-GPL--2.0-blue)

*Created and maintained by **Mister Stark***

</div>

---

## Overview

Edith keeps Telegram communities safe, organised and engaging. It combines a complete
group-management suite with a large toolbox of media, search and AI utilities, all behind a
single, consistent help system with table-based command references.

- **One bot, full coverage** — moderation, anti-spam, welcome flows, federations, notes, filters, downloaders, AI and games.
- **Clean help system** — every module documented in a command / description table, navigated with inline buttons that edit a single message in place.
- **Easy to customise** — all help text, all inline buttons and all configuration live in three dedicated files.
- **Production-minded** — asynchronous throughout, MongoDB persistence, isolated databases for each subsystem and per-module fault isolation.

---

## Features

| Category | Highlights |
|---|---|
| **Moderation** | Ban, kick, mute, temporary actions, silent and delete-variants, warn system with configurable limit and action, promotions and staff roles, federations, blacklists (users and words), command and media auto-delete |
| **Security** | Captcha verification, anti-raid, anti-flood, anti-link, anti-sticker, bio-link detection, locks and scheduled auto-lock, force-subscribe, join-request handling, night mode, approved users |
| **Utility** | Welcome system with PM setup panel, notes, filters, rules, tag-all, forwarding, AFK, karma, message cleaner, long-message handling |
| **Groups** | Group identity tools (name, bio, photo), invite links, group info |
| **AI & Tools** | Grok-powered `/ai` and `/ask`, OCR, paste services, web screenshots, code tester, currency, session generator, inline mode |
| **Media** | Social downloader (Instagram, TikTok, Facebook, Twitter/X, YouTube), media tools and extractor, stickers, quote stickers, movie scrapers, prayer reminder |
| **Fun & Games** | Pool and Space Shooter Telegram Mini Apps, couple of the day, fun commands |
| **Owner** | Broadcast, global bans, chat blacklist, logs, restart and system statistics |

Send `/help` to the bot in private chat to browse every module.

---

## Quick Start

### Requirements

- Python **3.12**
- A MongoDB database (MongoDB Atlas free tier works)
- Telegram **API ID / API Hash** from [my.telegram.org](https://my.telegram.org) and a **bot token** from [@BotFather](https://t.me/BotFather)
- `ffmpeg` and `git` installed on the host

### Installation

```bash
sudo apt update && sudo apt install -y python3-venv python3-full git ffmpeg

git clone <your-repository-url> Edith
cd Edith

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

> Install dependencies **only** through `requirements.txt` inside the virtual environment.
> The `pykeyboard` package is vendored in this repository on purpose — installing the PyPI
> version replaces the Kurigram framework files and breaks the bot.

### Configuration

All settings are hardcoded in a single file — no `.env` required. Open `misskaty/vars.py` and fill in the values:

| Variable | Description |
|---|---|
| `API_ID`, `API_HASH` | Telegram application credentials |
| `BOT_TOKEN` | Bot token from BotFather |
| `DATABASE_URI` | MongoDB connection string |
| `DATABASE_NAME`, `EDITH_DB_NAME` | Database names (main toolkit and group manager) |
| `OWNER_ID` | Telegram user ID of the owner |
| `SUDO` | List of additional sudo user IDs |
| `LOG_CHANNEL` | Channel ID used for logs (`-100…`) |
| `SUPPORT_GROUP`, `UPDATE_CHANNEL` | Links shown on the start menu |
| `START_IMAGE`, `PRIVACY_IMAGE`, `PRIVACY_POLICY_URL` | Start / privacy assets |
| `GROK_API_KEY`, `GROK_MODEL` | Grok credentials for `/ai` and `/ask` |
| `BILLIARD_GAME_URL`, `SHOOTER_GAME_URL` | HTTPS links of the Mini App games |
| `TZ` | Time zone, for example `Asia/Kolkata` |

### Run

```bash
python -m misskaty
```

---

## Deployment

### Background process

```bash
nohup ./venv/bin/python -m misskaty > bot.log 2>&1 &
```

### systemd service (recommended for servers)

Create `/etc/systemd/system/edith.service`:

```ini
[Unit]
Description=Edith Telegram Bot
After=network-online.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/Edith
ExecStart=/home/ubuntu/Edith/venv/bin/python -m misskaty
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now edith
sudo journalctl -u edith -f
```

---

## Mini App Games

Edith can launch HTML5 games as Telegram Mini Apps.

| Command | Action |
|---|---|
| `/game` | Games menu with a button for each game |
| `/billiard`, `/pool` | 8-Ball Pool |
| `/shoot` | Space Shooter |

Host each game on an HTTPS domain and set `BILLIARD_GAME_URL` and `SHOOTER_GAME_URL` in `misskaty/vars.py`. A game with an empty link is hidden from the menu.

---

## Customisation

Everything user-facing is separated from the logic:

| What you want to change | File |
|---|---|
| Any help text or command description | `misskaty/ui/help_texts.py` |
| Any inline button, label, colour or help menu layout | `misskaty/ui/buttons.py` |
| Credentials and settings | `misskaty/vars.py` |

Help entries are plain data — each module is a list of `(command, description)` rows. The same data produces the table
view in the help menu and the formatted text used in command replies.

---

## Project Structure

```text
Edith/
├── misskaty/
│   ├── vars.py              # configuration
│   ├── ui/
│   │   ├── help_texts.py    # all help content
│   │   └── buttons.py       # all inline keyboards
│   ├── plugins/             # feature modules (start/help, AI, games, tools, media, ...)
│   │   └── edith_suite.py   # loads the group-manager suite
│   ├── edith/               # group-manager suite (moderation, security, welcome, ...)
│   │   ├── db.py
│   │   └── handlers/
│   ├── core/                # client, bootstrap, decorators, web server
│   └── helper/              # shared helpers
├── database/                # data access layer
├── locales/                 # translations
├── pykeyboard/              # vendored keyboard helper
└── requirements.txt
```

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| `externally-managed-environment` on Ubuntu | Use a virtual environment as shown above |
| `RequestedPeerUser` / `InputRichMessage` import errors | The wrong Pyrogram build is installed. Recreate the virtual environment and install only from `requirements.txt` |
| `/ai` or `/ask` reports a missing key | Set `GROK_API_KEY` and `GROK_MODEL` in `misskaty/vars.py` |
| `/game` says links are not set | Set `BILLIARD_GAME_URL` and/or `SHOOTER_GAME_URL` |

---

## Credits

- **Edith** — design, integration and maintenance by **Mister Stark**.
- Built on top of the open-source **MissKatyPyro** project by Yasir Aris M, and the **Kurigram** Telegram framework.

## License

Distributed under the **GNU General Public License v2.0**. See [`LICENSE`](LICENSE) for details.
