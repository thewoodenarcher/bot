import discord
from discord.ext import commands
import asyncio
import time
import os

bot = discord.ext.commands.Bot(command_prefix="j!")
bot.remove_command("help")

@bot.command(name="from")
@commands.is_owner()
async def _from(ctx, user: discord.Member, *, command: str):
    ctx.message.author = user
    ctx.message.content = f"{ctx.prefix}{command}"
    await bot.process_commands(ctx.message)

@bot.command()
async def spamme(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.orange())
    embed.set_author(name='spamme')
    embed.add_field(name='Spam', value='Spam', inline=False)
    for x in range(10):
        await ctx.author.send(embed=embed)

bot.command()
async def say(ctx, *, word):
    for x in range(10):
        await ctx.send(word)
        
@bot.event
async def on_ready():
    print("Bot is online and connected to Discord")


@bot.command()
@commands.has_permissions(manage_roles=True)
async def role(ctx, userName: discord.Member, role: discord.Role = None):
    if role is None:
        return await ctx.send("You haven't specified a role! ")
    if role not in ctx.guild.roles:
        return await ctx.send("That role doesn't exist.")
    for server_role in ctx.guild.roles:
        if server_role.id == role.id:
            if role not in userName.roles:
                await userName.add_roles(role)
                return await ctx.send("{} role has been added to {}.".format(role, userName.mention))
    if role in userName.roles:
        await userName.remove_roles(role)
        return await ctx.send("{} role has been removed from {}.".format(role, userName.mention))

@bot.command()
@commands.has_permissions (kick_members=True)
async def kick(ctx, userName: discord.User ):
    await bot.kick(userName)
    await ctx.send("Successfully commited die.")

@bot.command()
async def mix(ctx, word1, word2):
    await ctx.send(word1[:int(len(word1) / 2)] + word2[int(len(word2) / 2):])

@bot.command()
async def antimix(ctx, word1, word2):
    await ctx.send(word1[int(len(word1) / 2):] + word2[:int(len(word2) / 2)])


@bot.command()
async def blend(ctx):
    await ctx.send("**_WRRRRRRRRRRRRRR_**")



@bot.command()
async def say(ctx, *, word):
    await ctx.send(word)

@bot.command()
async def embed(ctx, *, sth):
    embed = discord.Embed(title="You said:", description=(sth), color=000000)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount, bulk=True)
    await ctx.send('OOF messages')

@bot.command()
async def help(ctx):
    embed = discord.Embed(colour2=discord.Colour.red())
    embed.set_author(name='Page 1')
    embed.add_field(name='j!help (page)', value='Shows all commands on the given page', inline=False)
    embed.add_field(name='j!say (something)', value='Says anything.', inline=False)
    embed.add_field(name='j!kick (user)', value='Kicks the mentioned user', inline=False)
    embed.add_field(name='j!spamme', value='Spams you Literally.', inline=False)
    embed.add_field(name='j!blend', value='Returns a message.', inline=False)
    embed.add_field(name='j!clear (value)', value='Clears the given amount of messages.', inline=False)
    embed.add_field(name='j!mix (something)(something else)', value='Mixes the given words.', inline=False)
    embed.add_field(name='j!antimix (something)(something else)', value='AntiMixes the given words.', inline=False)
    embed.add_field(name='j!embed (something)', value='Says anything but in embed.', inline=False)
    await ctx.author.send(embed=embed)

@bot.command()
async def help2(ctx):
    embed = discord.Embed(colour3=discord.Colour.orange())
    embed.set_author(name='Page 2')
    embed.add_field(name='j!role (user) (role)', value='If a user has a role, it is removed.If not, it is added.', inline=False)
    await ctx.author.send(embed=embed)

bot.run(os.getenv("TOKEN"))
