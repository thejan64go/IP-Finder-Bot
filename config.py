from os import path, getenv

class config:
    API_ID = int(getenv("API_ID", "Your API ID"))
    API_HASH = getenv("API_HASH", "YOUR API HASH")
    BOT_TOKEN = getenv("BOT_TOKEN", "YOUR BOT TOKEN")
    IP_API =getenv("ACCESS_TOKEN","IP API ACCESS TOKEN")
    LOGCHID = int(getenv("LOGCHID", "LOG CHANNEL ID"))
con = config()
