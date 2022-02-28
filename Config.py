import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "5238433330:AAGQdHfe1PdByMdZUp9yGsKZbJMhrWjXBJ8"
    DATABASE_URL = "https://t.me/endangsusantii"
    APP_ID = "11000823"
    API_HASH = "742cd7b8fa09151d890ea9a21dec3f3d"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "<b><u>Force Subscribe</u>\nForce group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.</b>\n\n<b><u>⚠️Note</u> :- I Can Force Members To Join Only A Public Channel not Pvt Channel.</b>",
        
        "<b><u>Setup</u>\nFirst of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.</b>",
        
        "<b><u>Commmands</u>\n/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe</b>",
        
        "<b>Developed by @StarkXT8</b>"
      ]

      START_MSG = "**Hey [{}](tg://user?id={})**\n\n**I can force members to join a specific channel before writing messages in the group.\nLearn more at /help**"
