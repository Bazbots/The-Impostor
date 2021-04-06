import discord
from discord.ext import commands
from colorama import Fore
from datetime import datetime
import random



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
    embedTwo = discord.Embed(
        title="Help",
        description="Join my support server here:\nhttps://discord.gg/Sun4mtFjwE\n\nUse the prefix `$` or `@The Impostor`",
        colour=discord.Colour.red()
      )
    embedTwo.add_field(name="Informative Commands",value="help\ninfo\nabout\nversion\nfeedback\ncreator\nping", inline=True)
    embedTwo.add_field(name="Fun commands", value="eject {user} {role}\nsus\nkill {username}\nvent\nsabotage", inline=True)
    embedTwo.add_field(name="Tasks", value="scan\ndownload\nweather\ninspect")
    embedTwo.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/logos-brands-in-colors/231/among-us-player-red-512.png")
    embedTwo.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    await ctx.send(embed=embedTwo)

  @commands.command()
  async def info(self, ctx):
    print(f"{ctx.author} has pinged the info command")
    embedTen = discord.Embed(
      title="Bot Information",
      colour=discord.Colour.red()
      )
    embedTen.add_field(name="Invite Link", value="https://discord.com/api/oauth2/authorize?client_id=759436027529265172&permissions=8&redirect_uri=https%3A%2F%2Fbazbots.github.io%2FThe-Impostor&response_type=code&scope=identify%20email%20bot%20applications.commands", inline=True)
    embedTen.add_field(name="Website", value="https://bazbots.github.io/The-Impostor", inline=True)
    embedTen.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/logos-brands-in-colors/231/among-us-player-red-512.png")
    embedTen.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    embedTen.add_field(name="Support Server Link:", value="https://discord.gg/Sun4mtFjwE", inline=True)
    embedTen.add_field(name="Voting link:", value="https://top.gg/bot/759436027529265172/vote", inline=True)
    embedTen.add_field(name="Github Repository", value="https://github.com/Bazbots/The-Impostor", inline=True)
    await ctx.send(embed=embedTen)
      
  @commands.command()
  async def about(self, ctx):
	  await ctx.send(":question:A bit about The Impostor:question:\n\n:lock:100% Safe and Secure:lock:\n:england:English:england:\n:white_check_mark:Sus:white_check_mark:\n:spy:Impossible for Data Breaching:spy:")
  
  @commands.command()
  async def version(self, ctx):
	  await ctx.send(":rocket:Current Version::rocket:\n`1.5.5`\n\n\n:inbox_tray:What's new to this update::inbox_tray:\n:white_check_mark:$sabotage\n\n:clock3:What is still to come::clock3:\n:clock3:Fixing the servers I'm in status\n\n:outbox_tray:What we removed::outbox_tray:\n:x:Nothing!")
  

  @commands.command()
  async def creator(self, ctx):
	  await ctx.send(":placard:The Impostor was a bot created by Baz!:placard:\n:one:This is actually his first ever coded bot!:one:\n:snake:It is a discord.py bot!:snake:\n:warning:The bot is not complete yet!:warning:\n:sparkling_heart:Show some love and join his server!:sparkling_heart:\n:calling: https://discord.gg/5jKA9kj :calling:")
  
  
 
 

  @commands.command()
  async def feedback(self, ctx):
	  await ctx.send(":pencil:Please answer this short survey to let us know how you feel about the bot::pencil:\nhttps://docs.google.com/forms/d/e/1FAIpQLSeS_fcVh5_GRBmYCFw5qkxU29lSLU1zsTkioePy7Kp8roTVig/viewform?usp=sf_link")
	  print(f"{ctx.author} has triggered the feedback command")
	    





def setup(client):
  client.add_cog(Basic(client))
