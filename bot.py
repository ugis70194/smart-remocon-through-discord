import discord
import os
import subprocess
import datetime
from time import sleep
from dotenv import load_dotenv

def send_signal(id: str):
  subprocess.run(["python3", "./_irrp.py", "-p", "-g17", "-f", "./codes", id])

def reserve_signal(id: str, hour: str, minute: str):
  command = f"python3 /home/pi/smart-remocon/_irrp.py -p -g17 -f ./codes {id}"
  subprocess.run(f'echo {command} | at {hour}:{minute}')

load_dotenv(".env")

TOKEN = os.getenv("TOKEN")
print(TOKEN)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  command = message.content.split("_")
  if command[0] == "light":
    if command[1] == "on":
      send_signal("light:toggle")
    elif command[1] == "off":
      send_signal("light:toggle")
      sleep(0.5)
      send_signal("light:toggle")
  elif command[0] == "aircon":
    if command[1] == "cool":
      if command[3] == "reserve":
        reserve_signal("aircon:cool", command[4], command[5])
      else:
        send_signal("aircon:cool")
    elif command[1] == "warm":
      if command[3] == "reserve":
        reserve_signal("aircon:warm", command[4], command[5])
      else:
        send_signal("aircon:warm")
    elif command[1] == "off":
      send_signal("aircon:off")
  else:
    pass

client.run(TOKEN)
