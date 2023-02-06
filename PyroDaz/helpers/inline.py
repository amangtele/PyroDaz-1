from math import ceil
from traceback import format_exc

from pyrogram.errors import MessageNotModified
from pyrogram.types import (
    InlineKeyboardButton,
)

from PyroDaz import ids as list_users

looters = None


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 5
    number_of_cols = 3
    global looters
    looters = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        InlineKeyboardButton(
            text="{}".format(x),
            callback_data=f"ub_modul_{x}",
        )
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [   
            (
                InlineKeyboardButton(
                    text="⫷", callback_data=f"{prefix}_prev({modulo_page})"),
                InlineKeyboardButton(
                    text="⫸", callback_data=f"{prefix}_next({modulo_page})"),
            )
        ]
    return pairs

