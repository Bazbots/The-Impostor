"""
Copyright © Baz 2021 - The Impostor - Among Us Bot for Discord
"""
import discord
import os
import threading
import unittest
from keep_alive import keep_alive
from discord.ext import commands, tasks
from itertools import cycle
from datetime import datetime
import asyncio
import dbl
from colorama import Fore
from replit import db
import random
import json
import patreon



now = datetime.now()

boot_time = now.strftime("%H:%M:%S")

client = commands.Bot(
    command_prefix=["$", "<@759436027529265172>", "<@759436027529265172> ", "<@!759436027529265172>", "<@!759436027529265172> ", "<@&759436027529265172> ", "<@&759436027529265172>"], description="An Among Us bot for Discord!", case_insensitive=True)
client.remove_command("help")


__version__ = "X.X.X"


@client.event
async def on_guild_join(guild):
  print(Fore.GREEN + f"I have joined {guild}" + Fore.RESET)
  for channel in guild.text_channels:
    if channel.permissions_for(guild.me).send_messages:
      embedHi = discord.Embed(
			    title="Thanks for adding me!",
			    description=
			    f"<:impostor:774673531786625024>I am the Impostor - a bot created by Baz!<:impostor:774673531786625024>\n\n<:noice:751384305464377375>You can join my support server by running $help and you can view all of my commands here as well!<:noice:751384305464377375>\n\n<:patreon:839897502925062165> Feel free to go to https://www.patreon.com/theimpostor do gain access to cool premium commands! <:patreon:839897502925062165>\n:partying_face:Have fun!:partying_face:\n\n\n<:ping:757276110252670986>When you added this bot, it was in version {__version__}<:ping:757276110252670986>",
			    colour=discord.Colour.red())
      embedHi.set_thumbnail(
			    url=
			    "https://cdn1.iconfinder.com/data/icons/logos-brands-in-colors/231/among-us-player-red-512.png"
			)
      embedHi.set_image(url="https://cdn.discordapp.com/attachments/764132789670117406/833380621686145095/impostor_thumbnail.png")
      embedHi.set_footer(
			    text="© Baz - The Impostor - Among Us bot for Discord")
      await channel.send(embed=embedHi)
    break



@client.event
async def on_guild_remove(guild):
  print(Fore.GREEN + f"I have left {guild}" + Fore.RESET)





@client.event
async def on_ready():
  print(Fore.BLUE + f'Successful login to {client.user}\nVersion {__version__}\nBot is in {len(client.guilds)} servers\nClient ID: {client.user.id}\nRemember to add 1 hour to time: {boot_time}')
  change_status.start()

  

  

@tasks.loop(seconds=600)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))
  print(Fore.GREEN + "Successfully changed status!")


status = cycle(["Among Us on Discord! | $help, $info", "https://www.patreon.com/theimpostor | $patreon",
    "https://bazbots.github.io/The-Impostor | $info",
    f"Version {__version__} | $version",
    "Vote for the bot by running $vote {site} | $info",
    "The GitHub Repository | $info", "What do you think? | $feedback",
    "$help, $info", "Use the prefix $ or @The Impostor", "Created by Baz!"
])


@client.command()
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")
  


@client.command()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

keep_alive()
client.run(os.getenv("TOKEN"))
