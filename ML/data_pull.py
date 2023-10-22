import requests
import json
import numpy as nd
import pandas as pd

base = "http://ip-api.com/json/"

zip = requests.get(f"{base}").json()['zip']
df = pd.ExcelFile('urban-data.xlsx').parse(0)
zip_codes = df['ZCTA'].to_numpy().tolist()
row = zip_codes.index(int(zip))
categories = ('null', 'urban', 'suburban', 'rural')

# urban, suburban, rural classification of the zip code
category = categories[df['classification'].to_numpy()[row]]

APIkey = "46e89de8832f4f74921204441232110"
base = "http://api.weatherapi.com/v1"

weather_info = requests.get(f"{base}/current.json?key={APIkey}&q={zip}&aqi=yes").json()

print(weather_info)

# current_weather = weather_info['current']['text']

# with open('data.json', 'w') as file:
    # json.dump(current_weather, file)

