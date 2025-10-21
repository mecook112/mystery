import requests
from config import WEATHER_API_KEY


def get_weather(lat, lon):
    # print(city)
    # print(stateCode)
    # print(WEATHER_API_KEY)
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}'
    print(url)
    response = requests.get(url)
    data = response.json()
    if response.status_code !=200:
        raise Exception(f"Error: {data.get('message')})")
    # weather = {
    #     "city": data["name"],
    #     "temp": data["main"]["temp"],
    #     "condition": data["weather"][0]["description"].title(),
    # }
    return data

