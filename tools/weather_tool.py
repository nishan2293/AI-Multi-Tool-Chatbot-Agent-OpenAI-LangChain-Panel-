from langchain.tools import tool
from pydantic import BaseModel, Field
import requests

class WeatherInput(BaseModel):
    latitude: float = Field(..., description="Latitude of the location")
    longitude: float = Field(..., description="Longitude of the location")

@tool(args_schema=WeatherInput)
def get_current_weather(latitude: float, longitude: float) -> str:
    """Fetches current weather using Open-Meteo API"""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        weather = response.json().get('current_weather', {})
        return f"Temperature: {weather.get('temperature')}°C, Windspeed: {weather.get('windspeed')} km/h"
    return "Unable to fetch weather data." 