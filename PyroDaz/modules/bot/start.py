from PyroDaz import app
from pyrogram import filters


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
   await message.reply_text(
      "👋🏻 Halo!\n\n"
      "Dengan bot ini, Anda dapat melakukan pembayaran untuk userbot premium PyroDaz-Userbot.\n\n"
      "💭 Berikut dibawah ini perintah yang berisi petunjuk untuk melakukan pembayaran!\n"
      "/pertanyaan : untuk bertanya ke admin PyroDaz-Userbot.\n"
      "/harga : untuk melihat harga Langganan Userbot.\n"
      "/pembayaran : Untuk Melakukan Pembayaran.\n"
      "/login : untuk memulai userbot anda.\n\n"
      "MASIH DALAM PENGEMBANGAN!\n"
      "JIKA MAU ORDER HUBUNGI\n\n"
      "@amwang | @xdazher"
      
   )
