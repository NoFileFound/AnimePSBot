import sys
sys.dont_write_bytecode = True

import disnake
import os
import threading
from disnake.ext import commands
from modules import Config

def LoadExtensions(bot):
    for root, dirs, files in os.walk("./Cogs"):
        path = root.split(os.sep)
        for file in files:
            if file.endswith(".py"):
                file = file.replace(".py", "")
                if os.path.basename(root) != "Cogs":
                    bot.load_extension(f"Cogs." + os.path.basename(root) + "." + file)
                else:
                    bot.load_extension(f"Cogs." + file)

if __name__ == "__main__":
    global bot
    Config.Load()
    bot = commands.InteractionBot(test_guilds=Config.db.Config["guilds"], owner_ids=Config.db.Config["owners"], intents=disnake.Intents().all())
    LoadExtensions(bot)
    thread = threading.Thread(target=bot.run(Config.db.Config["debugtoken"]) if Config.db.Config["debug"] else bot.run(Config.db.Config["token"]))
    thread.start()