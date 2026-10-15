"""
Travel Weather Tool
===================

A command-line tool that fetches live weather information for a city
and combines it with country information from a second API.

APIs used:
1. OpenWeather API - provides live weather data.
2. REST Countries API - provides country information.

How to run:
1. Install the required packages:
       pip install requests python-dotenv

2. Create a .env file in the same folder as this script:
       OPENWEATHER_API_KEY=your_api_key_here

3. Add .env to .gitignore so your API key is never pushed to GitHub.

4. Run the program:
       python travel_weather_tool.py

5. Enter a city when prompted.

The program displays a clean summary and saves the combined API
response to a JSON file.
"""

import json
import os

import requests
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    """
    Fetch live weather information for a city from OpenWeather.

    Returns:
        dict: Weather data if successful.
        None: If the request fails.
    """

    if not API_KEY:
        print("Error: OPENWEATHER_API_KEY was not found in the .env file.")
        return None

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 404:
            print(f"Could not find the city '{city}'.")
        elif response.status_code == 401:
            print("Error: Invalid OpenWeather API key.")
        else:
            print(
                f"Weather API error. "
                f"Status code: {response.status_code}"
            )

    except requests.exceptions.RequestException as error:
        print(f"Could not connect to the weather API: {error}")

    return None


def get_country_info(country_code):
    """
    Fetch country information from the REST Countries API.

    Returns:
        dict: Country information if successful.
        None: If the request fails.
    """

    url = f"https://restcountries.com/v3.1/alpha/{country_code}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            countries = response.json()

            if countries:
                return countries[0]

        print(
            f"Could not retrieve country information "
            f"for code {country_code}."
        )

    except requests.exceptions.RequestException as error:
        print(f"Could not connect to the country API: {error}")

    return None


def save_to_file(data, filename):
    """
    Save combined API data to a JSON file.
    """

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(f"\nCombined data saved to: {filename}")

    except OSError as error:
        print(f"Could not save the JSON file: {error}")


def display_results(city, weather_data, country_data):
    """
    Display the combined information in a clean format.
    """

    main_weather = weather_data.get("main", {})
    weather_description = weather_data.get("weather", [{}])[0]
    wind = weather_data.get("wind", {})
    system = weather_data.get("sys", {})

    temperature = main_weather.get("temp", "N/A")
    feels_like = main_weather.get("feels_like", "N/A")
    humidity = main_weather.get("humidity", "N/A")

    condition = weather_description.get(
        "description",
        "N/A"
    ).title()

    wind_speed = wind.get("speed", "N/A")
    wind_direction = wind.get("deg", "N/A")

    country_name = country_data.get("name", {}).get(
        "common",
        "Unknown"
    )

    region = country_data.get("region", "Unknown")
    subregion = country_data.get("subregion", "Unknown")
    population = country_data.get("population", "Unknown")

    currencies = country_data.get("currencies", {})

    if currencies:
        currency_names = []

        for currency_code, currency_info in currencies.items():
            currency_name = currency_info.get(
                "name",
                currency_code
            )
            currency_names.append(
                f"{currency_name} ({currency_code})"
            )

        currency_display = ", ".join(currency_names)

    else:
        currency_display = "Unknown"

    print("\n" + "=" * 50)
    print("             TRAVEL WEATHER REPORT")
    print("=" * 50)

    print(f"\nLocation: {city.title()}, {country_name}")

    print("\n--- WEATHER ---")
    print(f"Temperature : {temperature} °C")
    print(f"Feels Like  : {feels_like} °C")
    print(f"Condition   : {condition}")
    print(f"Humidity    : {humidity}%")
    print(f"Wind Speed  : {wind_speed} m/s")
    print(f"Wind Direction: {wind_direction}°")

    print("\n--- COUNTRY ---")
    print(f"Country     : {country_name}")
    print(f"Region      : {region}")
    print(f"Subregion   : {subregion}")
    print(f"Population  : {population:,}")
    print(f"Currency    : {currency_display}")

    print("\n" + "=" * 50)


def run_tool():
    """
    Main program workflow.
    """

    print("\n" + "=" * 50)
    print("             TRAVEL WEATHER TOOL")
    print("=" * 50)

    city = input("\nEnter a city: ").strip()

    if not city:
        print("No city was entered. Exiting program.")
        return

    print(f"\nFetching live information for {city.title()}...")

    # API CALL 1
    weather_data = get_weather(city)

    if weather_data is None:
        print("Unable to retrieve weather information.")
        return

    # Extract country code from first API response
    country_code = weather_data.get("sys", {}).get("country")

    if not country_code:
        print("The weather API did not provide a country code.")
        return

    # API CALL 2
    country_data = get_country_info(country_code)

    if country_data is None:
        print("Unable to retrieve country information.")
        return

    # Combine the results from both APIs
    combined_data = {
        "city": city,
        "country_code": country_code,
        "weather": weather_data,
        "country": country_data
    }

    # Display clean information
    display_results(
        city,
        weather_data,
        country_data
    )

    # Save combined response
    filename = f"{city.lower().replace(' ', '_')}_travel_data.json"

    save_to_file(
        combined_data,
        filename
    )


if __name__ == "__main__":
    run_tool()