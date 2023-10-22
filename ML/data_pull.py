import requests
import json
import numpy as nd
import pandas as pd

base = "http://ip-api.com/json/"

zip = requests.get(f"{base}").json()['zip']
df = pd.ExcelFile('urban-data.xlsx').parse(0)
zip_codes = df['ZCTA'].to_numpy().tolist()
row = zip_codes.index(int(zip))

categories = ('null', 'Urban', 'Suburban', 'Rural')

APIkey = "46e89de8832f4f74921204441232110"
base = "http://api.weatherapi.com/v1"

weather_info = requests.get(f"{base}/current.json?key={APIkey}&q={zip}&aqi=yes").json()

city = weather_info['location']['name']
state = weather_info['location']['region']
category = categories[df['classification'].to_numpy()[row]] # urban, suburban, rural
condition = weather_info['current']['condition']['text'].lower()

cloudy = ['cloudy', 'overcast', 'mist', 'fog']
rainy = ['rain', 'drizzle', 'thundery']
snowy = ['snow', 'sleet', 'blizzard', 'pellets']

if any(i in condition for i in cloudy):
    condition = 'Cloudy'
elif any(j in condition for j in rainy):
    condition = 'Rainy'
elif any(k in condition for k in snowy):
    condition = 'Snowy'
else:
    condition = 'Sunny'
