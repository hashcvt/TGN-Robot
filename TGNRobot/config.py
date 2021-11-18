# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/TGNRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it
    TOKEN = "2025919134:AAH1EVKeu8gNiLuKSBuDGV4BRkwbfuBzbQs"
    EVENT_LOGS = "-1001568719671"
    WEBHOOK = bool(False)
    URL = os.environ.get("URL", "")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    API_ID = 4091096
    API_HASH = "6bb0682b4af56456201c3b9d8b99c94a"
    BOT_ID = 2025919134
    DB_URI = os.environ.get("DATABASE_URL")
    MONGO_DB_URI = "mongodb+srv://TROJ3N:Nethika123@cluster0.uppg6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    DONATION_LINK = "https://t.me/tr0j3n"
    HEROKU_API_KEY = "df102f98-cc01-4e40-a020-6b50ee29af21"
    HEROKU_APP_NAME = "yukinoyuki"
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    OPENWEATHERMAP_ID = None
    VIRUS_API_KEY =  None
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    DEL_CMDS = bool (False)
    STRICT_GBAN = bool( False)
    WORKERS = int( 8)
    BAN_STICKER = None
    ALLOW_EXCL =  False
    CASH_API_KEY = "UV7PDV3CTZ4RF6JG"
    TIME_API_KEY = "6NS5U207UB3D"
    AI_API_KEY = None
    WALL_API =  None
    SUPPORT_CHAT = "waifuNetBots"
    SPAMWATCH_SUPPORT_CHAT =  None
    SPAMWATCH_API = "cI1g0oI7ttUNM1VihXYOKCXsrT~kxKtJtnTJCy0UPfcg6EdjvL0g~dzYd9q2V1Y0"
    ALLOW_CHATS = True
    DRAGONS =  "1954364940"
    DEV_USERS = "1954364940"
    DEMONS = "1954364940"
    WOLVES =  "1954364940"
    TIGERS =  "1954364940"
    OWNER_ID = 1954364940
    JOIN_LOGGER = "-1001568719671"
    OWNER_USERNAME = "tr0j3n"
    SQLALCHEMY_DATABASE_URI = None
    BL_CHATS = None

class Development(Config):
    LOGGER = True
