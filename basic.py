import discord
from discord.ext import commands
from colorama import Fore

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
	  await ctx.send("Need help? Join my support server!\nhttps://discord.gg/Sun4mtFjwE\nOr you can view all the current commands below!\n\n\n:robot:Current Commands::robot:\nUse prefix `$`\nhelp\nabout\ninvite\nversion\nfeedback\nwebsite\nvote\nservers\ncreator\ngithub\ntier {current/basic/gold/diamond}\nping\neject {user} {role}\nreport {your username} {problem}\nsus")

  @commands.command()
  async def invite(self, ctx):
	  await ctx.send(":incoming_envelope:Invite me here!:incoming_envelope:\n https://discord.com/api/oauth2/authorize?client_id=759436027529265172&permissions=3423071425&redirect_uri=https%3A%2F%2Fbazbots.github.io%2FImpostor-Bot&scope=bot")
      
  @commands.command()
  async def about(self, ctx):
	  await ctx.send(":question:A bit about The Impostor:question:\n\n:lock:100% Safe and Secure:lock:\n:england:English:england:\n:white_check_mark:Sus:white_check_mark:\n:spy:Impossible for Data Breaching:spy:")
  
  @commands.command()
  async def version(self, ctx):
	  await ctx.send(":rocket:Current Version::rocket:\n`1.4.3`\n\n\n:inbox_tray:What's new to this update::inbox_tray:\n:white_check_mark:$kill (Thanks <@513283671353196585> for the suggestion)\n\n:clock3:What is still to come::clock3:\n:clock3:Solo Mode Among Us\n:clock3:Fixing the guild status issue\n:clock3:The return of $changeprefix\n$play and $modes\n\n:outbox_tray:What we removed::outbox_tray:\n:x:Nothing")
  
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

  @commands.command()
  async def report(self, ctx, username, problem):
    print(Fore.GREEN + f"{username} has a problem: {problem}")
    await ctx.send("Done!\nThanks for reporting this issue, we will look into it!")

  @report.error
  async def no_prob_or_user(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f":x:Error:x:\n:information_source:{error}")
      print(Fore.GREEN + f"Error: {error}")

  



def setup(client):
  client.add_cog(Basic(client))
