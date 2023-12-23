# Updated By @MrAbhi2k3

import asyncio
import string
import random
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply



async def reply_forward(message: Message, file_id: int):
    try:
        await message.reply_text(
            f"✨ 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖴𝗌 𝖡𝗒 𝖩𝗈𝗂𝗇𝗂𝗇𝗀 𝖮𝗎𝗋 𝖢𝗁𝖺𝗇𝗇𝖾𝗅𝗌 ✨",
            disable_web_page_preview=True,
            quote=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝖡𝗈𝗍𝗌 𝖢𝗁𝖺𝗇𝗇𝖾𝗅", url="https://t.me/Rokubotz")
                    ],
                    [
                        InlineKeyboardButton("𝖠𝗇𝗂𝗆𝖾 𝖢𝗁𝖺𝗇𝗇𝖾𝗅", url="https://t.me/Low_Mb_Zone"),
                        InlineKeyboardButton(""𝖮𝗇𝗀𝗈𝗂𝗇𝗀 𝖠𝗇𝗂𝗆𝖾, url="https://t.me/Dr_Stone_New_World_English_Dub"),
                        InlineKeyboardButton("", callback_data="closeMessage")
                    ],
                    [
                        InlineKeyboardButton("𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖦𝗋𝗈𝗎𝗉", url="https://t.me/Team_Roku"),
                        InlineKeyboardButton("", url="")
                    ]
                ]
            )
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await reply_forward(message, file_id)

async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id)
        elif Config.FORWARD_AS_COPY is False:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return media_forward(bot, user_id, file_id)
        await message.delete()

async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    sent_message = await media_forward(bot, user_id, file_id)
    await reply_forward(message=sent_message, file_id=file_id)
