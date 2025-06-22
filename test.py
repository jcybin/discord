from dotenv import load_dotenv
import os
import discord
from discord import app_commands
from discord.ext import commands

load_dotenv()
KEY= os.getenv("KEY")

intent = discord.Intents.default()
intent.message_content = True

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intent)

    async def on_ready(self):
        await self.tree.sync()
        

        

bot = Bot()


@bot.tree.command()
async def say_hi(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hello {interaction.user.mention}')


bot.run(KEY)