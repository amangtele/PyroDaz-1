import requests
import os
import json
import random
import asyncio
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as mang
from pyrogram.errors import MessageNotModified
from PyroDaz.helpers.what import *
from config import OPENAI_API
from config import CMD_HANDLER as cmd

@mang.on_message(filters.command("ask", cmd) & filters.me)
async def chatgpt(c: Client, m: Message):
    randydev = (
        m.text.split(None, 1)[1]
        if len(
            m.command,
        )
        != 1
        else None
    )
    if not randydev:
       await m.reply(f"use command {cmd} [question] to ask questions using the API.")
       return
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API}",
    }

    json_data = {
        "prompt": randydev,
        "model": "text-davinci-003",
        "temperature": 0.5,
        "max_tokens": 1024,
        "n": 1,
        "stop": None,
        "top_p": 0.3,
        "frequency_penalty": 0.5,
    }
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
        await asyncio.sleep(5)
        await c.send_message(m.chat.id, response["choices"][0]["text"], reply_to_message_id=m.id)
    except Exception:
        await c.send_message(m.chat.id, "GI ERROR BANH, BLM FIX.", reply_to_message_id=m.id)
        
        
