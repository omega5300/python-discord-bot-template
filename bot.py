# bot.py
import os
import time
import discord

from discord.ext import commands
from dotenv import load_dotenv

from urllib import parse, request
import re

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$', description="this is a helper BOT")

@bot.command()
async def ping(ctx):
    await ctx.send(f'pong {ctx.message.author.mention}')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def say(ctx, *, something):
    """Say something!"""
    if something is None:
        await ctx.send("What do you want to say?")
        return
    print(something)    
    await ctx.send(f"{ctx.message.author.mention} said: **{something}**")
    
# Events
@bot.event
async def on_ready():
    await print('My bot is Ready')

bot.run(TOKEN)
