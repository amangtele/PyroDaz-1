# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")

API_HASH = getenv("API_HASH")
API_ID = int(getenv("API_ID", ""))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283, -1001434137371]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
OPENAI_API = getenv("OPENAI_API")
BOT_TOKEN = getenv("BOT_TOKEN", "5658697942:AAFnHC5lOfX11L8_6mLeatHa6AFfo6gnJWA")
ID_OWNER = getenv("ID_OWNER", "2056203142")
GIT_TOKEN = getenv("GIT_TOKEN", "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")
BOT_VER = "1.2.2@main"
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or None)
BRANCH = getenv("BRANCH", "main")
CHANNEL = getenv("CHANNEL", "About_db")
DB_URL = getenv("DATABASE_URL", "")
GROUP = getenv("GROUP", "SharingUserbot")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
CMD_HANDLER = getenv("CMD_HANDLER", ".")
REPO_URL = getenv("REPO_URL", "https://github.com/FadRepo/PyroDaz")
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
