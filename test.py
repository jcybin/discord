from dotenv import load_dotenv
import os
import discord
from discord import app_commands
from discord.ext import commands
import random
import mistral

load_dotenv()
KEY= os.getenv("KEY")

gifs = [
    "https://tenor.com/view/cat-gif-24925438", # police cat
    'https://tenor.com/view/fly-gif-21341388', # flying cat
    "https://tenor.com/view/cat-kitty-smoking-blunt-blehskibidi-gif-4336732105413285679", # smoking cat
    "https://tenor.com/view/cat-sad-vacuum-cleaner-robot-helpless-gif-16172119984579874863", # roomba run over cat
    "https://tenor.com/view/lenny-confetti-kitty-kitten-cat-cat-wiggle-gif-3410022925973943926" # useless 
]


intent = discord.Intents.default()
intent.message_content = True

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intent)

    async def on_ready(self):
        await self.tree.sync()  # sync global commands
        self.previous_gif = None
        

        

bot = Bot()

@bot.command(name="cat")
async def cat(ctx):
    while(1):
        gif_index = random.randint(0, len(gifs) - 1)
        if(bot.previous_gif == None or bot.previous_gif != gif_index):
            bot.previous_gif = gif_index
            break

    print(gif_index)
    await ctx.send(gifs[gif_index])


# Example for slash(/) commands 
"""
@bot.tree.command()
async def say_hi(interaction: discord.Interaction):
    while(1):
        gif_index = random.randint(0, len(gifs))
        if(bot.previous_gif == None or bot.previous_gif != gif_index):
            bot.previous_gif = gif_index
            break

    print(gif_index)
    await interaction.response.send_message(gifs[gif_index])
"""

bot.run(KEY)