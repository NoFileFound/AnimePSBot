import datetime
import disnake
import json
from disnake.ext import commands
from modules import Config, Utils

badreason_types = ["FORBID_PLAYER_DATA_ERROR", "FORBID_CHEATING_PLUGINS", "FORBID_LOGIN_DEDFAUT", "FORBID_ABNORMAL_BEHAVIOR"]
error_types = ["4214"]

class Information(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.config = Config.db

    @commands.slash_command()
    async def baninfo(self, inter: disnake.ApplicationCommandInteraction, bantype:str=commands.Param(choices=badreason_types)):
        """
        Says additional information about given ban reason from the official server.
                
        Parameters
        ----------
        bantype: Ban reason type
        """
        await inter.response.defer(ephemeral=False)
        
        if bantype in self.config.badReasonData:
            embed = disnake.Embed(timestamp=datetime.datetime.now(), title = f"Information", color = Utils.RandomHEXColor())
            embed.add_field(name="Ban Type:", value = f"{bantype}", inline=False)
            embed.add_field(name="Explanation:", value = f"{self.config.badReasonData[bantype]['msg']}", inline=True)
            await inter.send(embed=embed)
        else:
            await inter.send("There is no information about provided ban reason type. (Try again in few days)")
        
    @commands.slash_command()
    async def errorc(self, inter: disnake.ApplicationCommandInteraction, error:str=commands.Param(choices=error_types)):
        """
        Says additional information about given server/client side error thrown by the game.
                
        Parameters
        ----------
        error: Error code
        """
        await inter.response.defer(ephemeral=False)
        
        if error in self.config.errorCodeData:
            description = self.config.errorCodeData[error]['description'] + "\n\nCauses:\n"
            i = 1
            for problem in self.config.errorCodeData[error]['problems']:
                description += str(i) + ". " + problem + "\n"
                i += 1
        
            embed = disnake.Embed(timestamp=datetime.datetime.now(), title = f"Information", color = Utils.RandomHEXColor())
            embed.add_field(name="Name:", value = f"{self.config.errorCodeData[error]['name']} ({error})", inline=True)
            embed.add_field(name="Type:", value = f"{self.config.errorCodeData[error]['type']}", inline=True)
            embed.add_field(name="Description:", value = f"{description}", inline=False)
            await inter.send(embed=embed)
        else:
            await inter.send("There is no information about provided error code. (Try again in few days)")

def setup(bot: commands.Bot):
    bot.add_cog(Information(bot))