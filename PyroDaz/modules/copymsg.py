# Copyright (C) 2020-2021 by Toni880@Github, < https://github.com/Toni880 >.
#
# This file is part of < https://github.com/Toni880/Prime-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Toni880/Prime-Userbot/blob/master/LICENSE >
# kenkan
# abdul
#
# All rights reserved.


import os

from pyrogram import *
from pyrogram import Client, filters
from pyrogram.errors import RPCError
from pyrogram.types import *

from PyroDaz.helpers.tools import get_arg
from PyroDaz.modules.help import add_command_help
from config import CMD_HANDLER as prefix

@Client.on_message(filters.command("copy", prefix) & filters.me)
async def nyolongnih(client, message):
    await message.edit("Let's grab the content first...")
    link = get_arg(message)
    msg_id = int(link.split("/")[-1])
    if "t.me/c/" in link:
        try:
            chat = int("-100" + str(link.split("/")[-2]))
            dia = await client.get_messages(chat, msg_id)
        except RPCError:
            await message.edit("Looks like something's wrong")
    else:
        try:
            chat = str(link.split("/")[-2])
            dia = await client.get_messages(chat, msg_id)
        except RPCError:
            await message.edit("Looks like something's wrong")
    anjing = dia.caption or None
    if dia.text:
        await dia.copy(message.chat.id)
        await message.delete()
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)
    else:
        await message.edit("Looks like something's wrong")


@Client.on_message(filters.command("copybot", prefix) & filters.me)
async def pencuri(client, message):
    dia = message.reply_to_message
    if not dia:
        await message.edit("Please reply to the media on the bot")
    anjing = dia.caption or None
    await message.edit("Ready to steal content...")
    if dia.text:
        await dia.copy(message.chat.id)
        await message.delete()
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)
    else:
        await message.edit("Looks like something's wrong")


@Client.on_message(filters.command("getmsg", prefix) & filters.me)
async def ambil(client: Client, message: Message):
    dia = message.reply_to_message
    if not dia:
        await message.edit("Looks like something's wrong")
    dia.caption or None
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(message.from_user.id, anu)
        await message.delete()
        os.remove(anu)

    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video(message.from_user.id, anu)
        await message.delete()
        os.remove(anu)

    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(message.from_user.id, anu)
        await message.delete()
        os.remove(anu)

    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(message.from_user.id, anu)
        await message.delete()
        os.remove(anu)


add_command_help(
    "copymsg",
    [
        [
            "copy <link protected channel.>",
            "Copy anything from the protected channel."],
        [   "copybot <reply message>",
            "Copy anything from the protected channel."],
        [   "getmsg <get the photo on the timer.>",
            "get the photo on the timer.",
          
        ],
    ],
)
