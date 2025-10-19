import os
from dotenv import load_dotenv
import requests


load_dotenv()
URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError(
        "API_KEY not found! Ensure you have set up "
        "your API key throw Docker or in .env file."
    )


def get_weather() -> None:

    result = requests.get(URL + f"key={API_KEY}&q={FILTERING}")
    result.raise_for_status()
    data = result.json()

    city = data.get("location").get("name")
    temperature = data.get("current").get("temp_c")
    country = data.get("location").get("country")
    last_update = data.get("current").get("last_updated")
    weather_condition = data.get("current").get("condition").get("text")

    print(
        f"Performing request to Weather API for city {city}...\n"
        f"{city}/{country} {last_update} Weather: {temperature} Celsius, "
        f"{weather_condition}"
    )


if __name__ == "__main__":
    get_weather()
