import disnake
from disnake.ext import commands

class SlashCommandErrorHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_slash_command_error(self, inter: disnake.ApplicationCommandInteraction, error): 
        if isinstance(error, commands.errors.CheckFailure) or isinstance(error, commands.errors.MissingPermissions):
            await inter.send("You don't have permission to use this command. Contact an administrator for more information.", ephemeral = True)
        elif isinstance(error, commands.errors.CommandOnCooldown):
            await inter.send(f"You currently are at cooldown. Please try again after {error.retry_after:.2f} seconds.", ephemeral = True)
        elif isinstance(error, commands.errors.NSFWChannelRequired):
            await inter.send("The command can be executed only in NSFW channel.", ephemeral = True)
        elif isinstance(error, commands.errors.PrivateMessageOnly):
            await inter.send("The command can be executed only in DM.", ephemeral = True)
        elif isinstance(error, commands.errors.DisabledCommand):
            await inter.send("The command is disabled by administrators. Contact an administrator for more information.", ephemeral = True)
        elif isinstance(error, commands.errors.BotMissingPermissions):
            await inter.send("The bot does not have a rights to execute this command. Contact an administrator for more information.", ephemeral = True)
        elif isinstance(error, commands.errors.NotOwner):
            await inter.send("Only bot owners can execute this command.", ephemeral = True)
        elif isinstance(error, commands.errors.MessageNotFound):
            await inter.send("The specific message could not get found.", ephemeral = True)
        elif isinstance(error, commands.errors.MemberNotFound) or isinstance(error, commands.errors.UserNotFound):
            await inter.send("The specific guild member could not get found.", ephemeral = True)
        elif isinstance(error, commands.errors.GuildNotFound):
            await inter.send("The specific guild could not get found.", ephemeral = True)
        elif isinstance(error, commands.errors.ChannelNotFound):
            await inter.send("The specific guild channel could not get found.", ephemeral = True)
        elif isinstance(error, commands.errors.ThreadNotFound):
            await inter.send("The specific thread or forum post could not get found.", ephemeral = True)
        elif isinstance(error, commands.errors.RoleNotFound):
            await inter.send("The specific guild role could not get found.", ephemeral = True)
        elif isinstance(error, commands.errors.EmojiNotFound):
            await inter.send("The specific guild emoji could not get found.", ephemeral = True)
        elif isinstance(error, commands.errors.GuildStickerNotFound):
            await inter.send("The specific guild sticker could not get found.", ephemeral = True)
        else:
            await inter.send(str(error) + ". Contact an administrator for more information.", ephemeral = True)

def setup(bot: commands.Bot):
    bot.add_cog(SlashCommandErrorHandler(bot))