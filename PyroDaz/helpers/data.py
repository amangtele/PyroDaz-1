from pyrogram.types import InlineKeyboardButton
from PyroDaz.helpers.cmd import *

class Data:

    text_help_menu = (
        f"**Command List & Help**\n**ㅤ Prefixes:** {cmd}"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("ᴏᴘᴇɴ", callback_data="reopen")]]
