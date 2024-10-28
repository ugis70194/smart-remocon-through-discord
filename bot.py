import discord
import os
from dotenv import load_dotenv
from modules.Light import Light

load_dotenv(".env")

TOKEN = os.getenv("TOKEN")
print(TOKEN)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

light = Light()

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  command = message.content.split("_")
  if not (command[0] == "light" or command[0] == "aircon" or command[0] == "cleaner"):
    return
  
  if   command[0] == "light":
    if   command[1] == "on":       light.on()
    elif command[1] == "off":      light.off()
    elif command[1] == "night":    light.night()
    elif command[1] == "toBright": light.toBright()
    elif command[1] == "toDark":   light.toDark()
    elif command[1] == "toWarm":   light.toWarm()
    elif command[1] == "toCool":   light.toCool()
    elif command[1] == "full":     light.full()
    elif command[1] == "reset":    light.reset()
  elif command[0] == "aircon":
    pass

client.run(TOKEN)
