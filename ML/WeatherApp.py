import requests
import json

class WeatherApp:

    def __init__(self, api_key, base, api_method):
        self.api_key = "46e89de8832f4f74921204441232110"
        self.base = "http://api.weatherapi.com/v1"
        self.query = "/current.json"
    
    def get_weather(self, location = "Austin"): 
        weather = requests.get(f"{self.base}{self.api_method}?key={self.query}&q={location}&aqi=yes").json
