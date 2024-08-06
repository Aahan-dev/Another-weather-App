import requests
import json
import time

# API Key for OpenWeatherMap
api_key = '21857ebedc19b88ac028582686871f7a'

interactions = []

def show_current_weather(location):
    current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    current_weather_response = requests.get(current_weather_url)
    if current_weather_response.status_code in range(200, 300):
        
        # Parse JSON response
        current_weather_data = json.loads(current_weather_response.text)

        # Extract current weather conditions
        current_temp: int = current_weather_data['main']['temp'] 
        current_weather: str = current_weather_data['weather'][0]['description']
        current_feels_like: int = current_weather_data['main']['feels_like']
        current_humidity: str = current_weather_data['main']['humidity']
        current_visibility: str = current_weather_data['visibility']
        min_temp: int = current_weather_data['main']['temp_min']
        max_temp: int = current_weather_data['main']['temp_max']
        record_interaction(location, current_temp, current_humidity, current_weather, interactions)
        
        