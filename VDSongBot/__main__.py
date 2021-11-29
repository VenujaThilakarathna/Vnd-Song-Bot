#VndBots <https://t.me/VndBotSupport>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from VDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from VDSongBot import SDbot as app
from VDSongBot import LOGGER

pm_start_text = """
👋 Hey [{}](tg://user?id={}), **I'm Song Downloader Bot**
**Now send me the song name you want to download**
     
Syntax : ```/song Faded```
      
Powerd By @VndBotSupport 🔥
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="Channel 🙋‍♀️", url="https://t.me/VndBotSupport"
                    ),
                    InlineKeyboardButton(
                        text="Dev 🔥", url="https://t.me/Venuja_Sadew"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("""
██╗░░░██╗██████╗░██████╗░░█████╗░████████╗░██████╗
██║░░░██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
╚██╗░██╔╝██║░░██║██████╦╝██║░░██║░░░██║░░░╚█████╗░
░╚████╔╝░██║░░██║██╔══██╗██║░░██║░░░██║░░░░╚═══██╗
░░╚██╔╝░░██████╔╝██████╦╝╚█████╔╝░░░██║░░░██████╔╝
░░░╚═╝░░░╚═════╝░╚═════╝░░╚════╝░░░░╚═╝░░░╚═════╝░ VDSongBot is online.Bot By Venuja""")
idle()
