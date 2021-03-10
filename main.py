"""
Copyright (c) Baz 2021 Impostor Bot - Among Us Bot for Discord
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


now = datetime.now()

boot_time = now.strftime("%H:%M:%S")

client = commands.Bot(command_prefix="$")
client.remove_command("help")


version = "1.4.6"

@client.event
async def on_guild_join(guild):
	print(Fore.GREEN + f"I have joined {guild}")
	print(Fore.RESET)
	for channel in guild.text_channels:
		if channel.permissions_for(guild.me).send_messages:
			await channel.send(f":mailbox:Hi there!:mailbox:\n\n:exclamation:I am the Impostor - a bot created by Baz!:exclamation:\n\n:incoming_envelope:You can join my support server by running $help! and you can view all of my commands here as well!:incoming_envelope:\n\n:partying_face:Have fun!:partying_face:\n\n\n:information_source:When you added this bot, it was in version {version}:information_source:")
		break


@client.event
async def on_guild_remove(guild):
	print(Fore.GREEN + f"I have left {guild}")
	print(Fore.RESET)



status = cycle([
    "Among Us on Discord! | Run $help or $commands for help!",
    "https://bazbots.github.io/Impostor-Bot/ | Run $website to gain a link!",
    "Happy Mother's Day!",
    "Version 1.4.6!",
    "Vote for the bot here at https://top.gg/bot/759436027529265172",
    "The GitHub Repository | $github for a link!",
    "In MAXIMUM Servers | Join our Support Server For more Information",
    "What do you think? | Run $feedback", "$help, $invite"
])


@tasks.loop(seconds=600)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))
	print(Fore.GREEN + "Successfully changed status!")



@client.event
async def on_ready():
	print(Fore.BLUE + 'Successfully booted {0.user}\nVersion 1.4.6'.format(client))
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

global ghostmode_on
ghostmode_on = False

global dead_members
dead_members = []

global in_discussion
in_discussion = False

global leader
leader = None


@client.command()
async def host(ctx):
  global leader
  if leader == None:
      leader = ctx.author
      await ctx.send(f"```[!] Host connected: {ctx.author.name}```")
  elif leader != None and leader != ctx.author:
      await ctx.send(f"```[!] {leader} is already hosting, they can disconnect by typing $host again```")
  else:
      await ctx.send(f"```[!] Host has disconnected: {ctx.author.name}```")
      leader = None

@client.command()
async def users(ctx):
  global leader

  if leader == None:
      await ctx.send("[!] There is currently no host, use $host to host a game")
  else:
      string = f"[!] Current connected users: \n{leader}\n"

      for member in list(client.get_channel(leader.voice.channel.id).members):
          string = string + f"- {member}\n"

      await ctx.send(f"```{string}```")

@client.command()
async def mute(ctx):
  global leader
  global ghostmode_on

  global in_discussion
  in_discussion = False
  try:
      if ctx.author != leader:
          await ctx.send("```[!] Only the host can use this command```")
  except: pass

  try:
      for member in list(client.get_channel(leader.voice.channel.id).members):
          if member.id in dead_members and ghostmode_on:
              await member.edit(mute = False)
          elif member.id not in dead_members and ghostmode_on:
              await member.edit(deafen = True, mute = True)
          else:
              await member.edit(mute = True)

  except AttributeError as e:
      print("[!] A host must first connect by using the $host command")

@client.command()
async def unmute(ctx):
  global leader
  global dead_members
  global ghostmode_on
  global in_discussion
  in_discussion = True
  try:
      if ctx.author != leader:
          await ctx.send("```[!] Only the host can use this command```")
  except: pass

  try:
      for member in list(client.get_channel(leader.voice.channel.id).members):
          if member.id in dead_members and ghostmode_on:
              await member.edit(mute = True)
          elif member.id in dead_members and ghostmode_on == False:
              await member.edit(mute = True)
          elif member.id not in dead_members and ghostmode_on:
              await member.edit(deafen = False, mute = False)
          else:
              await member.edit(mute = False)

  except AttributeError:
      print("[!] There is no host found, connect using $host")


@client.command()
async def dead(ctx):
  global dead_members
  global ghostmode_on

  if ghostmode_on:
      await ctx.author.edit(mute = False, deafen = False)
  else:
      await ctx.author.edit(mute = True)

  if ctx.author.id not in dead_members:
      dead_members.append(ctx.author.id)

@client.command()
async def game_mute(ctx, *members: discord.Member):
    global dead_members
    global ghostmode_on
    global leader

    for member in members:
        if member not in list(client.get_channel(leader.voice.channel.id).members):
            await ctx.send(f"[!] {member} is not in game")
            continue
        try:
            if ghostmode_on and in_discussion:
                await member.edit(mute = True)
                valid = True
            if ghostmode_on and in_discussion == False:
                await member.edit(mute = False, deafen = False)
                valid = True
            else:
                await member.edit(mute = True)
                valid = True
        except Exception as e:
            print(e)
            await ctx.send(f"[!] Invalid user: {member}")
            valid = False

        if valid:
            if member.id not in dead_members:
                dead_members.append(member.id)
        print(dead_members)

async def ghostmode(ctx):
    global ghostmode_on

    if ctx.author != leader:
        await ctx.send("```[!] Only the host can use this command```")
    else:
        if ghostmode_on == False:
            ghostmode_on = True
            await ctx.send("```[!] You have entered ghostmode```")
        else:
            ghostmode_on = False
            await ctx.send("```[!] You are no longer in ghostmode```")



keep_alive()
client.run(os.getenv("TOKEN"))
