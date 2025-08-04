"""
This script retrieves and displays the current weather information for a user-specified city
using the OpenWeatherMap API.

Functionality:
- Loads the OpenWeatherMap API key from a `.env` file using the environment variable `API_K`.
- Prompts the user to enter the name of a city.
- Sends a GET request to the OpenWeatherMap API to fetch weather data for that city.
- If the request is successful, displays:
    - Weather description
    - Temperature in Celsius (with 'feels like' temperature)
    - Humidity percentage
    - Wind speed in meters per second
    - Country code

Requirements:
- A `.env` file containing your OpenWeatherMap API key in the format:
    API_K=your_api_key_here
- The following Python packages installed:
    - `requests`
    - `python-dotenv`

Example usage:
    Enter your city: London
    Weather in London, GB: Clear sky
    Temperature: 21ºC (feels like 20ºC)
    Humidity: 60%
    Wind speed: 3.6 m/s

Error Handling:
- If the API request fails (e.g., invalid API key, city not found), an error message and status code are displayed.
"""

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
