import requests
import json

webhook_url = "http://127.0.0.1:5000/delay"

data = {'event': 'FishTankPump',
        'delay': 10,
        'key': 'uFka7sL1ho2J0CLg7WTnq'}
        
r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})