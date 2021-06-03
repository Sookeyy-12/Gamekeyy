import discord
from discord.ext import commands
import os
from discord.ext.commands import context
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='g!',intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.online, activity = discord.Game('Something that you can\'t play. Nub'))

extensions = ['Games.GuessTheNumber',
            'Games.RockPaperScissor']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

bot.run(os.getenv('DISCORD_TOKEN'))