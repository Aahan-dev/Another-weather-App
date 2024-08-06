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
        
        # Prints the current weather conditions
        print(f"The current temperature in {location} is {current_temp}°C")
        print(f"""The current weather conditions are {current_weather}""")
        print(f"The current temperature feels like {current_feels_like}°C")
        print(f"The current humidity is {current_humidity}%")
        print(f"The current visibility is {current_visibility}m")
        print(f"The minimum temperature is {min_temp}°C")
        print(f"The maximum temperature is {max_temp}°C")
   
    elif current_weather_response.status_code in range(400, 500):
        print("User error, either the city you have used does not exist or you have spelled the name wrong, try again")
        return -1,-1,-1,-1,-1,-1,-1,-1
   
    elif current_weather_response.status_code in range(500, 600):
        print("Server error, servers may be down, try again later")
        return -1,-1,-1,-1,-1,-1,-1,-1


def get_5day_forecast(location):
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric'
    forecast_response = requests.get(forecast_url)
    forecast_data = json.loads(forecast_response.text)


    forecast_list = forecast_data['list']


    forecast = {}
    for f in forecast_list:
        date = f['dt_txt'][:10]
        if date not in forecast:
            forecast[date] = {
                'temp': f['main']['temp'],
                'weather': f['weather'][0]['description']
            }
            record_interaction(location, f['main']['temp'], f['main']['humidity'], f['weather'][0]['description'], interactions)
    print("\n5-day forecast:")
    
    

    for date, weather in forecast.items():
        print(f'{date}: Temperature: {weather["temp"]}°C, Weather: {weather["weather"]}')


def record_interaction(city, temperature, humidity, conditions, interactions):
    interactions.append({
        'City': city,
        'Temperature': temperature,
        'Humidity': humidity,
        'Conditions': conditions
    })


def display_interactions(interactions):
    print("Past Interactions:")
    for interaction in interactions:
        print(f"City: {interaction['City']}")
        print(f"Temperature: {interaction['Temperature']}°C")
        print(f"Humidity: {interaction['Humidity']}%")
        print(f"Conditions: {interaction['Conditions']}")
        print()
   


def weather_app():
    while True:
        choice = input("""
        Aahan's Weather App Menu:
        1. Current Weather
        2. 5-Day Forecast
        3. Exit
        4. Help
        5. History
        Enter choice: """)
       
        if choice == '1':
            location = input("Enter location: ")
            show_current_weather(location)