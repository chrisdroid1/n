from lycia.config import Config
from pyrogram import Client

APP_ID = Config.APP_ID
APP_HASH = Config.APP_HASH
TOKEN = Config.TOKEN

LYCIA = Client(':memory:', api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
