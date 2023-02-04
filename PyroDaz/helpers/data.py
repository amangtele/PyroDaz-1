from pyrogram.types import InlineKeyboardButton, WebAppInfo
from config import CMD_HANDLER

class Data:

    text_help_menu = (
        "**Command List & Help**\n**— Prefixes:** `{CMD_HANDLER}`"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("ᴏᴘᴇɴ", callback_data="reopen")]]
