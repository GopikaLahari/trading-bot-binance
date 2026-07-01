import os
from binance.client import Client
from dotenv import load_dotenv
from bot.logging_config import logger

# Load the keys from your .env file
load_dotenv()


def get_futures_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        logger.error("API Keys missing from environment variables.")
        raise ValueError("API Keys missing in .env file")

    # testnet=True points the client to the fake-money testing ecosystem
    client = Client(api_key, api_secret, testnet=True)
    return client
