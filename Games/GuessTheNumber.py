import discord
from discord.ext import commands
import random
import asyncio

class GuessingGame(commands.Cog):
    """Guess The Number!"""
    def __init__(self,bot):
        self.bot = bot

    # Guessing Game
    @commands.command()
    async def guess(self, ctx, x=None, y=None):
        """ Guess a Number from a Range provided by the user. Usage: !guess <min> <max> """ 
        if x is None or y is None :
            x = 0
            y = 10
        elif (int(y) - int(x)) > 1001:
            await ctx.channel.send('Range too big, Please Reduce the Range.')
        elif (int(y)-int(x)) <= 1001:
            await ctx.channel.send(f'Guess a Number from {int(x)} to {int(y)}.')
            answer = random.randint(int(x),int(y))
            attempt = 0
            while True:
                attempt += 1
                try:
                    guess = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=10.0)
                except asyncio.TimeoutError:
                    return await ctx.channel.send(f'Sorry, You took too long, it was {answer}.')
                if int(attempt) == 15:
                    await ctx.channel.send(f'You took too many attempts, the answer was {answer}!')
                    break
                elif int(guess.content) < answer:
                    await ctx.channel.send('The Number should be Bigger!')
                elif int(guess.content) > answer:
                    await ctx.channel.send('The Number should be Smaller!')
                elif int(guess.content) == answer:
                    await ctx.channel.send(f'Bingo! You guess the number in {attempt} attempt(s)')
                    break

def setup(bot):
    bot.add_cog(GuessingGame(bot))