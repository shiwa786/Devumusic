# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "10448562"))
API_HASH = getenv("API_HASH", "4a8a640bb154fc59227ccbcb5d5ce612")
BOT_TOKEN = getenv("BOT_TOKEN", "5545963604:AAFyeZDxieUOq1mmz6khwuSzTvvf8JiBJcU")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Denvil")
BOT_USERNAME = getenv("BOT_USERNAME", "miselisarobot")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "elisha_spport")
BOT_NAME = getenv("BOT_NAME","Elisa🥀")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))
SESSION_NAME = getenv("SESSION_NAME", "BQA4e-wjD-pyzN5qgV_F2ujobZWeIiNBHlZ_PDtJU2k8TlXegWbgcOxsbM9SJj-ccRafJGFzm1_kwBnDrA9SQq0YLBn3aPDdd4kN9m9Z2TZ8U1o1ZWeCQXSKaYwlQd_YvNgX0umh62L9p0XaUCYlTa0yPrtzj8At0YJRMsVkX2r-_jhr7u9-m1bKMAFUKv5WOh4NYiuNmze1uakIXqU5mtC2JRg9XPd6-PPcsStJx0SiaJGl03pgvGnFI5UrHLSmv6oFj2qkro7WcYa9dHu2djAYYqoURXnsEKeK_Cz621hZbDFSz36DrR0jC0eVOC_SgtEYK2scdigY6JkG6zMaDcJEAAAAAUvyJg4A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "DISABLE")
BOT_IMG = getenv("BOT_IMG", "https://telegra.ph/file/2c3097ae03f950800a66f.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5280801259").split()))
