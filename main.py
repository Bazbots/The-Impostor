import discord
import os
import threading
import unittest
from keep_alive import keep_alive
from discord.ext import commands, tasks
from itertools import cycle
from datetime import datetime
import time
import asyncio
import dbl
from discord import utils, Client
from discord import Member as DiscordMember
from discord.ext.commands import BadArgument, CommandNotFound, MissingRequiredArgument
from colorama import Fore
from replit import db


now = datetime.now()

boot_time = now.strftime("%H:%M:%S")

client = commands.Bot(command_prefix="$")
client.remove_command("help")




@client.event
async def on_guild_join(guild):
	print(Fore.GREEN + f"I have joined {guild}")
	print(Fore.RESET)
	for channel in guild.text_channels:
		if channel.permissions_for(guild.me).send_messages:
			await channel.send(
			    ":mailbox:Hi there!:mailbox:\n\n:exclamation:I am the Impostor - a bot created by Baz!:exclamation:\n\n:incoming_envelope:You can join my support server by running $help! and you can view all of my commands here as well!:incoming_envelope:\n\n:partying_face:Have fun!:partying_face:"
			)
		break


@client.event
async def on_guild_remove(guild):
	print(Fore.GREEN + f"I have left {guild}")
	print(Fore.RESET)


status = cycle([
    "Among Us on Discord! | Run $help or $commands for help!",
    "https://bazbots.github.io/Impostor-Bot/ | Run $website to gain a link!",
    "Happy Mother's Day! | Run $help for help!", "Version 1.4.1!",
    "Vote for us here at https://top.gg/bot/759436027529265172",
    "The GitHub Repository | $github for a link!",
    "In MAXIMUM Servers | Join our Support Server For more Information",
    "What do you think? | Run $feedback"
])


@tasks.loop(seconds=600)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))
	print(Fore.GREEN + "Successfully changed status!")



@client.event
async def on_ready():
	print(Fore.BLUE + 'Successfully booted {0.user}\nVersion 1.4.1'.format(client))
	print("Booted at", boot_time)
	change_status.start()


@client.command()
async def servers(ctx):
	await ctx.send(f"Currently playing Among Us in **{len(client.guilds)}** servers!")

@client.command()
async def ping(ctx):
	await ctx.send(f"Pong!\nYour ping is {round(client.latency * 1000)}ms!")

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
