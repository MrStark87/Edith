# Edith

All-in-one Telegram group manager + toolbox bot. Owner: **Mister Stark**.

## Setup (Ubuntu 24 / VPS)
```bash
sudo apt install -y python3-venv python3-full git ffmpeg
cd Edith
python3 -m venv venv && source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
# misskaty/vars.py me values bharo, phir:
python -m misskaty
```
Background me: `nohup ./venv/bin/python -m misskaty > bot.log 2>&1 &`

## Edit karne ki jagah
| Kya | File |
|---|---|
| Config / keys (hardcoded) | `misskaty/vars.py` |
| Saare help texts (table + box format) | `misskaty/ui/help_texts.py` |
| Saare inline buttons / help menu | `misskaty/ui/buttons.py` |
| Start / help logic | `misskaty/plugins/start_help.py` |
| Grok AI (/ai, /ask) | `misskaty/plugins/grok_ai.py` |
| Group manager modules | `misskaty/edith/handlers/` (loaded by `plugins/edith_suite.py`) |

`pykeyboard/` repo me vendored hai (PyPI wala pyrogram ko overwrite kar deta tha) — isko install mat karna.
