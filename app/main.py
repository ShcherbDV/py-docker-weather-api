import os
from dotenv import load_dotenv
import requests


load_dotenv()
URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:

    result = requests.get(URL + f"key={API_KEY}&q={FILTERING}")
    data = result.json()

    city = data["location"]["name"]
    temperature = data["current"]["temp_c"]
    country = data["location"]["country"]
    last_update = data["current"]["last_updated"]
    weather_condition = data["current"]["condition"]["text"]

    print(
        f"Performing request to Weather API for city {city}...\n"
        f"{city}/{country} {last_update} Weather: {temperature} Celsius, "
        f"{weather_condition}"
    )


if __name__ == "__main__":
    get_weather()
