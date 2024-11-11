from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "24818964"))
API_HASH = getenv("API_HASH", "1ab692fe8efac1343c7d6a6ee1d4194f")

BOT_TOKEN = getenv("BOT_TOKEN", "8120562276:AAHVyD_2E8J45GdsdlQkg3hCUhfWks1sxoY")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://marwin2002:7Yw81GpqZq2a9j4R@cluster0.rgqgp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

OWNER_ID = int(getenv("OWNER_ID", 7078122796))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/izzy_tamil_junction")
