import http.client
import json

headers = {'Content-Type': 'application/json'}
body = json.dumps({ "content": "light_reset"}).encode('utf-8')

conn = http.client.HTTPSConnection('discord.com')
conn.request('POST', '/api/webhook', body, headers)
res = conn.getresponse()