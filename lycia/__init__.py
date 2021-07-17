from lycia.config import Config
from pyrogram import Client

APP_ID = Config.APP_ID
APP_HASH = Config.APP_HASH
TOKEN = Config.TOKEN

LYCIA = Client(':memory:', app_id=APP_ID, app_hash=API_HASH, bot_token=TOKEN)
