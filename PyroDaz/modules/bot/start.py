from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from PyroDaz import app
from PyroDaz.modules.bot import callback


START = """
❏ Haii {}
╭╼┅━━━━━╍━━━━━┅━━━━━━━┅╾
├▹ {} Adalah Ubot Pyrogram Telegram
├▹ Yang Dibuat Untuk Bersenang-Senang
├▹ Dan Memiliki Modul Yg Bisa Anda Gunakan
├▹ Bisa Membuat Ubot Sampai Dengan 10 String 
╰╼┅━━━━━╍━━━━━┅━━━━━━━┅╾
❏ © py-Ayiin v{}
"""


@tgbot.on_message(filters.private & filters.incoming &
                  filters.command("start"))
async def start(bot, msg):
    user = await bot.get_me()
    mention = user.mention
    buttons = [
        [
            InlineKeyboardButton(
                "☞︎︎︎ Cʀᴇᴀᴛᴇ Uʙᴏᴛ ☜︎︎︎", callback_data="multi_client")
        ],
    ]
    await bot.send_message(
        msg.chat.id,
        START.format(msg.from_user.mention, mention, __version__),
        reply_markup=InlineKeyboardMarkup(buttons)
    )



@callback("multi_client")
async def added_to_group_msg(_, cq):
    button = [
        [
            InlineKeyboardButton(
                text="SESSION 1",
                callback_data=f"session_1",
            ),
            InlineKeyboardButton(
                text="SESSION 2",
                callback_data=f"session_2",
            )
        ],
        [
            InlineKeyboardButton(
                text="SESSION 3",
                callback_data=f"session_3",
            ),
            InlineKeyboardButton(
                text="SESSION 4",
                callback_data=f"session_4",
            )
        ],
        [
            InlineKeyboardButton(
                text="SESSION 5",
                callback_data=f"session_5",
            ),
        ],
    ]
    await cq.message.reply(
        text="String Session Mana Yang Ingin Anda Buat ???",
        reply_markup=InlineKeyboardMarkup(button),
    )
