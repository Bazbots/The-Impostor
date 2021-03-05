import discord
from discord.ext import commands
from colorama import Fore

class Tier_Info(commands.Cog):

  def __init__(self, client):
    self.client = client


  @commands.command()
  async def tier(self, ctx, tier):
    if tier == "current":
      await ctx.send(":free:You are in `Basic` Tier!:free:\nThis is Tier `1` out of 3!\n:free:Basic:free:\n:coin:Gold:coin:\n:gem:Diamond:gem:")
    else:
      pass
    if tier == "basic":
      await ctx.send(":question:What you can do at `Basic` Tier::question:\n:white_check_mark:Use all Basic commands (all under basic in $commands)\n:white_check_mark:You have access to certain modes (Standard and Crazy Colours)")
    else:
      pass
    if tier == "gold":
      await ctx.send(":coin:What you get when you reach `Gold` Tier::coin:\n:coin:Access to most modes(To be added soon)\n:coin:Multiplayer Mode\n:coin:A 10% higher chance of being Impostor")
    else:
      pass
    if tier == "diamond":
      await ctx.send(":gem:What you get at `Diamond` Tier::gem:\n:gem:Access to all modes, even before they are released!\n:gem:25% higher chance of being Impostor\n:gem:Able to suggest modes for the bot!")
    else:
      pass

  @tier.error
  async def no_tier(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f":x:Error:x:\n:information_source:{error}")
      print(Fore.GREEN + f"Error: {error}")

  @commands.command()
  async def vote(self, ctx):
	  await ctx.send(":arrow_up:The bot can been found here::arrow_up:\nhttps://top.gg/bot/759436027529265172")

def setup(client):
  client.add_cog(Tier_Info(client))
