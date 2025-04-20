# Import required libraries
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables and set base URL for OpenWeather API
API_KEY = os.getenv('WEATHER_API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    """
    Fetch weather data for a given city using OpenWeather API
    Args:
        city (str): Name of the city to get weather for
    Returns:
        dict: Weather information if successful
        str: Error message if request fails
    """
    try:
        # Construct API URL with city name, API key, and metric units
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            # Parse JSON response and extract relevant weather data
            data = response.json()
            weather = {
                'City': data['name'],
                'Temperature': data['main']['temp'],
                'Description': data['weather'][0]['description'],
                'Humidity': data['main']['humidity'],
                'Wind Speed': data['wind']['speed'],
                'Country': data['sys']['country'],
            }
            return weather
        elif response.status_code == 404:
            return 'City not found, please check the city name and try again.'
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def main():
    """
    Main function to run the weather app interface
    """
    # Display welcome message
    print("\nWelcome to the Weather App!")
    print("=" * 30)
    
    # Main program loop
    while True:
        # Get city name from user input
        city_name = input("Enter city name (or type 'exit' to quit): ")
        
        # Check if user wants to exit
        if city_name.lower() == 'exit':
            print("Exiting...")
            break
            
        # Get weather data for the specified city
        result = get_weather(city_name)
        
        # Display weather information if successful
        if isinstance(result, dict):
            print(f"\nWeather for {result['City']}:")
            print(f"Temperature: {result['Temperature']}°C")
            print(f"Description: {result['Description']}")
            print(f"Humidity: {result['Humidity']}%")
            print(f"Wind Speed: {result['Wind Speed']} m/s")
            print(f"Country: {result['Country']}\n")
        else:
            # Display error message if request failed
            print(result)

# Entry point of the program
if __name__ == "__main__":
    main()