import http.client
import json
from os import getenv

from dotenv import load_dotenv


def airconWarm():
    load_dotenv()
    WEBHOOK = getenv("WEBHOOK")

    headers = {"Content-Type": "application/json"}
    body = json.dumps({"content": "aircon_warm"}).encode("utf-8")

    conn = http.client.HTTPSConnection("discord.com")
    conn.request("POST", WEBHOOK, body, headers)
    res = conn.getresponse()
    return res.status


if __name__ == "__main__":
    airconWarm()
