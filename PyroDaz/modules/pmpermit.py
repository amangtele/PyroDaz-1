# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram import Client, enums, filters
from pyrogram.types import Message
from sqlalchemy.exc import IntegrityError

import PyroDaz.helpers.SQL.globals as sq
from config import CMD_HANDLER as cmd
from PyroDaz import TEMP_SETTINGS
from PyroDaz.helpers.basic import *
from PyroDaz.helpers.SQL.pm_permit_sql import approve, dissprove, is_approved
from PyroDaz.helpers.tools import eod
from PyroDaz.utils import *

PM_AUTO_BAN = sq.gvarstatus("PM_AUTO_BAN") or "True"


DEF_UNAPPROVED_MSG = (
    "**\\\#PM_SECURITY!//**\n\n"
    "`Hi this is guard private messages.`"
    "` Don't spam or I will block you.`"
    "` Wait untill my owner wake up and reply your pm.`"
)


@Client.on_message(
    ~filters.me & filters.private & ~filters.bot & filters.incoming, group=69
)
async def incomingpm(client: Client, message: Message):
    if sq.gvarstatus("PM_AUTO_BAN") and sq.gvarstatus("PM_AUTO_BAN") == "False":
        message.continue_propagation()
    else:
        if message.chat.id != 777000:
            PM_LIMIT = sq.gvarstatus("PM_LIMIT") or 5
            getmsg = sq.gvarstatus("unapproved_msg")
            if getmsg is not None:
                UNAPPROVED_MSG = getmsg
            else:
                UNAPPROVED_MSG = DEF_UNAPPROVED_MSG
            apprv = is_approved(message.chat.id)
            if not apprv and message.text != UNAPPROVED_MSG:
                if message.chat.id in TEMP_SETTINGS["PM_LAST_MSG"]:
                    prevmsg = TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id]
                    if message.text != prevmsg:
                        async for message in client.search_messages(
                            message.chat.id,
                            from_user="me",
                            limit=10,
                            query=UNAPPROVED_MSG,
                        ):
                            await message.delete()
                        if TEMP_SETTINGS["PM_COUNT"][message.chat.id] < (
                            int(PM_LIMIT) - 1
                        ):
                            ret = await message.reply_text(UNAPPROVED_MSG)
                            TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id] = ret.text
                else:
                    ret = await message.reply_text(UNAPPROVED_MSG)
                    if ret.text:
                        TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id] = ret.text
                if message.chat.id not in TEMP_SETTINGS["PM_COUNT"]:
                    TEMP_SETTINGS["PM_COUNT"][message.chat.id] = 1
                else:
                    TEMP_SETTINGS["PM_COUNT"][message.chat.id] = (
                        TEMP_SETTINGS["PM_COUNT"][message.chat.id] + 1
                    )
                if TEMP_SETTINGS["PM_COUNT"][message.chat.id] > (int(PM_LIMIT) - 1):
                    await message.reply("`Blocked! Because you spamming.`")
                    try:
                        del TEMP_SETTINGS["PM_COUNT"][message.chat.id]
                        del TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id]
                    except BaseException:
                        pass
                    await client.block_user(message.chat.id)
    message.continue_propagation()


@Client.on_message(filters.command(["ok", "a", "approve"], cmd) & filters.me)
async def approvepm(client: Client, message: Message):
    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            await message.edit("`Can't approve yourself.`")
            return
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        uid = replied_user.id
    else:
        aname = message.chat
        if not aname.type == enums.ChatType.PRIVATE:
            return await eod(message, "`Reply someone messages to approve PM.`", time=8)
        name0 = aname.first_name
        uid = aname.id
    try:
        approve(uid)
        getmsg = sq.gvarstatus("unapproved_msg")
        if getmsg is not None:
            UNAPPROVED_MSG = getmsg
        else:
            UNAPPROVED_MSG = DEF_UNAPPROVED_MSG
        async for kk in client.search_messages(
            uid,
            from_user="me",
            limit=10,
            query=UNAPPROVED_MSG,
        ):
            await kk.delete()
        await eod(
            message, f"**Approved message from** [{name0}](tg://user?id={uid})!", time=6
        )
    except IntegrityError:
        await eod(
            message,
            f"[{name0}](tg://user?id={uid}) maybe has been approved to PM.",
            time=6,
        )
        return


@Client.on_message(filters.command(["dis", "nopm", "disapprove"], cmd) & filters.me)
async def disapprovepm(client: Client, message: Message):
    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            await message.edit("`You can't disapprove yourself.`")
            return
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        uid = replied_user.id
    else:
        aname = message.chat
        if not aname.type == enums.ChatType.PRIVATE:
            return await eod(
                message, "`Reply someone messages to dissaprove PM.`", time=7
            )

        name0 = aname.first_name
        uid = aname.id
    dissprove(uid)
    await eod(
        message,
        f"**Message from** [{name0}](tg://user?id={uid}) **is declined, please don't spam!**",
    )


@Client.on_message(filters.command("pmlimit", cmd) & filters.me)
async def setpm_limit(client: Client, message: Message):
    if sq.gvarstatus("PM_AUTO_BAN") and sq.gvarstatus("PM_AUTO_BAN") == "False":
        return await eod(
            message,
            f"Your PM Security is off. Use `{prefix}pmpermit on` to enable it first.",
            time=13,
        )
    input_str = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if not input_str:
        return await eod(message, "**Give me a count for PM_LIMIT.**", time=7)
    if input_str and not input_str.isnumeric():
        return await eod(message, "**Give me a count for PM_LIMIT.**", time=6)
    sq.addgvar("PM_LIMIT", input_str)
    await eod(message, f"**Set PM limit to** `{input_str}`")


@Client.on_message(filters.command(["pmpermit", "pmban"], cmd) & filters.me)
async def pmpermit_toggle(client: Client, m: Message):
    if len(m.command) != 2:
        return await m.edit("Give me a status, {on} | {off}")
    status = m.text.split(None, 1)[1]
    if status == "On" or status == "true" or status == "on" or status == "ON":
        if sq.gvarstatus("PM_AUTO_BAN") and sq.gvarstatus("PM_AUTO_BAN") == "True":
            return await eod(m, "✖️ **Your PM Security is already enabled!**")
        k = status.replace(status, "True")
        sq.addgvar("PM_AUTO_BAN", k)
        ok = await m.edit("`Processing...`")
        await ok.edit(f"✅ **PM Security Enabled.**")
    elif status == "False" or status == "false" or status == "off" or status == "OFF":
        if sq.gvarstatus("PM_AUTO_BAN") and sq.gvarstatus("PM_AUTO_BAN") == "False":
            return await eod(m, "✖️ **Your PM Security is already disabled!**")
        k = status.replace(status, "False")
        sq.addgvar("PM_AUTO_BAN", k)
        ok = await m.edit("`Processing...`")
        await ok.edit(f"✅ **PM Security Disabled.**")
    else:
        await eod(m, "👀 What do you mean. I only know `ON` or `OFF` only")


@Client.on_message(filters.command("setpmpermit", cmd) & filters.me)
async def setpmpermit(client: Client, message: Message):
    """Set your own Unapproved message"""
    if sq.gvarstatus("PM_AUTO_BAN") and sq.gvarstatus("PM_AUTO_BAN") == "False":
        return await eod(
            message,
            f"Your PM Security is off. Use `{prefix}pmpermit on` to enable it first.",
            time=15,
        )
    custom_message = sq.gvarstatus("unapproved_msg")
    r = message.reply_to_message
    if custom_message is not None:
        sq.delgvar("unapproved_msg")
    if not r:
        return await eod(message, "**Reply to a text to set pm message.**")
    msg = r.text
    sq.addgvar("unapproved_msg", msg)
    await eod(message, "**Messages has been saved successfully to PM.**")


@Client.on_message(filters.command("getpmpermit", cmd) & filters.me)
async def get_pmermit(client: Client, message: Message):
    if sq.gvarstatus("PM_AUTO_BAN") and sq.gvarstatus("PM_AUTO_BAN") == "False":
        return await message.edit(
            f"Your PM Security is off. Use `{prefix}pmpermit on` to enable it first."
        )
    ok = await message.edit("`Processing...`")
    custom_message = sq.gvarstatus("unapproved_msg")
    if custom_message is not None:
        await ok.edit("**Messages on PMPERMIT now is:**" f"\n\n{custom_message}")
    else:
        await ok.edit(
            "**You don't have setting PMPERMIT,**\n"
            f"**Now is on old default PM:**\n\n{DEF_UNAPPROVED_MSG}"
        )


@Client.on_message(filters.command("resetpmpermit", cmd) & filters.me)
async def reset_pmpermit(client: Client, message: Message):
    if sq.gvarstatus("PM_AUTO_BAN") and sq.gvarstatus("PM_AUTO_BAN") == "False":
        return await message.edit(
            f"Your PM Security is off. Use `{prefix}pmpermit on` to enable it first."
        )
    ok = await message.edit("`Processing...`")
    custom_message = sq.gvarstatus("unapproved_msg")
    if custom_message is None:
        await ok.edit("**Your PM messages set to DEFAULT**")
    else:
        sq.delgvar("unapproved_msg")
        await ok.edit("**Done set PM messages set to DEFAULT**")
add_command_help(
    "pmpermit",
    [
        [
            f"ok atau {cmd}setuju",
            "Menerima pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm",
        ],
        [
            f"tolak atau {cmd}nopm",
            "Menolak pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm",
        ],
        [
            "pmlimit <angka>",
            "Untuk mengcustom pesan limit auto block pesan",
        ],
        [
            "setpmpermit <balas ke pesan>",
            "Untuk mengcustom pesan PMPERMIT untuk orang yang pesannya belum diterima.",
        ],
        [
            "getpmpermit",
            "Untuk melihat pesan PMPERMIT.",
        ],
        [
            "resetpmpermit",
            "Untuk Mereset Pesan PMPERMIT menjadi DEFAULT",
        ],
        [
            "pmpermit on/off",
            "Untuk mengaktifkan atau menonaktifkan PMPERMIT",
        ],
    ],
)
