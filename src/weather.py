import requests
import datetime as dt

from config import WEATHER_API_KEY


#def get_weather(lat, lon):
def get_weather(city):
#def get_weather(city, st, country):
    #url = f'https://api.openweathermap.org/geo/1.0/direct?q={city},{st},{country}&units=imperial&appid={WEATHER_API_KEY}'
    url = f'https://api.openweathermap.org/data/2.5/weather?&q={city}&units=imperial&appid={WEATHER_API_KEY}'
    #url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={WEATHER_API_KEY}' # this one works
    print(url)
    response = requests.get(url)
    data = response.json()

    if response.status_code !=200:
        raise Exception(f"Error: {data.get('message')})")
    # This may work now below, but I am not sure about the .title() at the end just yet. I would like to change this to pull a city instead of lat lon.
    # weather = {
    #     "city": data["name"],
    #     "temp": data["main"]["temp"],
    #     "condition": data["weather"][0]["description"].title(),
    # }

    # get the sunrise and sunrise in the location's local time
    # The method I tried to use has been decommissioned and would not work. Chat in Visual Studio code came up with this.
    # Perhaps try to get the Sunset and make this a function so it does not repeate the code.
        # OpenWeather returns 'sunrise' as a UTC epoch and 'timezone' as seconds offset from UTC
        # Use timezone-aware fromtimestamp to avoid deprecated utcfromtimestamp
    sunrise_utc = dt.datetime.fromtimestamp(data['sys']['sunrise'], tz=dt.timezone.utc)
        # build a timezone for the location using the offset in seconds
    local_tz = dt.timezone(dt.timedelta(seconds=data.get('timezone', 0)))
    sunrise_local = sunrise_utc.astimezone(local_tz)
    print(f'The sunrise (UTC) is: {sunrise_utc}')
    print(f'The sunrise (local) is: {sunrise_local}')
    
    return data

