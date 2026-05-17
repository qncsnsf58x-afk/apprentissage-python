import requests

def get_meteo(city, latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
    data = response.json()

    temperature = data["current_weather"]["temperature"]
    windspeed = data["current_weather"]["windspeed"]

    return f"{city} : {temperature}°C, vent {windspeed} km/h"

cities = [
    {"name": "Paris", "latitude": 48.85, "longitude": 2.35},
    {"name" : "Bali", "latitude": -8.65, "longitude":115.22},
    {"name" : "Singapour", "latitude": 1.35, "longitude":103.82}
]

def display_weather(cities):
    for city in cities:
        print(get_meteo(city["name"],city["latitude"], city["longitude"]))
display_weather(cities)