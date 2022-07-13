import json
import time
import os

from discord.ext import commands
import discord

os.chdir("Json")

if __name__ == "__main__":
    token = json.load(open("Config.json"))["token"]

bot = commands.Bot()


@bot.event
async def on_ready():
    print("ready")


bot.run(token)