import requests
import json
import numpy as nd
import pandas as pd

def getZipCode(self):
    base = "http://ip-api.com/json/"
    return requests.get(f"{base}").json()['zip']


def getWeatherInfo(self, zip):
    APIkey = "46e89de8832f4f74921204441232110"
    base = "http://api.weatherapi.com/v1"
    return requests.get(f"{base}/current.json?key={APIkey}&q={zip}&aqi=yes").json()

def getWeather(self):
    condition = getWeatherInfo(getZipCode())['current']['condition']['text'].lower()
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
    return condition
    
def getCityCategory(self):
    df = pd.ExcelFile('urban-data.xlsx').parse(0)
    zip_codes = df['ZCTA'].to_numpy().tolist()
    row = zip_codes.index(int(getZipCode()))
    categories = ('null', 'Urban', 'Suburban', 'Rural')
    category = categories[df['classification'].to_numpy()[row]] # urban, suburban, rural
    return category
    