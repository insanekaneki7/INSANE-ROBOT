import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from kanekiRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID,BOT_NAME,START_IMG

PHOTO = [
    "https://te.legra.ph/file/eace7a5d8d4b515a11e50.jpg",
    "https://te.legra.ph/file/eace7a5d8d4b515a11e50.jpg",
    "https://te.legra.ph/file/eace7a5d8d4b515a11e50.jpg",
    "https://te.legra.ph/file/eace7a5d8d4b515a11e50.jpg",
    "https://te.legra.ph/file/eace7a5d8d4b515a11e50.jpg",
]

kaneki = [
    [
        InlineKeyboardButton(text="ɴᴏᴏʙ", user_id=OWNER_ID),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/insanesociety"),
    ],
    [
        InlineKeyboardButton(
            text="➕🥀😎ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙᴀʙʏ🥀😎",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]



@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.2)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await asyncio.sleep(0.1)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")

    await accha.delete()
    await asyncio.sleep(0.3)
    umm = await m.reply_sticker(
        "CAACAgUAAxkDAAJHbmLuy2NEfrfh6lZSohacEGrVjd5wAAIOBAACl42QVKnra4sdzC_uKQQ"
    )
    await umm.delete()
    await asyncio.sleep(0.2)
    await m.reply_photo(
        START_IMG,
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ 『[{BOT_NAME}](f"t.me/{BOT_USERNAME}")』**
   ━━━━━━━━━━━━━━━━━━━
  » **ᴍʏ ᴏᴡɴᴇʀ :** [KANEKI](tg://user?id=6624008600)
  
  » **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{lver}`
  
  » **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tver}`
  
  » **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pver}`
  
  » **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{pyver()}`
   ━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(kaneki),
    )
