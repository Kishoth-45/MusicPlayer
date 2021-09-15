from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        
        f"""<b>Hey {message.from_user.first_name}!
       \n I Am The Assitant of @KHILADIKING45 ✨🍒[https://telegra.ph/file/c639a3b15fed410b820f4.jpg].
       </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
              InlineKeyboardButton('Tamil Chat🍒 ', url='https://t.me/Tamil_Chat_Empire'),
              InlineKeyboardButton('Facebook🎻', url='https://www.facebook.com/khiladi.kishoth.3'),
           ],
           [
              InlineKeyboardButton('Instagram❄️', url='https://www.instagram.com/khiladiking45/')
        
           ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support Group  ", url="https://t.me/GodofAnjelsupport"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!

**Common Commands**:
**/play**  Reply to an audio file or YouTube link to play it or use /play <song name>.
**/splay** Play music from Jio Saavn, Use /splay <song name> or <code>/splay -a album name</code> to play all the songs from that album.
**/player**  Show current playing song.
**/upload** Uploads current playing song as audio file.
**/help** Show help for commands
**/playlist** Shows the playlist.
**Admin Commands**:
**/skip** [n] ...  Skip current or n where n >= 2.
**/cplay** Play music from a channel's music files.
**/yplay** Play music from a youtube playlist.
**/join**  Join voice chat.
**/leave**  Leave current voice chat
**/shuffle** Shuffle Playlist.
**/vc**  Check which VC is joined.
**/stop**  Stop playing.
**/radio** Start Radio.
**/stopradio** Stops Radio Stream.
**/clearplaylist** Clear the playlist.
**/export** Export current playlist for future use.
**/import** Import a previously exported playlist.
**/replay**  Play from the beginning.
**/clean** Remove unused RAW PCM files.
**/pause** Pause playing.
**/resume** Resume playing.
**/volume** Change volume(0-200).
**/mute**  Mute in VC.
**/unmute**  Unmute in VC.
**/restart**  Update and restarts the Bot.
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Creator🎻", url="https://t.me/KhiladiKing45"
                    )
                ]
            ]
        )
    )    
