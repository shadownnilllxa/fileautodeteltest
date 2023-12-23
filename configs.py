# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int("21027612")
	API_HASH=("b36c5dc986f77eedd4bbf356b65eab19")
	BOT_TOKEN=("6603389643:AAEh-w7kIpcSqZvOnidTsvhUq2qCUpSoWx0")
	BOT_USERNAME=("CloudXStoreRobot")
	DB_CHANNEL = int("-1001175626344")
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL')
	SHORTLINK_API = os.environ.get('SHORTLINK_API')
	BOT_OWNER = int("5098097249")
	DATABASE_URL=("mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL=("-1001175626344")
	LOG_CHANNEL=("-1001175626344")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
╭────[ **🔅𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆𝖢𝗅𝗈𝗎𝖽𝖡𝗈𝗍🔅**]────⍟
│
├🔸 **𝖬𝗒 𝖭𝖺𝗆𝖾:** [𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖢𝗅𝗈𝗎𝖽 𝖡𝗈𝗍](https://t.me/{BOT_USERNAME})
│
├🔸 **𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾:** [𝖯𝗒𝗍𝗁𝗈𝗇 3](https://www.python.org)
│
├🔹 **𝖫𝗂𝖻𝗋𝖺𝗋𝗒:** [𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆](https://docs.pyrogram.org)
│
├🔹 **𝖧𝗈𝗌𝗍𝖾𝖽 𝖮𝗇:** [𝖦𝗈𝗈𝗀𝗅𝖾 𝖢𝗅𝗈𝗎𝖽](https://cloud.google.com)
│
├🔸 **𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋:** [𝖲𝗇𝗈𝗐𝖻𝖺𝗅𝗅](https://t.me/Snowball_Official) 
│
├🔹 **𝖡𝗈𝗍 𝖲𝗎𝗉𝗉𝗈𝗋𝗍:** [𝖲𝗎𝗉𝗉𝗈𝗋𝗍](https://t.me/Team_Roku)
│
├🔸 **𝖡𝗈𝗍 𝖴𝗉𝖽𝖺𝗍𝖾𝗌:** [𝖡𝗈𝗍𝗌 𝖢𝗁𝖺𝗇𝗇𝖾𝗅](https://t.me/Rokubotz)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [𝖲𝗇𝗈𝗐𝖻𝖺𝗅𝗅](https://t.me/Snowball_Official)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Snowball_Official)
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴏғ @waifu4ur
ᴛᴏ ᴜsᴇ ᴍᴇ ʏᴏᴜ ᴊᴜsᴛ ʜᴀᴠᴇ ᴛᴏ sɪᴍᴘʟɪғʏ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ғɪʟᴇ & ɪ'ʟʟ ᴄᴏɴᴠᴇʀᴛ ɪᴛ ɪɴᴛᴏ ʟɪɴᴋ

"""
	
