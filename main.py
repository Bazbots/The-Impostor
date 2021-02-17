import discord
import os
import threading
from keep_alive import keep_alive
from discord.ext import commands, tasks
import logging
from itertools import cycle
from datetime import datetime
import time
import asyncio
import dbl
from discord import utils, Client
from discord import Member as DiscordMember
from discord.ext.commands import Bot, Greedy
from discord.ext.commands import BadArgument, CommandNotFound, MissingRequiredArgument
from replit import db

#bot = commands.Bot(command_prefix='$')
"""#ping command
@bot.command(help="Gives you a response time from the bot API",
             brief="Tests Bot Latency")
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f"Bot Latency is {latency} ms, "+ctx.message.author.mention)"""

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

client = discord.Client()

status = cycle([
    "Among Us on Discord! | Run $help or $commands for help!",
    "https://bazbots.github.io/Impostor-Bot/ | Run $website to gain a link!",
    "Happy Mother's Day! | Run $help or $commands for help!",
    "Version 1.2.8!",
    "Vote for us here at https://top.gg/bot/759436027529265172",
    "The GitHub Repository | $github for a link!", "In MAXIMUM Servers | Join our Support Server For more Information", "What do you think? | Run $feedback"])

#f"Among Us in {len(client.guilds)} servers!"


@tasks.loop(seconds=600)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))
	print("Successfully changed status!")


BOTVERSION = "1.2.8"


@client.event
async def on_ready():
	print("Loading...")
	time.sleep(3)
	print('Successfully booted {0.user}\nVersion 1.2.8'.format(client))
	time.sleep(2)
	print("Booted at", current_time)
	time.sleep(2)
	change_status.start()


Gold_Tier = bool
Diamond_Tier = bool
Basic_Tier = bool

@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(":mailbox:Hi there!:mailbox:\n\n:exclamation:I am the Impostor - a bot created by Baz!:exclamation:\n\n:incoming_envelope:You can join my support server by running $help!:incoming_envelope:\n\n:information_source:Also, you can view all commands by running $commands!:information_source:\n\n:partying_face:Have fun!:partying_face:")
        break



@client.event
async def on_dbl_vote(data):
	print(data)


"""@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command(name="feedback", description="Write feedback for the bot here!")
async def feedback(self, ctx):
  await ctx.message.delete()
  embed = discord.Embed(
    title="Please answer the folloing questions about the bot:",
    description="1.Why did you add this bot?\n2.Did you get what you wanted with the bot?"
  )
  sent = await ctx.send(embed=embed)

  try:
    msg = self.bot.wait_for(
      "message",
      timeout="10",
      check=lambda message: message.author == ctx.author
                            and message.channel == ctx.channel
    )
    if msg:
      await sent.delete()
      await msg.delete()
      await ctx.send("Thanks!\nYour response has been submitted")
      #print("{.author} said" + )
  except asyncio.TimeoutError:
    await sent.delete()
    await ctx.send("Timeout Error\nCancelled due to inactivity (5 minutes)", delete_after=15)"""


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith('$help'):
		await message.channel.send('Need help? Join my support server!\nhttps://discord.gg/Sun4mtFjwE\nOr you can run $commands to get help with commands!')
	if message.content.startswith("$invite"):
		await message.channel.send(":incoming_envelope:Invite me here!:incoming_envelope:\n https://discord.com/api/oauth2/authorize?client_id=759436027529265172&permissions=217579073&redirect_uri=https%3A%2F%2Fdiscord.gg%2FnzsyDWg&scope=bot")
	if message.content.startswith("$about"):
		await message.channel.send(":question:A bit about The Impostor:question:\n\n:lock:100% Safe and Secure:lock:\n:england:English:england:\n:white_check_mark:Sus:white_check_mark:\n:spy:Impossible for Data Breaching:spy:")
	if message.content.startswith("$commands"):
		await message.channel.send(":robot:Current Commands::robot:\nUse prefix `$`\nhelp\nabout\ninvite\nversion\nfeedback\nwebsite\nvote\nservers\ncreator\ngithub\ntier")
	if message.content.startswith("$version"):
		await message.channel.send(":rocket:Current Version:::\n`1.2.8`\n\n\n:inbox_tray:What's new to this update::inbox_tray:\n:white_check_mark:Added a message when the bot joins a server!\n\n:clock3:What is still to come::clock3:\n:clock3:Solo Mode Among Us\n:clock3:Fixing the guild status issue\n\n:outbox_tray:What we removed::outbox_tray:\n:x:The upgrade command\n:x:The Prefix command")
	if message.content.startswith("$website"):
		await message.channel.send(":desktop:Here is my Website::desktop:\nhttps://bazbots.github.io/Impostor-Bot/")
	if message.content.startswith("$vote"):
		await message.channel.send(":arrow_up:The bot can been found here::arrow_up:\nhttps://top.gg/bot/759436027529265172")
	if message.content.startswith("$servers"):
		await message.channel.send(f"Currently playing Among Us in **{len(client.guilds)}** servers!")
	if message.content.startswith("$creator"):
		await message.channel.send(":placard:The Impostor was a bot created by Baz!:placard:\n:one:This is actually his first ever coded bot!:one:\n:snake:It is a discord.py bot!:snake:\n:warning:The bot is not complete yet!:warning:\n:sparkling_heart:Show some love and join his server!:sparkling_heart:\n:calling: https://discord.gg/5jKA9kj :calling:")
	if message.content.startswith("$github"):
		await message.channel.send(":file_folder:Oke doke!:file_folder:\n:open_file_folder:Here is my GitHub Repo!:open_file_folder:\nhttps://github.com/Bazbots/Impostor-Bot")
	if message.content.startswith("$tier"):
		await message.channel.send(":free:You are in `Basic` Tier!:free:\nThis is Tier `1` out of 3!\n:free:Basic:free:\n:coin:Gold:coin:\n:gem:Diamond:gem:\n:question:What you can do at `Basic` Tier::question:\n:white_check_mark:Use all Basic commands (all under basic in $commands)\n:white_check_mark:You have access to certain modes (Standard and Crazy Colours)\n\n:coin:What you get when you reach `Gold` Tier::coin:\n:coin:Access to most modes(To be added soon)\n:coin:Multiplayer Mode\n:coin:A 10% higher chance of being Impostor\n\n:gem:What you get at `Diamond` Tier::gem:\n:gem:Access to all modes, even before they are released!\n:gem:25% higher chance of being Impostor\n:gem:Able to suggest modes for the bot!\n\n\n:crown:Soon, you will be able to unlock the other tiers!\n\nHey, you can unlock these tiers from giveaways on our support server!\nhttps://discord.gg/Sun4mtFjwE")
	if message.content.startswith("$feedback"):
	  await message.channel.send(":pencil:Please answer this short survey to let us know how you feel about the bot::pencil:\nhttps://docs.google.com/forms/d/e/1FAIpQLSeS_fcVh5_GRBmYCFw5qkxU29lSLU1zsTkioePy7Kp8roTVig/viewform?usp=sf_link")







keep_alive()
client.run(os.getenv("TOKEN"))
