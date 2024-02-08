from os import path, getenv

class config:
    API_ID = int(getenv("API_ID", "7880546"))
    API_HASH = getenv("API_HASH", "1acb85d7ced32df2a29ffa323724a199")
    BOT_TOKEN = getenv("BOT_TOKEN", "6758944091:AAE3w2ncCnobmiLoR-PW_P07GTIOO85Ma5I")
    CHID = int(getenv("CHID", "-1000112234"))
    IP_API =getenv("ACCESS_TOKEN","f016dde667c323")
    LOGCHID = int(getenv("LOGCHID", "-1000112234"))
con = config()
