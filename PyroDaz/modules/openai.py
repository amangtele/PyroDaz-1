from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as mang 

from pyrogram.errors import MessageNotModified
from PyroDaz.helpers.what import *

from PyroDaz.helpers.basic import *
from PyroDaz.helpers.adminHelpers import DEVS
from config import BLACKLIST_GCAST
from .help import add_command_help
from PyroDaz.utils.misc import *

from PyroDaz.utils.tools import *
from config import CMD_HANDLER as cmds
from config import OPENAI_API
import requests
import os
import json
import random

@mang.on_message(filters.command("cask", cmds) & filters.user(DEVS) & ~filters.me)
@mang.on_message(filters.command("ask", cmds) & filters.me)
async def openai(c, m):
    if len(m.command) == 1:
        return await m.reply(f"Ketik <code>{cmds}{m.command[0]} [question]</code> Pertanya untuk menggunakan OpenAI")
    question = m.text.split(" ", maxsplit=1)[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API}",
    }

    json_data = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 200,
        "temperature": 0,
    }
    msg = await m.reply("`Processing..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception:
        await msg.edit("**Kalo nanya yang bener dikit kek...**")

add_command_help(
    "openai",
    [
        [f"{cmds}ask [question]", "to ask questions using the API."],
    ],
)
