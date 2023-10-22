import requests
import googlemaps
import json


base = "http://api.weatherapi.com/v1"

APIkey = "46e89de8832f4f74921204441232110"

user_input = input("Enter City: ")

current_weather = requests.get(f"{base}/current.json?key={APIkey}&q={user_input}&aqi=yes").json()

with open('data.json', 'w') as file:
    json.dump(current_weather, file)
    

    



