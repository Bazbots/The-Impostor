import discord
from discord.ext import commands
from colorama import Fore
import random

deaths = ["brutally murdered them", "ejected them into space", "no scoped them for a 180 headshot", "oofed them", "tripping them over and them making them fall into some conveniently placed lava", "`demonitised` them... I'm talking to <@744610714316046387> too!", "repeatedly stabbed them in the back", "hacked all of their `vbucks`", "summoned the enderdragon", "made people think that Innersloth added the airship map (still not here yet)"]

vents = ["to Polus", "to Mira HQ", "into the Nether...?", "to top.gg where they vote for The Impostor 😎😎😎😎", "to the airship map :O (that we have waited forever for)"]

places = ["Electrical", "Medbay" , "Security", "Cafeteria", "Navigation", "Storage", "Admin", "Shields", "Oxygen", "Office", "Laboratory"]

class Impostor(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def eject(self, ctx, name, role):
    if role == "crew":
      await ctx.send(f". 　　　。　　　　•　 　ﾟ　　。 　　.\n　.　　　 　　.　　　　　。　　 。　. \n.　　 。　　　　　 ඞ 。 . 　　 • 　　　　•\n　ﾟ　　 {name} was not The Impostor.　 。　\n'　　。 . 　•　  1 Impostor remains 　 　　。\n。 . 　　 •　　　.　　　. ,　　　　。 . 　　 •")
   
    elif role == "imp":
      await ctx.send(f". 　　　。　　　　•　 　ﾟ　　。 　　.\n　.　　　 　　.　　　　　。　　 。　. \n.　　 。　　　　　 ඞ 。 . 　　 • 　　　　•\n　ﾟ　　 {name} was The Impostor.　 。　\n'　　。 . 　•　  0 Impostors remain 　 　　。\n。 . 　　 •　　　.　　　. ,　　　　。 . 　　 •")
    else:
      await ctx.send("Please provide a valid role like \"crew\" or \"imp\"")

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

  @commands.command()
  async def vent(self, ctx):
    await ctx.send(f"{ctx.author.mention} goes to {random.choice(places)} and vents {random.choice(vents)}!")
  
  @commands.command()
  @commands.is_owner()
  async def alldeaths(self, ctx):
    await ctx.send(f"Deaths:\n{deaths}")
  
  @commands.command()
  @commands.is_owner()
  async def allvents(self, ctx):
    await ctx.send(f"All possible outcomes of $vent:\n{vents}\n{places}")
  
def setup(client):
  client.add_cog(Impostor(client))
