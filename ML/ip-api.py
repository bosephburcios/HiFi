
import requests
import json

base = "http://ip-api.com/json/"

info = requests.get(f"{base}").json()

print(info)
