import http.client
import json
from os import getenv

from dotenv import load_dotenv

load_dotenv()
WEBHOOK = getenv("WEBHOOK")

headers = {"Content-Type": "application/json"}
body = json.dumps({"content": "light_full"}).encode("utf-8")

conn = http.client.HTTPSConnection("discord.com")
conn.request("POST", WEBHOOK, body, headers)
res = conn.getresponse()
