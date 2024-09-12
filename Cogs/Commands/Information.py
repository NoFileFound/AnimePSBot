import datetime
import disnake
import json
from disnake.ext import commands
from modules import Config, Utils

badreason_types = ["FORBID_PLAYER_DATA_ERROR", "FORBID_CHEATING_PLUGINS", "FORBID_LOGIN_DEDFAUT", "FORBID_ABNORMAL_BEHAVIOR"]
prod_types = ["PRODUCTION_CN", "SANDBOX_CN", "PRODUCTION_OS", "SANDBOX_OS", "PRODUCTION_PRE_RELEASE_CN", "PRODUCTION_PRE_RELEASE_OS", "TEST_CN", "TEST_OS", "PET_CN", "BETA_CN", "BETA_CN_PRE", "BETA_OS", "BETA_OS_PRE", "HOTFIX_CN", "HOTFIX_OS"]

# Error types
error_types_dispatch = ["4201", "4202", "4203", "4204", "4205", "4206", "4207", "4208", "4209", "4210", "4211", "4212", "4213", "4214", "4215"]
error_types_login = ["4301", "4302", "4303", "4304", "4305", "4306", "4307", "4308", "4309", "4310"]
error_types_network = ["4001", "4002", "4003", "4004", "4005", "4006", "4007", "4008", "4009", "4010", "4011"]
error_types_sdk = ["4401", "4402", "4403", "4404", "4405", "4406", "4407", "4408"]
error_types_resources = ["-9000", "-9107", "-9908"]

class Information(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.config = Config.db
        
    async def fetchMan(self, inter: disnake.ApplicationCommandInteraction, error: str):
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
    async def regionconf(self, inter: disnake.ApplicationCommandInteraction, typ:str=commands.Param(choices=["client", "server"])):
        """
        Says additional information about region's config based on client and server side.
                
        Parameters
        ----------
        typ: Client or server config
        """
        await inter.response.defer(ephemeral=False)
        
        message = ""
        for info in self.config.regionConfData[typ]:
            message += f"{info['name']} ({info['var']}) -> {info['description']}\n"
        message += "\n"
        
        embed = disnake.Embed(timestamp=datetime.datetime.now(), title = f"Variables", color = Utils.RandomHEXColor())
        embed.add_field(name="", value = f"```{message}```", inline=False)
        await inter.send(embed=embed)
        
    @commands.slash_command()
    async def prodtype(self, inter: disnake.ApplicationCommandInteraction, prodtype:str=commands.Param(choices=prod_types)):
        """
        Says additional information about region's environment type.
                
        Parameters
        ----------
        prodtype: Environment
        """
        await inter.response.defer(ephemeral=False)
        if prodtype in self.config.prodtypeConfData:
            embed = disnake.Embed(timestamp=datetime.datetime.now(), title = f"Information", color = Utils.RandomHEXColor())
            embed.add_field(name="Name:", value = f"{prodtype}", inline=True)
            embed.add_field(name="Id:", value = f"{self.config.prodtypeConfData[prodtype]['id']}", inline=True)
            embed.add_field(name="Url:", value = f"{self.config.prodtypeConfData[prodtype]['url']}", inline=False)
            embed.add_field(name="Descrption:", value = f"{self.config.prodtypeConfData[prodtype]['descrption']}", inline=False)
            await inter.send(embed=embed)
        else:
            await inter.send("There is no information about provided region environment. (Try again in few days)")


    @commands.slash_command()
    async def errorc(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @errorc.sub_command()
    async def dispatch(self, inter: disnake.ApplicationCommandInteraction, error:str=commands.Param(choices=error_types_dispatch)):
        """
        Says additional information about given error related to dispatch.
                
        Parameters
        ----------
        error: Error code
        """
        await self.fetchMan(inter, error)

    @errorc.sub_command()
    async def login(self, inter: disnake.ApplicationCommandInteraction, error:str=commands.Param(choices=error_types_login)):
        """
        Says additional information about given error related to login.
                
        Parameters
        ----------
        error: Error code
        """
        await self.fetchMan(inter, error)
        
    @errorc.sub_command()
    async def network(self, inter: disnake.ApplicationCommandInteraction, error:str=commands.Param(choices=error_types_network)):
        """
        Says additional information about given error related to network.
                
        Parameters
        ----------
        error: Error code
        """
        await self.fetchMan(inter, error)

    @errorc.sub_command()
    async def resources(self, inter: disnake.ApplicationCommandInteraction, error:str=commands.Param(choices=error_types_resources)):
        """
        Says additional information about given error related to game resources.
                
        Parameters
        ----------
        error: Error code
        """
        await self.fetchMan(inter, error)

    @errorc.sub_command()
    async def sdk(self, inter: disnake.ApplicationCommandInteraction, error:str=commands.Param(choices=error_types_sdk)):
        """
        Says additional information about given error related to SDK.
                
        Parameters
        ----------
        error: Error code
        """
        await self.fetchMan(inter, error)
        

def setup(bot: commands.Bot):
    bot.add_cog(Information(bot))