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
SESSION = "BAFDiakANCPEZBK7m7Dnqzn84w-U8ufO48T2F1y49RNPski0yePPbduJvwpxoetSIjI2XnMmQ5V4DTN47H8nbaMGsWw2g2uw8CIcLogSV5UkGGKHV9CBo-k7PF3ZGwpsK1XbRLZ3LuiMOZJrKN-qMC5YXDp7hCBKoH6YU5MoR8iTFn1Ys30XuFa623I2E_dEgkyxbJD8wv9ToLuendbnsV1ftRlCvFYHkSSeDqBMbA-KdWbRM7omyTs7CPFWlY9C31sBFbPhg-7-41B57Y59ow4k0VdwBrcz3u_f7eo3EmUquJjdl72lcmRZSuZoZ_fB4o544YNk4R1iuA2a684eMH55orHT1wAAAAGLTC1EAA"
FORCESUB = "testingforSRC"
AUTH = 6631992644, 6090819567

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
