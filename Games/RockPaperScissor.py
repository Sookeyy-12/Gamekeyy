import discord
from discord.ext import commands
import random

class RockPaperScissor(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    # Rock Paper Scissors
    @commands.command(name='playrps')
    async def rps(self, ctx):
        """ Play a game of Rock, Paper, Scissors with Bot """
        message = await ctx.channel.send('Choose one from Rock, Paper, Scissors')
        choices = ['🧱', '📄', '✂️']
        for choice in choices:
            await message.add_reaction(choice)
        bot_choice = random.choice(choices)
        reaction, user = await self.bot.wait_for('reaction_add', check= lambda r, u: u == ctx.author and r.message == message)
        if reaction.emoji == '🧱' and bot_choice == '✂️':
            result = await ctx.send(f'{ctx.author.mention} You **Won**! I chose {bot_choice}')
            await result.add_reaction('♻️')
        elif reaction.emoji == '📄' and bot_choice == '🧱':
            result = await ctx.send(f'{ctx.author.mention} You **Won**! I chose {bot_choice}')
            await result.add_reaction('♻️')
        elif reaction.emoji == '✂️' and bot_choice == '📄':
            result = await ctx.send(f'{ctx.author.mention} You **Won**! I chose {bot_choice}')
            await result.add_reaction('♻️')
        elif reaction.emoji == bot_choice:
            result = await ctx.send(f'{ctx.author.mention} Its a **Draw**! I chose {bot_choice} too!')
            await result.add_reaction('♻️')
        else:
            result = await ctx.send(f'{ctx.author.mention} You **Lost**... I chose {bot_choice}')
            await result.add_reaction('♻️')
        reaction, user = await self.bot.wait_for('reaction_add', check= lambda r, u: u == ctx.author and r.message == result)
        if reaction.emoji == '♻️':
            await message.delete()
            await result.delete()
            await ctx.invoke(self.bot.get_command('playrps'))

def setup(bot):
    bot.add_cog(RockPaperScissor(bot))
