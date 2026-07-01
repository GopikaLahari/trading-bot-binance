import logging

# This sets up logging to BOTH a file and your terminal screen
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        # Saves to file as required by assignment
        logging.FileHandler("bot_activity.log"),
        logging.StreamHandler()                  # Prints to terminal screen
    ]
)

# This is the exact variable the other files are looking to import!
logger = logging.getLogger("trading_bot")
