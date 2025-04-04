import os
from dotenv import load_dotenv


load_dotenv()


EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
