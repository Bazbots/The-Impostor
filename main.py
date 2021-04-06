"""
Copyright © Baz 2021 The Impostor - Among Us Bot for Discord
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
from discord import utils, Client
from discord import Member as DiscordMember
from colorama import Fore
from replit import db
import random

now = datetime.now()

boot_time = now.strftime("%H:%M:%S")

client = commands.Bot(
    command_prefix=["$", "<@759436027529265172> ", "<@759436027529265172>"])
client.remove_command("help")

__version__ = "1.5.5"


@client.event
async def on_guild_join(guild):
	with open('impostor_thumbnail.png', 'r') as f:
		picture = discord.File(f)
	print(Fore.GREEN + f"I have joined {guild}" + Fore.RESET)
	for channel in guild.text_channels:
		if channel.permissions_for(guild.me).send_messages:
			embedHi = discord.Embed(
			    title=":mailbox:Hi there!:mailbox:",
			    description=
			    f"<:impostor:774673531786625024>I am the Impostor - a bot created by Baz!<:impostor:774673531786625024>\n\n:incoming_envelope:You can join my support server by running $help and you can view all of my commands here as well!:incoming_envelope:\n\n:partying_face:Have fun!:partying_face:\n\n\n:information_source:When you added this bot, it was in version {__version__}:information_source:",
			    colour=discord.Colour.red())
			embedHi.set_thumbnail(
			    url=
			    "https://cdn1.iconfinder.com/data/icons/logos-brands-in-colors/231/among-us-player-red-512.png"
			)
			embedHi.set_footer(
			    text="© Baz - The Impostor - Among Us bot for Discord")
			await channel.send(embed=embedHi)
			await channel.send(file=picture)
		break


@client.event
async def on_guild_remove(guild):
	print(Fore.GREEN + f"I have left {guild}")
	print(Fore.RESET)


status = cycle([
    "Among Us on Discord! | $help, $info",
    "https://bazbots.github.io/The-Impostor | $info", "Happy Easter!",
    f"Version {__version__} | $version",
    "Vote for the bot here at https://top.gg/bot/759436027529265172 | $info",
    "The GitHub Repository | $info", "What do you think? | $feedback",
    "$help, $info", "Use the prefix $ or @The Impostor"
])


@tasks.loop(seconds=600)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))
	print(Fore.GREEN + "Successfully changed status!")


@client.event
async def on_ready():
	print(Fore.BLUE +
	      f'Successful login to {client.user}\nVersion {__version__}')
	print("Remember to add one hour to this:\nStarted at", boot_time)
	change_status.start()


@client.command()
async def servers(ctx):
	embedSeven = discord.Embed(
	    title="Current Servers",
	    description=
	    f"Currently playing Among Us in **{len(client.guilds)}** servers!",
	    colour=discord.Colour.red())
	embedSeven.set_thumbnail(
	    url=
	    "https://cdn1.iconfinder.com/data/icons/logos-brands-in-colors/231/among-us-player-red-512.png"
	)
	embedSeven.set_footer(
	    text="© Baz - The Impostor - Among Us bot for Discord")
	await ctx.send(embed=embedSeven)


@client.command()
async def ping(ctx):
	await ctx.send(f"Pong!\nYour ping is {round(client.latency * 1000)}!")


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
