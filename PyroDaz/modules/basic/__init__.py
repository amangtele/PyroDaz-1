import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "PyroDaz"])

async def join(client):
    try:
        await client.join_chat("about_db")
    except BaseException:
        pass
