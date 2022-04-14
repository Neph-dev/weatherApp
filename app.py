# Fetch the weather data from https://openweathermap.org
# You need to provide your personal API key from https://openweathermap.org
# to be able to execute this program.
# "status_code == 200" is the OK status code.

import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
API_KEY = 'YOUR API KEY'

city = input('Enter a city name: ')

api_endpoint = f'{BASE_URL}?appid={API_KEY}&q={city}'

response = requests.get(api_endpoint)

if response.status_code == 200:
    data = response.json()

    temperature = data['main']['temp']
    # convert temperature from kelvin to celsius
    temperature_celsius = round(temperature - 274.15, 2)

    description = data['weather'][0]['description']

    city_name = data['name']
    country_code = data['sys']['country']

    message = f'It is currently {temperature_celsius}°c with {description} in {city_name}, {country_code}'
    print(message)

else:
    print('An error occurred')
