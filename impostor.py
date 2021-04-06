import discord
from discord.ext import commands
from colorama import Fore
import random
import asyncio

deaths = ["brutally murdered them", "ejected them into space", "no scoped them for a 180 headshot", "oofed them", "tripping them over and them making them fall into some conveniently placed lava", "`demonitised` them... I'm talking to you <@818571042267594755>!", "repeatedly stabbed them in the back", "hacked all of their `vbucks`", "summoned the enderdragon"]

vents = ["to Polus", "to Mira HQ", "into the Nether...?", "to top.gg where they vote for The Impostor 😎😎😎😎", "to the airship map :O (that we have finally got)"]

places = ["Electrical", "Medbay" , "Security", "Cafeteria", "Navigation", "Storage", "Admin", "Shields", "Oxygen", "Office", "Laboratory"]

where = ["somewhere", "at top.gg where you vote for the impostor", "Electrical", "Medbay" , "Security", "Cafeteria", "Navigation", "Storage", "Admin", "Shields", "Oxygen", "Office", "Laboratory"]

colours = ["Yellow", "Red", "Blue", "Cyan", "Orange", "Lime", "Green", "Pink", "Purple", "Black", "White", "Brown"]

how = ["bruh did you kermit the frog or something?", "ok you are die", "do you need help or something?", "please don't"]

you = ["ha ha lol you can't kill me! im the impostor!", "you really thought", "you fool i"]

class Impostor(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def eject(self, ctx, name, role):
    name.replace("_", " ")
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
    if username == "me":
      await ctx.send(random.choice(how))
    elif username == "<@759436027529265172>":
      await ctx.send(random.choice(you))
    elif username == "you":
      await ctx.send(random.choice(you))
    else:
        embedOne = discord.Embed(
        description=f"{username} has been killed by {ctx.author.mention} who {random.choice(deaths)}!",
        colour = discord.Colour.red()
      )
        embedOne.set_thumbnail(url="https://preview.redd.it/rnj1si3kzwn51.png?width=720&format=png&auto=webp&s=6e7243bb5c2d8f27921313b0f8ef27617523d604")
        embedOne.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
        await ctx.send(embed=embedOne)

  @kill.error
  async def no_username(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f":x:Error:x:\n:information_source:{error}")
      print(Fore.GREEN + f"Error: {error}")

  @commands.command()
  async def vent(self, ctx):
    embedThree = discord.Embed(description=f"{ctx.author.mention} goes to {random.choice(places)} and vents to {random.choice(vents)}",
      colour = discord.Colour.red()
    )
    embedThree.set_thumbnail(url="https://static.wikia.nocookie.net/among-us-wiki/images/d/db/Vent.png/revision/latest/top-crop/width/360/height/360?cb=20210220170224")
    embedThree.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    await ctx.send(embed=embedThree)
  
  @commands.command()
  @commands.is_owner()
  async def alldeaths(self, ctx):
    await ctx.send(f"Deaths:\n{deaths}")
  
  @commands.command()
  @commands.is_owner()
  async def allvents(self, ctx):
    await ctx.send(f"All possible outcomes of $vent:\n{vents}\n\n{places}")

  @commands.command()
  async def sabotage(self, ctx, sab):
       if sab[0].lower() == "c":
         coms = await ctx.send("Please Wait...")
         await asyncio.sleep(2)
         for i in range(1, 5):
           await coms.edit(content="Beginning Sabotage...")
           await asyncio.sleep(2)
           await coms.edit(content="Please wait...")
           await asyncio.sleep(2)
         await coms.edit(content="Communtications Sabotaged!\nAll systems are offline!")
       elif sab[0].lower() == "r":
         countdown = 30
         reactor = await ctx.send("Please Wait...")
         await asyncio.sleep(2)
         for i in range(1,5):
           await reactor.edit(content="Beginning Sabotage...")
           await asyncio.sleep(2)
           await reactor.edit(content="Please Wait...")
           await asyncio.sleep(2)
         for i in range(1, 31):
           await reactor.edit(content=f"Reactor Meltdown in {countdown}!")
           await asyncio.sleep(1)
           countdown = countdown - 1
           await reactor.edit(content=f"Reactor Meltdown in {countdown}!")
           if countdown == 0:
             await reactor.edit(content="Reactor has Meltdown!\nAll crewmates have been eliminated")
           else:
             pass
       elif sab[0].lower() == "l":
         lights = await ctx.send("Please Wait...")
         await asyncio.sleep(2)
         for i in range(1, 5):
           await lights.edit(content="Beginning Sabotage...")
           await asyncio.sleep(2)
           await lights.edit(content="Please wait...")
           await asyncio.sleep(2)
         await lights.edit(content="Lights Pannel\n\n████████████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n███████████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n██████████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n█████████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n████████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n███████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n██████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n█████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n███████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n██████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n█████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n███████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n██████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n█████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n███")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n██")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n█")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\nOffline!")
         await asyncio.sleep(2)
         await ctx.send("Lights have been turned off!\nVision for crewmates has been impared!")
       elif sab[0].lower() == "o":
         countdowno = 30
         oxygen = await ctx.send("Please Wait...")
         await asyncio.sleep(2)
         for i in range(1, 5):
           await oxygen.edit(content="Beginning Sabotage...")
           await asyncio.sleep(2)
           await oxygen.edit(content="Please wait...")
           await asyncio.sleep(2)
         for i in range(1, 31):
           await oxygen.edit(content=f"Oxygen Depleteing in {countdowno}")
           await asyncio.sleep(2)
           countdowno = countdowno - 1
         await oxygen.edit(content="Oxygen has been Depleted!\nAll crewmates have been eliminated!")
       else:
         await ctx.send(f"{ctx.author.mention}\nThis sabotage does not exist!")

  @sabotage.error
  async def sab_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(
         title="Sabotage Menu", description=":radioactive: Reactor\n:zap: Lights\n:satellite: Communications\n:regional_indicator_o: Oxygen\n\n",
         colour=discord.Colour.red()
         )
      embed.set_footer(text="Type $sabotage (sabotage)\n\n© Baz - The Impostor - Among Us bot for Discord")
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/among-us-wiki/images/f/f3/Sabotage.png/revision/latest/top-crop/width/360/height/360?cb=20210220165836")
      await ctx.send(embed=embed)

  @commands.command()
  @commands.is_owner()
  async def report(self, ctx):
    embedFour = discord.Embed(
      title=":loudspeaker: Dead Body Reported :loudspeaker:",
      description=f"{random.choice(colours)}'s body has been found {random.choice(where)}!",
      colour = discord.Colour.red()
      )
    embedFour.set_thumbnail(url="https://static.wikia.nocookie.net/among-us-wiki/images/9/94/Report.png/revision/latest/top-crop/width/360/height/360?cb=20210220165923")
    embedFour.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    await ctx.send(embed=embedFour)
  
def setup(client):
  client.add_cog(Impostor(client))
