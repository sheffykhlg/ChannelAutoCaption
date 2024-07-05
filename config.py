import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7292591629:AAHDqNNpSu7qlJftlP_ponopfkv_rG3HDS0")
    API_ID = int(os.environ.get("API_ID", 29023986))
    API_HASH = os.environ.get("API_HASH", "895fde5d06418650fdcce2fddebe8276")
    DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://grouphelp:grouphelp@grouphelp.ccgqorv.mongodb.net/?retryWrites=true&w=majority&appName=grouphelp")
