import discord
from discord.ext import commands
import random 
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
async def serverinfo(ctx):
     embed = discord.Embed(colour=discord.Colour.red())
     embed.add_field(value=(icon_url_as(*, format='webp', size=1024)
     embed.add_field(name= 'Name', value=(ctx.guild.name), inline=False)
     embed.add_field(name= 'Owner', value=(ctx.guild.owner), inline=False)
     embed.add_field(name= 'Member count:', value=(ctx.guild.member_count), inline=False)
     embed.add_field(name= 'Verification level',value=(ctx.guild.verification_level), inline=False)
     embed.add_field(name= 'Created at',value=(ctx.guild.created_at), inline=False)
     await ctx.send (embed=embed)
    
    
@bot.command()
@commands.has_permissions(manage_messages = True)
async def mute(self, ctx, user:discord.Member=None):
    if user == None:
        await ctx.send("Who do i mute? ")
    elif user == ctx.author.id:
        await ctx.send("You can't mute youserlf...")
    elif user.id == 459300768525189121:
        await ctx.send("Why would i even mute myself?!")
    else:
        await ctx.send("{} just got JOEYED".format(user.name))
        await ctx.channel.set_permissions(user, send_messages=False)
        await asyncio.sleep(120)
        await ctx.channel.set_permissions(user, send_messages=True)
        await ctx.send("You are unJOEYED {} !".format(user.name))
    

@bot.command()
async def dmme(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.orange())
    embed.set_author(name='Hi')
    embed.add_field(name='hello', value='you asked', inline=False)
    await ctx.author.send(embed=embed)

@bot.command()
@commands.is_owner()
async def repeat(ctx, times: int, *, msg):
    for x in range(times):
        await ctx.send(msg)
        
@bot.event
async def on_ready():
    print("Bot is online and connected to Discord")
    responses = ['j!help', 'the word \"bed\" looks like a bed', 'this bot is not that good. chill, im learning','u have ligma','j!help for help'] 
    await bot.change_presence(activity=discord.Game(name=random.choice(responses)))


@bot.command()
async def ping(ctx):
    color = discord.Color(value=0)
    e = discord.Embed(color=color, title='Pinging')
    e.description = 'lmao wait... :thinking:'
    msg = await ctx.send(embed=e)
    em = discord.Embed(color=color, title='Big OOF! Your supersonic latency(like u even care)  is:')
    em.description = f"{bot.latency * 1000:.4f} ms"
    em.set_thumbnail(
        url="https://media.giphy.com/media/nE8wBpOIfKJKE/giphy.gif")
    await msg.edit(embed=em)
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
async def kick(ctx, userName: discord.Member):
    await userName.kick(userName)
    await ctx.send("Successfully commited die.")

@bot.command()
async def mix(ctx, word1, word2):
    await ctx.send(word1[:int(len(word1) / 2)] + word2[int(len(word2) / 2):])


@bot.command()
async def antimix(ctx, word1, word2):
    await ctx.send(word1[int(len(word1) / 2):] + word2[:int(len(word2) / 2)])

@bot.command()
async def invite(ctx):
    await ctx.send('https://discordapp.com/oauth2/authorize?client_id=459300768525189121&permissions=79872&scope=bot')

@bot.command()
async def server(ctx):
    await ctx.send('https://discord.gg/KuJGXVK')

@bot.command()
async def blend(ctx):
    await ctx.send("**_WRRRRRRRRRRRRRR_**")



@bot.command()
async def say(ctx, *, word):
    await ctx.send(word)
    await discord.Message.delete()
@bot.command()
async def embed(ctx, *, args):
    embed = discord.Embed(title="You said:", description=args, color=000000)
    await ctx.send(embed=embed)
    await discord.Message.delete()


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount, bulk=True)
    await ctx.send('OOF messages')

@bot.command()
async def truefalse(ctx, *, stuff=None):
    if not stuff:
        return await ctx.send("What do i even scan? Yea sure that's true. ")
    em = discord.Embed(title=stuff, description=random.choice(["True", "False"]), colour=discord.Colour.red ())
    await ctx.send(embed=em)
@bot.command()
async def choose(ctx, args=None, stuff=None):
    if not stuff:
        return await ctx.send("I need 2 things to choose from ")
    if not args:
        return await ctx.send("I need things to choose from")
    em = discord.Embed(title='I choose.... ', description=random.choice([stuff, args]), colour=discord.Colour.blue ())
    await ctx.send(embed=em)    

@bot.command()
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour.red())
    embed.set_author(name='Page 1')
    embed.add_field(name='j!help/j!help2', value='Shows all commands on the given page', inline=False)
    embed.add_field(name='j!say (something)', value='Says anything.', inline=False)
    embed.add_field(name='j!kick (user)', value='Kicks the mentioned user', inline=False)
    embed.add_field(name='j!dmme', value='Sends you a nice dm to say hi.', inline=False)
    embed.add_field(name='j!blend', value='Returns a message.', inline=False)
    embed.add_field(name='j!clear (value)', value='Clears the given amount of messages.', inline=False)
    embed.add_field(name='j!mix (something)(something else)', value='Mixes the given words.', inline=False)
    embed.add_field(name='j!antimix (something)(something else)', value='AntiMixes the given words.', inline=False)
    embed.add_field(name='j!embed (something)', value='Says anything but in embed.', inline=False)
    embed.add_field(name='j!server', value='Sends the support server link', inline=False) 
    await ctx.send(embed=embed)

@bot.command()
async def help2(ctx):
    embed = discord.Embed(colour=discord.Colour.orange())
    embed.set_author(name='Page 2') 
    embed.add_field(name='j!role (user) (role)', value='If a user has a role, it is removed.If not, it is added.', inline=False)
    embed.add_field(name= 'j!truefalse (something)', value='Detects if you are lying.', inline=False)
    embed.add_field(name= 'j!choose (something) (something else) ', value='Chooses one of 2 things.', inline=False)
    embed.add_field(name= 'j!invite', value='Sends the bot invite link', inline=False)
    embed.add_field(name= 'j!ping', value='Sends a 90% copied ping cmd', inline=False)
    embed.add_field(name= 'j!mute', value='Gives someone the "muted" role. ', inline=False)
    embed.add_field(name= 'j!serverinfo', value='Gives the server\'s info. ', inline=False)
    await ctx.send(embed=embed)

bot.run(os.getenv("TOKEN"))
