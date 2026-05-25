import os
import requests
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

WEATHER_KEY = os.getenv("WEATHER_API_KEY")
MAP_KEY = os.getenv("MAP_API_KEY")

# Style categories for local attractions
STYLE_CATEGORIES = {
    "adventure": "activity.sport",
    "luxury": "catering.restaurant.high_gaultmillau",
    "budget": "tourism.sights",
    "cultural": "entertainment.culture"
}

# Function to get current weather for a city
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
    
# Function to get coordinates for a city using Mapbox API
def get_coordinates(city):
    """Turns a city name into latitude and longitude using Geoapify."""
    if not MAP_KEY:
        return None

    # Geoapify Geocoding URL
    url = f"https://api.geoapify.com/v1/geocode/search?text={city}&apiKey={MAP_KEY}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Extract latitude and longitude from the first result
        if data["features"]:
            lon = data["features"][0]["properties"]["lon"]
            lat = data["features"][0]["properties"]["lat"]
            return {"lat": lat, "lon": lon}
        return None
    except requests.RequestException:
        return None
    
# Getting local attractions
def get_local_attractions(lat, lon, style):
    """Fetches real places near the coordinates based on travel style."""
    if not MAP_KEY:
        return []

    # Get the correct API category string for the chosen style
    category = STYLE_CATEGORIES.get(style.lower(), "tourism.sights")

    # Geoapify Places URL (searching within a 5000-meter radius)
    url = f"https://api.geoapify.com/v2/places?categories={category}&filter=circle:{lon},{lat},5000&limit=10&apiKey={MAP_KEY}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        attractions = []
        for feature in data.get("features", []):
            name = feature["properties"].get("name")
            # Only add it if the place actually has a name recorded
            if name:
                attractions.append(name)
        
        return attractions
    except requests.RequestException:
        return []