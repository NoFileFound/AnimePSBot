import ctypes
import datetime
import disnake
import os
import psutil
import random
from modules import Config
from disnake.ext import commands

class ON_READY_EVENT(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.isOnline = False

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.isOnline:
            self.isOnline = True
            ram = psutil.Process(os.getpid())
            ctypes.windll.kernel32.SetConsoleTitleW(f"Name: {self.bot.user.name}#{self.bot.user.discriminator} || ID: {self.bot.user.id} || Latency: {self.bot.latency}")
            print("[RELEASE] BOT is online!")
            print(f"[DETAILS] CPU Usage: {round(psutil.cpu_percent())}%")
            print(f"[DETAILS] Memory Usage: {round(psutil.virtual_memory().percent)}%")
            print(f"[DETAILS] RAM Usage: {(ram.memory_info().rss / (1e+6)):.2f}MB")
            print(f"[DETAILS] Available Memory: {round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)}%")
            await self.bot.change_presence(status=disnake.Status.idle, activity=disnake.Game(name="Touhou 19"))
            for guild in self.bot.guilds:
                print(f"[GUILDS] {guild.name} --> {guild.id} --> {len(guild.members)}")

def setup(bot: commands.Bot):
    bot.add_cog(ON_READY_EVENT(bot))