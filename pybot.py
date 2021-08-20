from os import name
import discord
from discord import client
from discord import activity
from discord.enums import Status
from discord.ext import commands
from _asyncio import *
from discord.ext.commands.core import command
import random

Client = commands.Bot(command_prefix="!")

Client.remove_command("help")

token = ""

# Activity

@Client.event
async def on_ready():
    await Client.change_presence(status=discord.Status.online, activity=discord.Game(name="With You"))

# Commands

@Client.command()
async def help(js):
    await js.send("Command Help Run Shad")

@Client.command()
async def hello(js, member : discord.Member):
    theembed = discord.Embed(title="Hello Mardak/Zanak", description="یک سلام معمولی", color= 0xfff)
    await member.send(embed=theembed)

@Client.command()
async def embed(js, member : discord.Member):
    theembed = discord.Embed(title = "Test", description= "Descriptiontest", color= 0x000)
    await js.send(embed=theembed)
    await member.send(embed=theembed)

# Runing

Client.run(token)