from asyncio import gather
from random import choice

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from PyroDaz.helpers.basic import edit_or_reply
from PyroDaz.helpers.PyroHelpers import ReplyCheck

from PyroDaz.modules.help import add_command_help


@Client.on_message(filters.command(["asupan", "ptl"], cmd) & filters.me)
async def asupan_cmd(client: Client, message: Message):
    Man = await edit_or_reply(message, "`Processing...`")
    await gather(
        Man.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "tedeasupancache", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )

@Client.on_message(filters.command(["dcowo", "cwo"], cmd) & filters.me)
async def dcowo_cmd(client: Client, message: Message):
    Man = await edit_or_reply(message, "`Processing...`")
    await gather(
        Man.delete(),
        client.send_voice(
            message.chat.id,
            choice(
                [
                    dcowo.voice.file_id
                    async for dcowo in client.search_messages(
                        "desahcowokk", filter=enums.MessagesFilter.VOICE_NOTE
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    
@Client.on_message(filters.command(["dcewe", "cwe"], cmd) & filters.me)
async def dcewe_cmd(client: Client, message: Message):
    Man = await edit_or_reply(message, "`Processing...`")
    await gather(
        Man.delete(),
        client.send_voice(
            message.chat.id,
            choice(
                [
                    dcewe.voice.file_id
                    async for dcewe in client.search_messages(
                        "desahancewek22", filter=enums.MessagesFilter.VOICE_NOTE
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    
@Client.on_message(filters.command(["vidbkp", "bkp"], cmd) & filters.me)
async def vidbkp_cmd(client: Client, message: Message):
    Man = await edit_or_reply(message, "`Processing...`")
    await gather(
        Man.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    vidbkp.video.file_id
                    async for vidbkp in client.search_messages(
                        "kacafilmid", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    
    
add_command_help(
    "asupan",
    [
        [
            f"asupan atau {cmd}ptl",
            "Download video asupan random.",
        ],
        [
            f"dcowo atau {cmd}cwo",
            "Download Voice Desah Cowo Random..",
        ],
        [
            f"dcewe atau {cmd}cwe",
            "Download Voice Desah Cewe Random.",
        ],
        [
            f"vidtik atau {cmd}tktk",
            "Download Asupan Tiktok  Random.",
        ],
        [
            f"vidbkp atau {cmd}bkp",
            " Download sensitive 18+ Random..",
        ]
    ],
)
