import requests
import json
import numpy as nd
import pandas as pd

base = "http://ip-api.com/json/"

zip = requests.get(f"{base}").json()['zip']

df = pd.ExcelFile('urban-data.xlsx').parse(0)
row = df['ZCTA'].to_numpy().tolist().index(int(zip))
categories = ('null', 'urban', 'suburban', 'rural')

category = categories[df['classification'].to_numpy()[row]]

print(category)
APIkey = "46e89de8832f4f74921204441232110"
base = "http://api.weatherapi.com/v1"

current_weather = requests.get(f"{base}/current.json?key={APIkey}&q={zip}&aqi=yes").json()

# with open('data.json', 'w') as file:
    # json.dump(current_weather, file)

