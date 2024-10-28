import http.client
import json

headers = {'Content-Type': 'application/json'}
body = json.dumps({ "content": "light_toDark"}).encode('utf-8')

conn = http.client.HTTPSConnection('discord.com')
conn.request('POST', '/api/webhooks/', body, headers)
res = conn.getresponse()