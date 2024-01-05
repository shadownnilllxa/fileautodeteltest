# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int("21027612")
	API_HASH=("b36c5dc986f77eedd4bbf356b65eab19")
	BOT_TOKEN=("6791224524:AAGxNwyJ0XxPu4nTJjH_TV-djIxaI7kE4_Q")
	BOT_USERNAME=("Cholefilestorebot")
	DB_CHANNEL = int("-1001941319109")
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL')
	SHORTLINK_API = os.environ.get('SHORTLINK_API')
	BOT_OWNER = int("6705973489")
	DATABASE_URL=("mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL=("-1001278639314")
	LOG_CHANNEL=("-1001941319109")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸 **Developer:** [Waifu](https://t.me/waifu4ur) 
│
├🔹 **Bot Support:** [Support](https://t.me/Team_Roku)
│
├🔸 **Bot Updates:** [Bots Channel](https://t.me/Rokubotz)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [Waifu](https://t.me/waifu4ur)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/waifu4ur)
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴏғ @waifu4ur
ᴛᴏ ᴜsᴇ ᴍᴇ ʏᴏᴜ ᴊᴜsᴛ ʜᴀᴠᴇ ᴛᴏ sɪᴍᴘʟɪғʏ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ғɪʟᴇ & ɪ'ʟʟ ᴄᴏɴᴠᴇʀᴛ ɪᴛ ɪɴᴛᴏ ʟɪɴᴋ

"""
	
