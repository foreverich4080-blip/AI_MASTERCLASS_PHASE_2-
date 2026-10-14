import requests
from dotenv import load_dotenv
import os

from WEEK1.day1 import response

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
city = 'NEW YORK'

if not api_key:
    print("no api key provided from .env file")


url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response= requests.get(url)
data = response.json()


if response.status_code == 200:
    print(data["weather"][0]["description"])
    print(data["main"]["humidity"])
    print(data["main"]["pressure"])

elif response.status_code == 400:
    print(f"unauthorized {response.status_code}")

elif response.status_code == 500:
    print(f"server error {response.status_code} try again later")

elif response.status_code == 429:
    print(f"rate limit {response.status_code} try again later and avoid topo many requests at a time")

else:
    print(f"unknown error {response.status_code}")
    print(response.text)


