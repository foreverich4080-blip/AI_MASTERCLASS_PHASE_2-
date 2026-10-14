import requests

API_KEY = "rc_live_28a3390a92bd47c291040122f783cbfd"  # paste your key
headers = {"Authorization": f"Bearer {API_KEY}"}

r = requests.get("https://api.restcountries.com/countries/v5/names.common/kenya", headers=headers)
print(r.json())
data = r.json()
print(data["common"])
















BASE_URL = "https://api.open-metro.com/v1/forecast"

latitude = 1.675
longitude = 1.675


params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": (
        "temperature",
        "humidity",
        "pressure",
        "precipitation",
        "wind",
        "clouds",
        "snow",
        "rain",
        "snow",
        "is_day"
    ),

    "timezone": "auto"
}

response = requests.get(BASE_URL, params = params, timeout=20)

if response.status_code != 200:
    print("failed to get the api requests ")
    print("status code", response.status_code)
    print("response", response.text)
    raise SystemExit


if response.status_code == 200:
    data = response.json()
    print(current["wind"]["speed"])













































