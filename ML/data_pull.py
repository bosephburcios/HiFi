import requests
import json

base = "http://ip-api.com/json/"

city = requests.get(f"{base}").json()['city']

APIkey = "46e89de8832f4f74921204441232110"
base = "http://api.weatherapi.com/v1"

current_weather = requests.get(f"{base}/current.json?key={APIkey}&q={city}&aqi=yes").json()

print(current_weather)

# with open('data.json', 'w') as file:
    # json.dump(current_weather, file)

