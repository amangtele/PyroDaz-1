import importlib
from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from PyroDaz.modules import ALL_MODULES
from PyroDaz import LOGGER, LOOP, aiosession, app, bots, ids
from PyroDaz.modules.basic import join

MSG_ON = """
✨ **Congratulations, Now your Premium userbot is active!**
➠ **Userbot Version -** `{}`
➠ **Type** `{}alive` untuk Mengecheck Bot
"""


async def main():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("PyroDaz.modules" + all_module)
        print(f"Successfully Imported {all_module} ")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            print(f"User Mode {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("logs").info("Userbot Is Actived!")
    install()
    LOOP.run_until_complete(main())
