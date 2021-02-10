import discord
import os
import threading
from keep_alive import keep_alive
from discord.ext import commands, tasks
import logging
from itertools import cycle
from datetime import datetime
import time
import dbl


now = datetime.now()

current_time = now.strftime("%H:%M:%S")

client = discord.Client()

status = cycle(["Among Us on Discord! | Run $help or $commands for help!","https://bazbots.github.io/Impostor-Bot/ | Run $website to gain a link!", "Happy Valentines Day! | Run $help or $commands for help!", "Version 1.2.2!", "Vote for us here at https://top.gg/bot/759436027529265172", "The GitHub Repository - $github for a link!"])

#f"Among Us in {len(client.guilds)} servers!"

@tasks.loop(seconds=600)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))
  print ("Successfully changed status!")

BOTVERSION = "1.2.2"


@client.event
async def on_ready():
    print("Loading...")
    time.sleep(3)
    print('Successfully booted {0.user}\nVersion 1.2.2'.format(client))
    time.sleep(2)
    print("Booted at", current_time)
    time.sleep(2)
    change_status.start()
    



logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
    
@client.event
async def on_dbl_vote(data):
    print(data)



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$help'):
        await message.channel.send('Need help? Join my support server!\nhttps://discord.gg/Sun4mtFjwE\nOr you can run $commands to get help with commands!')
    if message.content.startswith("$invite"):
      await message.channel.send(":incoming_envelope:Invite me here!:incoming_envelope:\n https://discord.com/api/oauth2/authorize?client_id=759436027529265172&permissions=217579073&redirect_uri=https%3A%2F%2Fdiscord.gg%2FnzsyDWg&scope=bot")
    if message.content.startswith("$about"):
      await message.channel.send(":question:A bit about The Impostor:question:\n\n:lock:100% Safe and Secure:lock:\n:england:English:england:\n:white_check_mark:Sus:white_check_mark:\n:spy:Impossible for Data Breaching:spy:\n:gift:Celebrating Events All Year Round!:gift:")
    if message.content.startswith("$commands"):
      await message.channel.send(":robot:Current Commands::robot:\nUse prefix `$`\nhelp\nabout\ninvite\nversion\nprefix\nwebsite\nvote\nservers\ncreator\ngithub\n\n\nSpecial Commands:\nUse the prefix `g$` for these commands\nevent")
    if message.content.startswith("$version") :
      await message.channel.send(":rocket:Current Version::rocket:\n`1.2.2`\n\n\n:inbox_tray:What's new to this update::inbox_tray:\n:white_check_mark:Edited a status\n:white_check_mark:Changed the Website command and address\n:white_check_mark:Updated the Impostor Website\n\n:clock3:What is still to come::clock3:\n:clock3:Solo Mode Among Us\n:clock3:Fixing the guild status issue\n\n:outbox_tray:What we removed::outbox_tray:\n:x:Nothing!")
    if message.content.startswith("$prefix"):
      await message.channel.send(":gear:We need a Database to change the prefix, it is something we will work on and will be released in a future update!\nUntil then, use the prefix $ or g$ for special commands!:gear:")
    if message.content.startswith("$website"):
      await message.channel.send(":desktop:Here is my Website::desktop:\nhttps://bazbots.github.io/Impostor-Bot/")
    if message.content.startswith("$vote"):
      await message.channel.send(":arrow_up:The bot is awaiting verification and can been found here::arrow_up:\nhttps://top.gg/bot/759436027529265172")
    if message.content.startswith("$servers"):
      await message.channel.send(f"Currently playing Among Us in {len(client.guilds)} servers!")
    if message.content.startswith("$creator"):
      await message.channel.send(":placard:The Impostor was a bot created by Baz!:placard:\n:one:This is actually his first ever coded bot!:one:\n:snake:It is a discord.py bot!:snake:\n:warning:The bot is not complete yet!:warning:\n:sparkling_heart:Show some love and join his server!:sparkling_heart:\n:calling: https://discord.gg/5jKA9kj :calling:")
    if message.content.startswith("g$event"):
      await message.channel.send(":calendar:Current Event is::calendar:\n:heart:Valentines Day!:heart:\n\n:sparkling_heart:Happy Valentines Day!:sparkling_heart:\n\nThe next event is...\n:woman:Mothers Day!:woman:")
    if message.content.startswith("$github"):
      await message.channel.send(":file_folder:Oke doke!:file_folder:\n:open_file_folder:Here is my GitHub Repo!:open_file_folder:\nhttps://github.com/Bazbots/Impostor-Bot")



keep_alive()
client.run(os.getenv("TOKEN"))
