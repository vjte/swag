import json
import discord
import aiohttp
import asyncio
import datetime
from discord import Embed
from discord.ext import commands, tasks
import os






config = json.load(open("config/config.json", encoding="UTF-8"))





class grave(commands.AutoShardedBot):
    def __init__(self, **kwargs):
        super().__init__(
            command_prefix=",",
            intents=discord.Intents.all(),
            help_command=None,
            case_insensitive=True,
            allowed_mentions=discord.AllowedMentions.none(),
            strip_after_prefix=True,
            owner_ids=[],
        )

    async def on_connect(self):
        print("Connecting To Grave...")
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                try:
                    await bot.load_extension("cogs." + file[:-3])
                    print("loaded extension {}".format(file[:-3]))
                except Exception as e:
                    print("unable to load extension {} - {}".format(file[:-3], e))
    
bot = grave()
bot.run(str(config["token"]))