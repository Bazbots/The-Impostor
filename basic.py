import discord
from discord.ext import commands
from colorama import Fore
from datetime import datetime
import random

now = datetime.now()

boot_time = now.strftime("%H:%M:%S")

sponsors = ["\n\nHey! You can join Fritzwinger's discord server here!\nhttps://discord.gg/wYC6dtUM5J", "\n\nHey! You can join Baz's discord server here!\nhttps://discord.gg/5jKA9kj", "\n\nHey! You should check out Milxq ok's channel! https://www.youtube.com/channel/UCA65XYkOjhXc1G3pko2bpbw", "", "", "", "", "", "", "", ""]


class Basic(commands.Cog):

  def __init__(self, client):
    self.client = client


  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
      await ctx.send(":x:Error:x:\n:information_source:Command is either in the command vault or does not exist")
      print(Fore.GREEN + f"Error: {error}")

  @commands.command()
  async def help(self, ctx):
	  await ctx.send("Need help? Join my support server!\nhttps://discord.gg/Sun4mtFjwE\nOr you can view all the current commands below!\n\n\n:robot:Current Commands::robot:\nUse prefix `$`\n\nInformative Commands:\nhelp\nabout\ninvite\nversion\nfeedback\nwebsite\nvote\ncreator\ngithub\nsponsors\nping\n\nFun Commands:\neject {user} {role}\nsus\nkill {username}\n\nGame Commands (Disabled):\nhost\nmute\nunmute\ndead\ngame_mute\nstart\n\nTasks:\nscan\ndownload\nweatherdownload\ninspect")

  @commands.command()
  async def invite(self, ctx):
	  await ctx.send(":incoming_envelope:Invite me here!:incoming_envelope:\n https://discord.com/api/oauth2/authorize?client_id=759436027529265172&permissions=8&redirect_uri=https%3A%2F%2Fbazbots.github.io%2FImpostor-Bot&response_type=code&scope=identify%20email%20bot")
      
  @commands.command()
  async def about(self, ctx):
	  await ctx.send(f":question:A bit about The Impostor:question:\n\n:lock:100% Safe and Secure:lock:\n:england:English:england:\n:white_check_mark:Sus:white_check_mark:\n:spy:Impossible for Data Breaching:spy:{random.choice(sponsors)}")
  
  @commands.command()
  async def version(self, ctx):
	  await ctx.send(f":rocket:Current Version::rocket:\n`1.5.0`\n\n\n:inbox_tray:What's new to this update::inbox_tray:\n:white_check_mark:$download, $weatherdownload, $inspect\n\n:clock3:What is still to come::clock3:\n:clock3:Fixing the servers I'm in status\n\n:outbox_tray:What we removed::outbox_tray:\n:x:Disabled host commands until further notice{random.choice(sponsors)}")

  @commands.command()
  @commands.is_owner()
  async def cv(self, ctx):
    await ctx.send(":rocket:Current Version::rocket:\n`1.5.0`\n\n\n:inbox_tray:What's new to this update::inbox_tray:\n:white_check_mark:$download, $weatherdownload, $inspect\n\n:clock3:What is still to come::clock3:\n:clock3:Fixing the servers I'm in status\n\n:outbox_tray:What we removed::outbox_tray:\n:x:Disabled host commands until further notice")

  
  @commands.command()
  async def website(self, ctx):
	  await ctx.send(f":desktop:Here is my Website::desktop:\nhttps://bazbots.github.io/Impostor-Bot/{random.choice(sponsors)}")

  @commands.command()
  async def github(self, ctx):
	  await ctx.send(f":file_folder:Oke doke!:file_folder:\n:open_file_folder:Here is my GitHub Repo!:open_file_folder:\nhttps://github.com/Bazbots/Impostor-Bot{random.choice(sponsors)}")

  @commands.command()
  async def creator(self, ctx):
	  await ctx.send(":placard:The Impostor was a bot created by Baz!:placard:\n:one:This is actually his first ever coded bot!:one:\n:snake:It is a discord.py bot!:snake:\n:warning:The bot is not complete yet!:warning:\n:sparkling_heart:Show some love and join his server!:sparkling_heart:\n:calling: https://discord.gg/5jKA9kj :calling:")

  @commands.command()
  async def feedback(self, ctx):
	  await ctx.send(":pencil:Please answer this short survey to let us know how you feel about the bot::pencil:\nhttps://docs.google.com/forms/d/e/1FAIpQLSeS_fcVh5_GRBmYCFw5qkxU29lSLU1zsTkioePy7Kp8roTVig/viewform?usp=sf_link LLP")
	  print(f"{ctx.author} has triggered the feedback command")
  
  @commands.command()
  async def sponsors(self, ctx):
    await ctx.send("Here are our current sponsors!\nTheir product will pop out throughout some of your commands!\n\nFritzwinger - Discord Server - https://discord.gg/wYC6dtUM5J\nCamila - YouTube Channel - https://www.youtube.com/channel/UCGQgRVgKexKmOfIA4lrFG9Q\nMilxq ok - YouTube channel - https://www.youtube.com/channel/UCA65XYkOjhXc1G3pko2bpbw\n\nHey, want to be a sponsor?\nFill out this form as to why you should be one!\nThere are now 0 slots left! The slots will reset after this month!\nhttps://forms.gle/vpY9PToyLoFYTQeaA")
    print(f"{ctx.author} pinged $sponsors")
  
  @commands.command()
  async def vote(self, ctx):
    await ctx.send(":arrow_up:You can vote for the bot here::arrow_up:\nhttps://top.gg/bot/759436027529265172/vote")





def setup(client):
  client.add_cog(Basic(client))
