from os import path, getenv

class config:
    API_ID = int(getenv("API_ID", "Enter Your API KEY"))
    API_HASH = getenv("API_HASH", "Enter Your API Hash")
    BOT_TOKEN = getenv("BOT_TOKEN", "Enter Your BOT Token")
    IP_API =getenv("ACCESS_TOKEN","IP-API API KEY IS HERE")
    
con = config()
