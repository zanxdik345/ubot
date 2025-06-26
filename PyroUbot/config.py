import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "8111609385").split()))

API_ID = int(os.getenv("API_ID", "23966045"))

API_HASH = os.getenv("API_HASH", "2f652f90142382f6f55bdc0ea7f84c81")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8031807602:AAE02KJQ1uEXJrfDZA3fCZVNlTJOT9D2juM")

OWNER_ID = int(os.getenv("OWNER_ID", "8111609385"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002633472922").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://userbotzanx:userbotzanx@cluster0.y6upssf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -1002633472922"))
