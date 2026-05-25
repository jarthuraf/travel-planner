import os
import requests
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

WEATHER_KEY = os.getenv("WEATHER_API_KEY")
MAP_KEY = os.getenv("MAP_API_KEY")

def get_weather(city):
    """Fetches current weather for a city using OpenWeatherMap."""
    if not WEATHER_KEY:
        return {"error": "API key missing"}
        
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_KEY}&units=metric"
    
    try:
        response = requests.get(url, timeout=5)
        # If the city isn't found or API fails, raise an exception
        response.raise_for_status() 
        data = response.json()
        
        return {
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"].title()
        }
    except requests.RequestException:
        # Fallback if internet is down or city name is weird
        return None