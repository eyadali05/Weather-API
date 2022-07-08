import requests
from secrets import access_key


def get_data(query):
    url = f"http://api.weatherstack.com/current?access_key={access_key}&query={query}"
    r = requests.get(url)
    parsed = r.json()
    return parsed
