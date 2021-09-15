from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, I am The Assitant Of @KHILADIKING45 🥳 !**
        """,
        reply_markup=InlineKeyboardMarkup(
           [
              InlineKeyboardButton('Tamil Chat🍒 ', url='https://t.me/Tamil_Chat_Empire'),
              InlineKeyboardButton('Facebook🎻', url='https://www.facebook.com/khiladi.kishoth.3'),
           ],
           [
              InlineKeyboardButton('Instagram❄️', url='https://www.instagram.com/khiladiking45/'),
        
           ]
    )
