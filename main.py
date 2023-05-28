import requests


def get_weather(city):
    params = {
              'appid': 'b3f9fd0900e3fa590a4aadf55c65b106',
              'q': city,
              'lang': 'ru',
              'units': 'metric'
          }

    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather", params=params
    )
    response = response.json()
    temp = response['main']['temp']
    description = response['weather'][0]['description']

    return {"temp": temp, "description": description}


print(get_weather("Москва"))
