#   _____                      ____        _   
#  / ____|                    |  _ \      | |  
# | (___  _ __   __ _  ___ ___| |_) | ___ | |_ 
#  \___ \| '_ \ / _` |/ __/ _ \  _ < / _ \| __|
#  ____) | |_) | (_| | (_|  __/ |_) | (_) | |_ 
# |_____/| .__/ \__,_|\___\___|____/ \___/ \__|
#        | |                                   
#        |_|                                   
#
#
# Made by:
#           _                 _            _                         
#          | |               | |          | |                        
#   ___  __| | __ _ _ __  ___| |_ ___  ___| |__        _ ____      __
#  / _ \/ _` |/ _` | '_ \/ __| __/ _ \/ __| '_ \      | '_ \ \ /\ / /
# |  __/ (_| | (_| | | | \__ \ ||  __/ (__| | | |  _  | |_) \ V  V / 
#  \___|\__,_|\__,_|_| |_|___/\__\___|\___|_| |_| (_) | .__/ \_/\_/  
#                                                     | |            
#                                                     |_|                                                                    
#                      spacebot.edanstech.pw


#Imports everything that is needed
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import requests
import random

#   _____      _   _   _                 
#  / ____|    | | | | (_)                
# | (___   ___| |_| |_ _ _ __   __ _ ___ 
#  \___ \ / _ \ __| __| | '_ \ / _` / __|
#  ____) |  __/ |_| |_| | | | | (_| \__ \
# |_____/ \___|\__|\__|_|_| |_|\__, |___/
#                               __/ |    
#                              |___/     
# Settings for the bot to run and work

#Bot token
bottoken = "BOT TOKEN"
#NASA API key
apikey = "NASA API KEY"
#Bot command prefix
commandprefix = "#"
#Hd image mode (May take longer to load image on slower connections)
hd = "true"

#   _____          _      
#  / ____|        | |     
# | |     ___   __| | ___ 
# | |    / _ \ / _` |/ _ \
# | |___| (_) | (_| |  __/
#  \_____\___/ \__,_|\___|
# Dont go past here unless you know what you are doing                        

#Toggles HD mode
if hd == True:
    hdmodetoggle = "hdurl"
else:
    hdmodetoggle = "url"

#Makes tha API work
r = requests.get("https://api.nasa.gov/planetary/apod?api_key="+ apikey )
json_object = r.json()
copyright1 = (json_object['copyright'])
title = (json_object['title'])
explanation = (json_object['explanation'])
url = (json_object[hdmodetoggle])
date = (json_object['date'])

#Making bot command the same one as set in the settings above
bot = commands.Bot(command_prefix=commandprefix)

#Starting up
@bot.event
async def on_ready():
    print ("Starting up")
    print ("My username is " + bot.user.name + " and i am running with the ID: " + bot.user.id)
    print ("Started")

#Image command #image
@bot.command(pass_context=True)
async def image(ctx):
    await bot.say("Copyright: "+ copyright1)
    await bot.say("Title: "+ title)
    await bot.say("Explanation: "+ explanation)
    await bot.say(url)
    await bot.say(date)
    print ("Image posted")

#Test if bot commands are working #test
@bot.command(pass_context=True)
async def test(ctx):
    await bot.say("Test")
    print ("Test posted")
    
#Credits
@bot.command(pass_context=True)
async def credits(ctx):
    await bot.say("Bot made by EdansTech")
    await bot.say("https://edanstech.pw")
    await bot.say("Official Supporter")
    await bot.say("https://molepatrol.club")
    print ("Credits Posted")

#Runs the bot with the token used in settings
bot.run(bottoken)

#  ______           _ 
# |  ____|         | |
# | |__   _ __   __| |
# |  __| | '_ \ / _` |
# | |____| | | | (_| |
# |______|_| |_|\__,_|
#
# You have reached the end                     
