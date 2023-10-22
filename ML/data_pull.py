import requests
<<<<<<< HEAD
import json
import numpy as nd
import pandas as pd
=======
import googlemaps
import json

>>>>>>> 5465960065e00d0fb3bd226bf9cf1ab055299b2c

base = "http://ip-api.com/json/"

zip = requests.get(f"{base}").json()['zip']

df = pd.ExcelFile('urban-data.xlsx').parse(0)
row = df['ZCTA'].to_numpy().tolist().index(int(zip))
categories = ('null', 'urban', 'suburban', 'rural')

category = categories[df['classification'].to_numpy()[row]]

print(category)
APIkey = "46e89de8832f4f74921204441232110"
base = "http://api.weatherapi.com/v1"

<<<<<<< HEAD
current_weather = requests.get(f"{base}/current.json?key={APIkey}&q={zip}&aqi=yes").json()
=======
APIkey = "46e89de8832f4f74921204441232110"

user_input = input("Enter City: ")

current_weather = requests.get(f"{base}/current.json?key={APIkey}&q={user_input}&aqi=yes").json()

with open('data.json', 'w') as file:
    json.dump(current_weather, file)
    

    

>>>>>>> 5465960065e00d0fb3bd226bf9cf1ab055299b2c

# with open('data.json', 'w') as file:
    # json.dump(current_weather, file)

