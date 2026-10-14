#AUTHENTICATION AND API KEYS
# learn how to use the keys safely and learn how to store them in env filer and add that file to .gitignore
## also help write the scripts which handles errors correctly.
# if your api keys ever even in second reach github its already exposed so the only solution is to revoke them completely and immedietely at once.
# APPLY A PUBLIC API KLEY FREE ONE LIKE OPENWEATHER.COM
#

import requests
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
city = 'Machakos'

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print(f"weather in {city} is: temperature={temp}C:, description = {description}:, humidity= {humidity}%")

elif response.status_code == 401:
    print(f"unauthorized{response.status_code}")

elif response.status_code == 404:
    print(f"not found{response.status_code}")

elif response.status_code == 500:
    print(f"server error{response.status_code} try again later kindly")

elif response.status_code == 429:
    print(f"Too many requests, try again later kindly")


else:
    print(f"unexpected error{response.status_code}")
    print(response.text)

