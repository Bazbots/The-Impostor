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
    await ctx.send("Beginning scan...")
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
    download_data = await ctx.send("Downloading Data\n")
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
    inspection = await ctx.send("Beginning Inspection\n")
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
  async def weatherdownload(self, ctx):
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

     
    
    
def setup(client):
  client.add_cog(Tasks(client))
