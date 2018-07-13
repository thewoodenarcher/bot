import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

bot = discord.bot()
bot = commands.Bot(command_prefix = "j!")
bot.remove_command('help')

@bot.command(pass_context=True)
async def spamme(ctx):
	author = ctx.message.author
	
	embed = discord.Embed(
		colour = discord.Colour.orange()
		)
	

	embed.set_author(name='spamme') 		
	embed.add_field(name='Spam', value= 'Spam', inline=False)

	await ctx.author.send(embed=embed)

	await ctx.author.send(embed=embed)

	await ctx.author.send(embed=embed)


	await ctx.author.send(embed=embed)


	await ctx.author.send(embed=embed)

	await ctx.author.send(embed=embed)
	
	
	await ctx.author.send(embed=embed)
	
	await ctx.author.send(embed=embed)
	
			
		
	await ctx.author.send(embed=embed)	
        
@bot.event 
async def on_ready():
    print("Bot is online and connected to Discord")
 
 
@bot.command(pass_context=True)
async def role(ctx, userName: discord.Member, role: discord.Role = None):

    if role is None:
        return await ctx.send("You haven't specified a role! ")
    if role not in ctx.message.server.roles:
        return await ctx.send("That role doesn't exist.")
    for server_role in ctx.message.server.roles:
        if server_role.id == role.id:
            if role not in userName.roles:
                await bot.add_roles(userName, role)
                return await ctx.send("{} role has been added to {}.".format(role, userName.mention))
    if role in userName.roles:
        await bot.remove_roles(userName, role)
        return await ctx.send("{} role has been removed from {}."
                                .format(role, userName.mention))
@bot.command (pass_context=True)
@commands.has_permissions (kick_members=True )
async def kick(ctx, userName: discord.User ):
	await bot.kick(userName)
	await ctx.send("Successfully commited die.")
     
@bot.command()
async def mix(word1, word2):
	await ctx.send(word1[:int(len(word1)/2)]  + word2[int(len(word2)/2):])

@bot.command()
async def antimix(word1, word2):
	await ctx.send(word1[
		int(len(word1)/2):]  + word2[:int(len(word2)/2)])
    
            
@bot.command( )
async def blend():
	await ctx.send("**_WRRRRRRRRRRRRRR_**")



@bot.command()
async def say(*args):
	output = ' '
	for word in args:
		output += word
		output += ' '
	await ctx.send(output)
@bot.command()
async def embed (*sth):
	output = ' '
	for word in sth:
		output += word
		output += ' '
		embed = discord.Embed(title="You said:", description= (output), color=000000)
	await ctx.send( embed=embed)

	
			
@bot.command(pass_context=True)
async def clear(ctx, amount=100):
	channel = ctx.message.channel
	messages = [ ]
	async for message in bot.logs_from(channel, limit=int(amount)):
		messages.append(message)
	await bot.delete_messages(messages)
	await ctx.send('OOF messages')

@bot.command(pass_context=True)
async def help(ctx):
	author = ctx.message.author
	
	embed = discord.Embed(
		colour2 = discord.Colour.red
		)
	 
		
	embed.set_author(name='Page 1') 		
	embed.add_field(name='j!help (page)', value= 'Shows all commands on the given page', inline=False)
	
	
	embed.add_field(name='j!say (something)', value= 'Says anything.', inline=False)
	

	embed.add_field(name='j!kick (user)', value= 'Kicks the mentioned user', inline=False)	

	embed.add_field(name='j!spamme', value= 'Spams you.Literally.', inline=False)
	
	embed.add_field(name='j!blend', value= 'Returns a message.', inline=False)
	embed.add_field(name='j!clear (value)', value= 'Clears the given amount of messages.', inline=False)

	embed.add_field(name='j!mix (something)(something else)', value= 'Mixes the given words.', inline=False)
	
	embed.add_field(name='j!antimix (something)(something else)', value= 'AntiMixes the given words.', inline=False)

	embed.add_field(name='j!embed (something)', value= 'Says anything but in embed.', inline=False)
	await ctx.author.send(embed=embed)
	

@bot.command(pass_context=True)
async def help2(ctx):
	author = ctx.message.author
	
	embed = discord.Embed(
		colour3 = discord.Colour.orange
		)
		
	embed.set_author(name='Page 2') 		
	embed.add_field(name='j!role (user) (role)', value= 'If a user has a role, it is removed.If not, it is added.', inline=False)
	await ctx.author.send(embed=embed)


bot.run(os.getnv("TOKEN"))