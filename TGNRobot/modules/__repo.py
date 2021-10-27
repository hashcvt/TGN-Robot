import os
from pyrogram import Client, filters
from pyrogram.types import *

from TGNRobot.conf import get_str_key
from TGNRobot import pbot

REPO_TEXT = "**A Kawaii Girl [❤] (https://telegra.ph/file/b67112e8172c0206dbac8.png) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [:~---» T尺O̸ᒍ乇N̶ «---~:](t.me/tr0j3n) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @waifuNetwork «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(" ᴊᴏɪɴ 💫", url=f"https://t.me/waifuNetwork"),
      ],[
        InlineKeyboardButton("Yukino's ᴏᴡɴᴇʀ ❣️", url="https://t.me/tr0j3n"),
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ⚡", url="https://t.me/waifuNetSupport"),
      ],[
        InlineKeyboardButton("⚡ ᴜᴘᴅᴀᴛᴇꜱ ☑️", url="https://t.me/waifuNetwork"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
