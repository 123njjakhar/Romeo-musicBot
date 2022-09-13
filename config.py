import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCwh2NWPba5LmwH4wcyPqI6aU7HcnS3PRbk_J7g7S98HTQbfGAWYn7DOw_swopi9pjV_yDa35GGJe5R80aYsCG31YgRrFGEor0ERaZt79mZ7XpKgYK5UMbeQmPP9-w8Xh_BVSJZe9vSVDRpW56G21U0OIm933kBQY55H6SV84FSNM9ZEki8YF4KiV0B95SNPsv8GwJUL_QyaAEXWaQMdXms6M3emWKTNa3BZR2lwXP0_UhMyfmb-6s_Ss2fjHwU7dx44MiGjd5OVlPgaXwDhlolq3aIHWR2oZ54evk0R40ySvbapG_szSYp1SFRzJ7SgrD6GIq7w_6JdscADj0KKJuyaZgpsAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5594836549:AAG0sYTMuq5_gr5X9XwknoGonChcC3vLxmU")
BOT_NAME = getenv("BOT_NAME", "NJ_OP_MUSIC_BOT")
API_ID = int(getenv("API_ID", "13909391"))
API_HASH = getenv("API_HASH", "19d0868bb18965eb6eb2e34ec5778310")
OWNER_NAME = getenv("OWNER_NAME", "1771579824")
OWNER_USERNAME = getenv("OWNER_USERNAME", "1771579824")
ALIVE_NAME = getenv("ALIVE_NAME", "1771579824")
BOT_USERNAME = getenv("BOT_USERNAME", "NJ_OP_MUSIC_BOT")
OWNER_ID = getenv("OWNER_ID", "1771579824")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "1771579824")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "RomeoBot_op")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Romeo_op")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1771579824").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/61fb830842b656136934b.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/61fb830842b656136934b.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "54000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Romeo-RJ/Romeo-musicBot")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/61fb830842b656136934b.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/61fb830842b656136934b.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/61fb830842b656136934b.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/61fb830842b656136934b.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/61fb830842b656136934b.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/61fb830842b656136934b.jpg")
