from dotenv import load_dotenv
import os
import discord
from discord import app_commands
from discord.ext import commands
import random
import mistral

load_dotenv()
KEY= os.getenv("KEY")

intent = discord.Intents.default()
intent.message_content = True

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intent)

    async def on_ready(self):
        await self.tree.sync()  # sync global commands
        

bot = Bot()


async def chat_bot(user_input):
    mistral.history.append(f"Human: {user_input}")
    reply = mistral.chat()
    reply = reply.split("Human:")[0].strip()
    mistral.history.append(f"Assistant: {reply}")
    return reply


@bot.tree.command()
async def talk(interaction: discord.Interaction, text: str):
    await interaction.response.defer()
    response = await chat_bot(text)
    await interaction.followup.send(response)


bot.run(KEY)