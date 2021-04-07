import discord
from discord.ext import commands
from colorama import Fore
import asyncio
import random

scan_resps = ["Yellow", "Red", "Blue", "Cyan", "Orange", "Lime", "Green", "Pink", "Purple", "Black", "White", "Brown"]

class Tasks(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def scan(self, ctx):
    scanning = await ctx.send("Beginning scan...")
    await asyncio.sleep(2)
    await ctx.send(f"ID: {ctx.author}")
    await asyncio.sleep(2)
    await ctx.send(f"HT: {random.randint(2, 10)}\"{random.randint(0,10)}\"")
    await asyncio.sleep(2)
    await ctx.send(f"WT: {random.randint(0,100)}lb")
    await asyncio.sleep(2)
    await ctx.send(f"C: {random.choice(scan_resps)}")
    await asyncio.sleep(4)
    await ctx.send(f"Scan Complete!\n{ctx.author} is clear!")

  @commands.command()
  async def download(self, ctx):
    download_data = await ctx.send("Beginning Download\n")
    await asyncio.sleep(1)
    await download_data.edit(content="Downloading Data.\n█")
    await asyncio.sleep(1)
    await download_data.edit(content="Downloading Data..\n██")
    await asyncio.sleep(1)
    await download_data.edit(content="Downloading Data...\n███")
    await asyncio.sleep(1)
    await download_data.edit(content="Downloading Data.\n████")
    await asyncio.sleep(1)
    await download_data.edit(content="Downloading Data..\n█████")
    await asyncio.sleep(1)
    await download_data.edit(content="Downloading Data...\n██████")
    await asyncio.sleep(1)
    await download_data.edit(content="Downloading Data.\n███████")
    await asyncio.sleep(1)
    await download_data.edit(content="Downloading Data..\n████████")
    await asyncio.sleep(1)
    await download_data.edit(content="Downloading Data...\n█████████")
    await asyncio.sleep(1)
    await download_data.edit(content="Downloading Data.\n██████████")
    await asyncio.sleep(1)
    await download_data.edit(content="Downloading Data..\n███████████")
    await asyncio.sleep(1)
    await download_data.edit(content="Downloading Data...\n████████████")
    await asyncio.sleep(1)
    await download_data.edit(content="Downloading Data.\n█████████████")
    await asyncio.sleep(1)
    await download_data.edit(content="Downloading Data..\n██████████████")
    await asyncio.sleep(1)
    await download_data.edit(content="Downloading Data...\n███████████████")
    await asyncio.sleep(1)
    await download_data.edit(content="Task Complete!")

  
  @commands.command()
  async def inspect(self, ctx):
    inspection = await ctx.send("Beginning Sample Inspection\n")
    timer = 60
    await asyncio.sleep(1)
    await inspection.edit(content=f"Inspecting\nTime Remaining: {timer}\n█")
    for i in range(5):
      await asyncio.sleep(1)
      timer = timer - 1
      await inspection.edit(content=f"Inspecting.\nTime Remaining: {timer}\n█")
    for i in range(6):
      await asyncio.sleep(1)
      timer = timer - 1
      await inspection.edit(content=f"Inspecting..\nTime Remaining: {timer}\n██")
    for i in range(6):
      await asyncio.sleep(1)
      timer = timer - 1
      await inspection.edit(content=f"Inspecting...\nTime Remaining: {timer}\n███")
    for i in range(6):
      await asyncio.sleep(1)
      timer = timer - 1
      await inspection.edit(content=f"Inspecting.\nTime Remaining: {timer}\n████")
    for i in range(6):
      await asyncio.sleep(1)
      timer = timer - 1
      await inspection.edit(content=f"Inspecting..\nTime Remaining: {timer}\n█████")
    for i in range(6):
      await asyncio.sleep(1)
      timer = timer - 1
      await inspection.edit(content=f"Inspecting...\nTime Remaining: {timer}\n██████")
    for i in range(6):
      await asyncio.sleep(1)
      timer = timer - 1
      await inspection.edit(content=f"Inspecting.\nTime Remaining: {timer}\n███████")
    for i in range(6):
      await asyncio.sleep(1)
      timer = timer - 1
      await inspection.edit(content=f"Inspecting..\nTime Remaining: {timer}\n████████")
    for i in range(6):
      await asyncio.sleep(1)
      timer = timer - 1
      await inspection.edit(content=f"Inspecting...\nTime Remaining: {timer}\n████████")
    for i in range(6):
      await asyncio.sleep(1)
      timer = timer - 1
      await inspection.edit(content=f"Inspecting.\nTime Remaining: {timer}\n█████████")
    await asyncio.sleep(1)
    await inspection.edit(content="Task Complete!")

  @commands.command()
  async def weather(self, ctx):
    weather_bar = await ctx.send("Beginning Download")
    await asyncio.sleep(1)
    await weather_bar.edit(content="Downloading.\n█\n\n")
    await asyncio.sleep(1)
    await weather_bar.edit(content="Downloading..\n██\n█\n")
    await asyncio.sleep(1)
    await weather_bar.edit(content="Downloading...\n███\n██\n█")
    await asyncio.sleep(1)
    await weather_bar.edit(content="Downloading.\n████\n███\n██")
    await asyncio.sleep(1)
    await weather_bar.edit(content="Downloading..\n█████\n████\n███")
    await asyncio.sleep(1)
    await weather_bar.edit(content="Downloading...\nDone!\n█████\n████")
    await asyncio.sleep(1)
    await weather_bar.edit(content="Downloading.\nDone!\nDone!\n█████")
    await asyncio.sleep(1)
    await weather_bar.edit(content="Downloading..\nDone!\nDone!\nDone!")
    await asyncio.sleep(1)
    await weather_bar.edit(content="Task Complete!")


  @commands.command()
  async def reboot(self, ctx, action):
    countdownr = 90
    if action.lower() == "start":
      rebooting = await ctx.send(f"Rebooting Wifi...\nPlease try again in {countdownr} seconds")
      for i in range(1, 91):
        await rebooting.edit(content=f"Rebooting Wifi...\nPlease try again in {countdownr} seconds")
        countdownr = countdownr - 1
        await asyncio.sleep(1)
      await asyncio.sleep(2)
      await rebooting.edit(content="Reboot complete!\nAll systems are back online!")
    else:
      await ctx.send("Next time say `$reboot start`")
    

  @reboot.error
  async def reb_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embedNine=discord.Embed(
      title="Wifi Pannel",
      colour=discord.Colour.green()
      )
      embedNine.add_field(name="Connection:", value=":x:", inline=True)
      embedNine.add_field(name="Back up Power:", value=":x:", inline=True)
      embedNine.add_field(name="Internal Server:", value=":x:", inline=True)
      embedNine.add_field(name="External Server", value=":x:", inline=True)
      embedNine.add_field(name="Summary:", value="Reboot Required", inline=True)
      embedNine.add_field(name="What to do:",value="Run `$reboot start` to start the reboot", inline=True)
      embedNine.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
      await ctx.send(embed=embedNine)
     
    
    
def setup(client):
  client.add_cog(Tasks(client))
