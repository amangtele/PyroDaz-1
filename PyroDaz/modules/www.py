# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import time
import asyncio
from datetime import datetime
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)

import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from config import CMD_HANDLER
from PyroDaz import StartTime
from PyroDaz import app 
from PyroDaz.helpers.basic import edit_or_reply
from PyroDaz.helpers.constants import WWW
from PyroDaz.helpers.PyroHelpers import SpeedConvert
from PyroDaz.utils.tools import get_readable_time
from PyroDaz.modules.bot.inline import get_readable_time
from PyroDaz.helpers.adminHelpers import DEVS

from .help import add_command_help

@Client.on_message(filters.command(["speed", "speedtest"], CMD_HANDLER) & filters.me)
async def speed_test(client: Client, message: Message):
    new_msg = await edit_or_reply(message, "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(filters.command("dc", CMD_HANDLER) & filters.me)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await edit_or_reply(
        message, WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc)
    )

@Client.on_message(filters.command("x3j7k", CMD_HANDLER) & filters.me)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(message, "**0% ▒▒▒▒▒▒▒▒▒▒**")
    await xx.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await xx.edit("**60% ██████▒▒▒▒**")
    await xx.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"❏ **PING!! 🚀**\n"
        f"├• **Pinger** - `%sms`\n"
        f"└• **Uptime -** `{uptime}` \n" % (duration)
    )

@Client.on_message(
    filters.command("cping", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("pingo", CMD_HANDLER) & filters.me)
async def kping(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(message, ".")
    await xx.edit("..")
    await xx.edit("...")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"🚀 **Pinger: ** `%sms`\n"
        f"⏱ **Uptime: ** `{uptime}` \n"  % (duration)
    )

@Client.on_message(filters.command("alive", CMD_HANDLER) & filters.me)
async def module_karman(client: Client, message: Message):
    cdm = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cdm) > 1:
        help_arg = " ".join(cdm[1:])
    elif not message.reply_to_message and len(cdm) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="alive")
            await asyncio.gather(
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id),
            )
        except BaseException:
            pass
