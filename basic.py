import discord
from discord.ext import commands
from colorama import Fore
from datetime import datetime

now = datetime.now()

boot_time = now.strftime("%H:%M:%S")

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
	  await ctx.send("Need help? Join my support server!\nhttps://discord.gg/Sun4mtFjwE\nOr you can view all the current commands below!\n\n\n:robot:Current Commands::robot:\nUse prefix `$`\nhelp\nabout\ninvite\nversion\nfeedback\nwebsite\nvote\ncreator\ngithub\ntier {current/basic/gold/diamond}\nping\neject {user} {role}\nsus\nkill {username}")

  @commands.command()
  async def invite(self, ctx):
	  await ctx.send(":incoming_envelope:Invite me here!:incoming_envelope:\n https://discord.com/api/oauth2/authorize?client_id=759436027529265172&permissions=8&redirect_uri=https%3A%2F%2Fbazbots.github.io%2FImpostor-Bot&response_type=code&scope=identify%20email%20bot")
      
  @commands.command()
  async def about(self, ctx):
	  await ctx.send(":question:A bit about The Impostor:question:\n\n:lock:100% Safe and Secure:lock:\n:england:English:england:\n:white_check_mark:Sus:white_check_mark:\n:spy:Impossible for Data Breaching:spy:")
  
  @commands.command()
  async def version(self, ctx):
	  await ctx.send("VERSION 1.4.6: THE BIGGEST UPDATE SO FAR\n\nWhat we have added:\n:white_check_mark:Host/mute/unmute/dead/game_mute (Special Thanks to alpharaoh for some help on the code)\nRun $host to start a game")
  
  @commands.command()
  async def website(self, ctx):
	  await ctx.send(":desktop:Here is my Website::desktop:\nhttps://bazbots.github.io/Impostor-Bot/")

  @commands.command()
  async def github(self, ctx):
	  await ctx.send(":file_folder:Oke doke!:file_folder:\n:open_file_folder:Here is my GitHub Repo!:open_file_folder:\nhttps://github.com/Bazbots/Impostor-Bot")

  @commands.command()
  async def creator(self, ctx):
	  await ctx.send(":placard:The Impostor was a bot created by Baz!:placard:\n:one:This is actually his first ever coded bot!:one:\n:snake:It is a discord.py bot!:snake:\n:warning:The bot is not complete yet!:warning:\n:sparkling_heart:Show some love and join his server!:sparkling_heart:\n:calling: https://discord.gg/5jKA9kj :calling:")

  @commands.command()
  async def feedback(self, ctx):
	  await ctx.send(":pencil:Please answer this short survey to let us know how you feel about the bot::pencil:\nhttps://docs.google.com/forms/d/e/1FAIpQLSeS_fcVh5_GRBmYCFw5qkxU29lSLU1zsTkioePy7Kp8roTVig/viewform?usp=sf_link")





def setup(client):
  client.add_cog(Basic(client))
