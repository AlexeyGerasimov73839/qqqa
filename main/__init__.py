#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 21203369
API_HASH = "cb0de78f765b4990eec36bc59b7db08f"
BOT_TOKEN = "7155130737:AAEfmcS89KGacwnquR5TpmM1PuELpS9kkWs"
SESSION = "BAE9p8oASYT1eyfe_498-JCHJsEDyTHFl-B_nmqEHJb1ZGvjPlexv-HdHJDpPwvfuS8yTVyYhhAZEKY4q7b3-KlAL53yLJWWO3ze4c8Qetiq9JAlJP5wPIj-H8-vnuK4I5G3CQCtdf5yxVm6RZ1OwdS3kvn2mVKw5NQ4bOmTGZrcnQOnYeQLWT62OOhhpEYNye1FfrxRjI2hHEevWnWXaIontJiuYJbZmtX4qAiBB4oOxd6DafQRKHgz8VEJjNZJSRGHD_Ysoxe01e7d-AaYMXWGoXP6JgKKvST-iFjsft1x0G-atjXkxz7ElDGvtOz1PCABRQI1w1rC1rfbCJPYV3Qk_LVTUAAAAAGLTC1EAA"
FORCESUB = "testingforSRC"
AUTH = 6631992644

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
