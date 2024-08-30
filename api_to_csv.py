import csv  # Import the CSV module to handle CSV file operations
import os  # Import the OS module to interact with the operating system
import requests  # Import the requests module to make HTTP requests
from datetime import datetime  # Import datetime to handle date and time
from dotenv import load_dotenv
# API key for accessing the weather data
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
# List of cities with their respective country codes
city_list = ['Hong Kong, HK', 'Republic of the Congo, CG']
# Parameters to be included in the CSV file
parameters = ['city_id', 'city_name', 'timestamp', 'temperature', 'humidity', 'weather', 'feels_like']

def fetch_weather_data():
    # Collect data from API and convert JSON data into CSV.
    for city in city_list:
        city_name = city.split(',')[1].strip()  # Extract the country code (e.g., "HK")
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(api_url.format(API_KEY), timeout=10)  # Make a GET request to the API
        if response.status_code == 200:  # Successfully retrieve data
            data = response.json()  # Parse the JSON response
            weather_data = {
                'city_id': data['id'],  # City ID from the API response
                'city_name': data['name'],  # City name from the API response
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Current timestamp
                'temperature': data['main']['temp'],  # Temperature in Celsius
                'humidity': data['main']['humidity'],  # Humidity percentage
                'weather': data['weather'][0]['description'],  # Weather description
                'feels_like': data['main']['feels_like']  # Feels like temperature in Celsius
            }

            csv_filename = f'{city_name}_weather.csv'
            if not os.path.exists(csv_filename):  # If the CSV file does not exist, create it and write the header
                with open(csv_filename, 'w', newline='', encoding='utf-8') as output_file:
                    dict_writer = csv.DictWriter(output_file, fieldnames=parameters)
                    dict_writer.writeheader()  # Write the header row
                    dict_writer.writerow(weather_data)  # Write the weather data
            else:  # Otherwise, append data to the existing file
                with open(csv_filename, 'a', newline='', encoding='utf-8') as output_file:
                    dict_writer = csv.DictWriter(output_file, fieldnames=parameters)
                    dict_writer.writerow(weather_data)  # Append the weather data
        else:
            print(f"Failed to fetch data: {response.status_code}")  # Fail to retrieve data

if __name__ == "__main__":
    fetch_weather_data()  # Fetch and save the weather data