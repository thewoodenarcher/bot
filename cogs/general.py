import discord
from discord.ext import commands
from utils.paginator import Paginator
from utils.utils import _command_signature

class General:
    """Some general commands."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *, msg: commands.clean_content()):
        """Bot repeats what you say."""
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass
        finally:
            await ctx.send(msg)

    @commands.command()
    async def ping(self, ctx):
        """Checks if bot is working and measures websocket latency"""
        await ctx.send(f"Pong! WebSocket Latency: **{self.bot.latency * 1000:.4f} ms**")

    @commands.command()
    async def invite(self, ctx):
        """Want me in your server?"""
        await ctx.send(f"Invite me to your server: <https://discordapp.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot&permissions=470281463>")

    @commands.command(name="help", aliases=["h", "halp", "commands", "cmds"])
    async def _help(self, ctx, command: str = None):
        """Shows all commands"""
        prefix = list(filter(lambda x: x != ctx.bot.user.mention, await self.bot.get_prefix(ctx.message)))[0]
        if command:
            cmd = self.bot.get_command(command.lower()) or self.bot.get_cog(command)
            if not cmd:
                return await ctx.send(f"Command or category '{command}' not found.")
            if isinstance(cmd, commands.Command):
                em = discord.Embed(color=0xff0000)
                em.title = cmd.name
                em.description = cmd.help or "No Description"
                em.description += "\nUsage: `{}{}`".format(ctx.prefix, _command_signature(cmd))
                if cmd.aliases:
                    em.description += "\nAliases: `{}`".format(", ".join(cmd.aliases))
                return await ctx.send(embed=em)
            cmds = self.bot.get_cog_commands(command)
            em = discord.Embed(color=self.bot.color)
            em.description = cmd.__doc__ + "\n\n`" if cmd.__doc__ else "No Description\n\n`" 
            em.set_footer(text=f"{prefix}help <cmd> for more info on a command.")
            for x in cmds:
                msg = f"{prefix}{x.signature} {x.short_doc}\n"
                em.description += msg
            em.description += "`"
            return await ctx.send(embed=em)
        else:
            cogs = self.bot.cogs.keys()
            pages = []
            for x in cogs:
                if x == "Owner" and ctx.author.id not in ctx.bot.devs:
                    continue
                cmds = self.bot.get_cog_commands(x)
                cog = self.bot.get_cog(x)
                msg = cog.__class__.__name__ + "\n" + cog.__doc__ + "\n\n`" if cog.__doc__ else cog.__class__.__name__ + "\nNo Description\n\n`"
                for cmd in cmds:
                    if cmd.hidden:
                        continue
                    cmd_msg = f"{prefix}{_command_signature(cmd)} {cmd.short_doc}\n"
                    msg += cmd_msg
                msg += "`"
                pages.append(msg)
            em = discord.Embed(color=0xff0000)
            em.set_footer(text=f"{prefix}help <cmd> for more information on a command.")
            paginator = Paginator(ctx, pages=pages, page_count=True, embed=em)
            await paginator.run()

def setup(bot):
    bot.add_cog(General(bot))
