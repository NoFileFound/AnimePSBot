import datetime
import disnake
import os
import psutil
from disnake.ext import commands
from modules import Config, Utils

class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.is_owner()
    @commands.slash_command()
    async def admin(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @admin.sub_command()
    async def shutdown(self, inter: disnake.ApplicationCommandInteraction):
        """
        Shutdown the bot.
        """
        await inter.response.defer(ephemeral=True)
        await inter.send("Done!")
        await self.bot.close()

    @admin.sub_command()
    async def stats(self, inter: disnake.ApplicationCommandInteraction):
        """
        Fetches information about physical machine, where bot is hosted.
        """
        await inter.response.defer(ephemeral=True)
        ram = psutil.Process(os.getpid())
        embed = disnake.Embed(timestamp=datetime.datetime.now(), title = f"Server Stats", color = Utils.RandomHEXColor())
        embed.add_field(name="CPU Usage:", value = f"{round(psutil.cpu_percent())}%", inline=False)
        embed.add_field(name="Memory Usage:", value = f"{round(psutil.virtual_memory().percent)}%", inline=False)
        embed.add_field(name="RAM Usage:", value = f"{(ram.memory_info().rss / (1e+6)):.2f}MB", inline=False)
        embed.add_field(name="Available Memory:", value=f"{round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)}%", inline=False)
        embed.add_field(name="API Latency:", value=f"{self.bot.latency}ms", inline=False)
        await inter.send(embed=embed)
        
    @admin.sub_command()
    async def reload(self, inter: disnake.ApplicationCommandInteraction):
        """
        Reload command
        """
        await inter.response.defer(ephemeral=True)
        Config.db.Reload()
        for root, dirs, files in os.walk("./Cogs"):
            path = root.split(os.sep)
            for file in files:
                if file.endswith(".py"):
                    file = file.replace(".py", "")
                    if os.path.basename(root) != "Cogs":
                        self.bot.reload_extension(f"Cogs." + os.path.basename(root) + "." + file)
                    else:
                        self.bot.reload_extension(f"Cogs." + file)
        await inter.send("Done!")

def setup(bot: commands.Bot):
    bot.add_cog(Admin(bot))