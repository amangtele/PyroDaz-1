#
# Copyright (C) 2023 by amangtele@Github, < https://github.com/amangtele >.
#
# This file is part of < https://github.com/amangtele > memek,
# and is released under the "GNU v3.0 License Agreement".
# Please see < hhttps://github.com/amangtele/blob/main/LICENSE >
#
# All rights reserved.


from pyrogram import Client, filters
from pyrogram.types import Message

from PyroDaz.utils.misc import restart
from PyroDaz.helpers.SQL.globals import addgvar
from PyroDaz.helpers.tools import eod, get_arg
from config import CMD_HANDLER as cmd

from .help import add_command_help

@Client.on_message(
    filters.command(["setprefix", "sethandler", "setcmd"], cmd) & filters.me
)
async def setprefix_(c: Client, m: Message):
    handle = get_arg(m)
    if not handle:
        return await eod(
            m,
            f"Set you prefix use {cmd}setprefix [new_prefix]\n • Current prefix is {cmd}",
            time=30,
        )
    else:
        addgvar("PREFIX", cmd)
        await m.edit(f"☑️ Prefix change to [{cmd}]")
        restart()

