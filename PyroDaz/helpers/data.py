from pyrogram.types import InlineKeyboardButton
from config import CMD_HANDLER


class Data:

    text_help_menu = (
        f"**Command List & Help**\n**ㅤ Prefixes:** {CMD_HANDLER}"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("ᴏᴘᴇɴ", callback_data="reopen")]]
