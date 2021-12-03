import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "ᴜғᴏ ᴍᴜsɪᴄ ʙᴏᴛ")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/1b5b5171887c08d6bfa84.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/1b5b5171887c08d6bfa84.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/1b5b5171887c08d6bfa84.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/1b5b5171887c08d6bfa84.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "B82bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "e8e8m")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "HMBots")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "HMBots")
OWNER_NAME = getenv("OWNER_NAME", "e8e8m") 
DEV_NAME = getenv("DEV_NAME", "e8e8m")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
