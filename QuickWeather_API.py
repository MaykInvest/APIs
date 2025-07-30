
from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_K")

city = input('Enter your city: ')

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    country = data['sys']['country']

    print(f"Weather in {city}, {country}: {weather_description.capitalize()}")
    print(f"Temperature: {temperature}ºC (feels like {feels_like}ºC)")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed} m/s")

else:
    print(f"Failed to retrieve data: {response.status_code}")
