# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = ("17170223")
	API_HASH = ("82dcb7e30b20c4e3129c152a53cddb95")
	BOT_TOKEN = ("6564783717:AAH1YLwx3o3YKk0M70yjz2Tzi3fJs8dw1Pk")
	BOT_USERNAME= ("FZAnimeRobot")
	DB_CHANNEL= ("-1001989663548")
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL')
	SHORTLINK_API = os.environ.get('SHORTLINK_API')
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1966867320"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = ("-1001720043105")
	LOG_CHANNEL= ("-1001989663548")
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
├🔸 **Developer:** [Snowball](https://t.me/Snowball_Official) 
│
├🔹 **Bot Support:** [Support](https://t.me/Roofiverse)
│
├🔸 **Bot Updates:** [Bots Channel](https://t.me/Rokubotz)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [Snowball](https://github.com/Snowball-0)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Snowball_Official) or ```Snowball_Official```
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ, I ᴡɪʟʟ sᴛᴏʀᴇ ɪᴛ ɪɴ ᴍʏ Dᴀᴛᴀʙᴀsᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɢɪᴠᴇ ʏᴏᴜʀ sʜᴀʀᴇʙʟᴇ ʟɪɴᴋ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴀᴛ ғɪʟᴇ.


🚀 Powered By @Roofiverse

"""
	
