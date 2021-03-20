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
import json

sponsors = ["\n\nHey! You can join Fritzwinger's discord server here!\nhttps://discord.gg/wYC6dtUM5J", "\n\nHey! You can join Baz's discord server here!\nhttps://discord.gg/5jKA9kj", "\n\nHey! You should check out Milxq ok's channel!\nhttps://www.youtube.com/channel/UCA65XYkOjhXc1G3pko2bpbw", "", "", "", "", "", "", "", ""]

sponsor_owners = ["Fritzwinger", "Milxq ok", "Camila"]

now = datetime.now()

boot_time = now.strftime("%H:%M:%S")

client = commands.Bot(command_prefix="$")
client.remove_command("help")

__version__ = "1.5.0"

@client.event
async def on_guild_join(guild):
	print(Fore.GREEN + f"I have joined {guild}")
	print(Fore.RESET)
	for channel in guild.text_channels:
		if channel.permissions_for(guild.me).send_messages:
			await channel.send(f":mailbox:Hi there!:mailbox:\n\n:exclamation:I am the Impostor - a bot created by Baz!:exclamation:\n\n:incoming_envelope:You can join my support server by running $help! and you can view all of my commands here as well!:incoming_envelope:\n\n:partying_face:Have fun!:partying_face:\n\n\n:information_source:When you added this bot, it was in version {__version__}:information_source:")
		break


@client.event
async def on_guild_remove(guild):
	print(Fore.GREEN + f"I have left {guild}")
	print(Fore.RESET)


status = cycle([
    "Among Us on Discord! | $help, $host",
    "https://bazbots.github.io/Impostor-Bot/ | $website",
    "Happy Easter!",
    f"Version {__version__} | $version",
    "Vote for the bot here at https://top.gg/bot/759436027529265172 | $vote",
    "The GitHub Repository | $github", "What do you think? | $feedback", "$help, $invite", "$host to start a game!", f"With {random.choice(sponsor_owners)}! You can be a sponsor by running $sponsors"])

@tasks.loop(seconds=600)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))
	print(Fore.GREEN + "Successfully changed status!")


@client.event
async def on_ready():
	print(Fore.BLUE + f'Successfully booted {client.user}\nVersion {__version__}')
	print("Booted at", boot_time)
	change_status.start()


@client.command()
async def servers(ctx):
	await ctx.send(f"Currently playing Among Us in **{len(client.guilds)}** servers!{random.choice(sponsors)}")

@client.command()
async def ping(ctx):
	await ctx.send(f"Pong!\nYour ping is {round(client.latency * 1000)}ms!{random.choice(sponsors)}")

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
