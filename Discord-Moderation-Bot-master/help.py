import discord 
from discord.ext import commands

client = commands.Bot(command_prefix='>')
client.remove_command('help')

@client.command()
async def help(ctx):
        embedVar = discord.Embed(title="List Of Commands", description="See The List Of Commands Alphy Supports For Now!", color=0x00ff00)
        embedVar = discord.Embed(title="Prefix For Using These Commands Are", description="``!`` | ``>`` Is Only For Help!", color=0x00ff00)
        embedVar.add_field(name="!mute <user ID> [reason]", value="- Permanently mutes the user. Must be unmuted manually.", inline=False)
        embedVar.add_field(name="!tempmute <user ID> <duration> [reason]", value="- Permanently mutes the user. Must be unmuted manually.", inline=False)
        embedVar.add_field(name="!ban <user ID> <duration> <reason>", value="- Bans the user from the server for the duration specified, **Note:-Reason is required. If you do not have a reason, you should not be banning them.**", inline=False)
        embedVar.add_field(name="!unmute <user ID>", value="- Unmutes the user.", inline=False)
        embedVar.add_field(name="!unban <user ID>", value="- Unbans the user from the server.", inline=False)
        embedVar.add_field(name="!reload", value="- Reloads the command registry for any changes that were made to commands", inline=False)
        embedVar.add_field(name="!reload", value="- Reloads the command registry for any changes that were made to commands", inline=False)
        await ctx.channel.send(embed=embedVar)



client.run('ODkzMDI3NDQ4ODg5OTYyNDk2.YVVenw.Zno9xenO6yWwJ5VbGrS6Jzn85H0')