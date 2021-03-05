import discord
from discord.ext import commands
from colorama import Fore
import random

deaths = ["brutally murdered them", "ejected them into space", "no scoped them for a 180 headshot", "oofing them", "tripping them over and them making them fall into some conveniently placed lava", "snapped their neck!\nOuch!", "repeatedly stabbed them in the back", "hacked all of their `vbucks`"]

class Fun(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def eject(self, ctx, name, role):
    if role == "crew":
      await ctx.send(f". 　　　。　　　　•　 　ﾟ　　。 　　.\n　.　　　 　　.　　　　　。　　 。　. \n.　　 。　　　　　 ඞ 。 . 　　 • 　　　　•\n　ﾟ　　 {name} was not The Impostor.　 。　\n'　　。 . 　•　  1 Impostor remains 　 　　。\n。 . 　　 •　　　.　　　. ,　　　　。 . 　　 •")
    else:
      pass
    if role == "imp":
      await ctx.send(f". 　　　。　　　　•　 　ﾟ　　。 　　.\n　.　　　 　　.　　　　　。　　 。　. \n.　　 。　　　　　 ඞ 。 . 　　 • 　　　　•\n　ﾟ　　 {name} was The Impostor.　 。　\n'　　。 . 　•　  0 Impostors remain 　 　　。\n。 . 　　 •　　　.　　　. ,　　　　。 . 　　 •")
    else:
      pass

  @eject.error
  async def no_role(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f":x:Error:x:\n:information_source:{error}")
      print(Fore.GREEN + f"Error: {error}")

  @commands.command()
  async def sus(self, ctx):
    await ctx.send("⠀⠀           ⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀\n ⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀\n⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀\n⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀\n⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀\n⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀\n⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀\n⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀\n⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀\n⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀\n⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  
  @commands.command()
  async def kill(self, ctx, username):
    await ctx.send(f"{username} was killed by {ctx.author.mention} who {random.choice(deaths)}")

  @kill.error
  async def no_username(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f":x:Error:x:\n:information_source:{error}")
      print(Fore.GREEN + f"Error: {error}")


def setup(client):
  client.add_cog(Fun(client))
