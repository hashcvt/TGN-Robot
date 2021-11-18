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

    API_ID = 4091096  # integer value, dont use ""
    API_HASH = "6bb0682b4af56456201c3b9d8b99c94a"
    TOKEN = "2025919134:AAH1EVKeu8gNiLuKSBuDGV4BRkwbfuBzbQs"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1954364940  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "tr0j3n" 
    SUPPORT_CHAT = "waifuNetwork"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001568719671
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001568719671
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = ""  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "cI1g0oI7ttUNM1VihXYOKCXsrT~kxKtJtnTJCy0UPfcg6EdjvL0g~dzYd9q2V1Y0"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
  
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "UV7PDV3CTZ4RF6JG"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "6NS5U207UB3D"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
