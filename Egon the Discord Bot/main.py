import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord_settings import *
from Egon_Gmail import *



bot = commands.Bot(command_prefix='$')

@bot.command(name='orwell')
async def orwell(ctx, arg):
    getEmails()
    print("I ran orwell!")
    pass

@bot.command(name='unitednations')
async def orwell(ctx, arg):
    getEmails()
    print("I hate the anti-christ!")
    #channel = bot.get_channel(935620087329730563)
    #await channel.send('working!',file = discord.File(r"C:\Users\Lhorigan\PycharmProjects\egon\sample.html"))
    #os.remove(r'C:\Users\Lhorigan\PycharmProjects\egon\sample.html')
    pass


load_dotenv()
EGON = os.getenv("EGON_DISCORD_KEY")
bot.run(EGON)
