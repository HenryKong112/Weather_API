##  Objective:

Recently, I watched a news interview with an African tourist who said that Hong Kong’s summer is hotter than her home place. Thus, I want to compare Hong Kong’s weather with one of a country in Africa — Congo, to see how ridiculous Hong Kong’s weather is.

<img src="Image\hk_so_hot.png">

## Data Source
<img src="Image\Openweather.png">

https://openweathermap.org/api

Parameters:

        weather_data = {
                'city_id': data['id'],  # City ID from the API response
                'city_name': data['name'],  # City name from the API response
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Current timestamp
                'temperature': data['main']['temp'],  # Temperature in Celsius
                'humidity': data['main']['humidity'],  # Humidity percentage
                'weather': data['weather'][0]['description'],  # Weather description
                'feels_like': data['main']['feels_like']  # Feels like temperature in Celsius
            }

## Tools
1. Python
2. SQLite

## Instruction

### 1.  Install or update the packages listed in `requirements.txt`

```
git clone https://github.com/HenryKong112/Weather_API.git
cd Weather_API
pip install --upgrade -r requirements.txt
```

### 2. Create a .env file and put down this code:

    WEATHER_API_KEY=' Enter Your API KEY '

You can get your own API key by register an account on the api website.

### 3. Run the main.py

The system will automatically collect data from the api every <span style="font-size:20px;color: red;">5 minutes</span>.
Then, it fetches the data into a database.
It also store the data in a CSV file for each city / country.
There will be a Graphical User Interface(GUI) too.

<span style="color: yellow;">
📌Only Hong Kong and Republic of the Congo are in these system.
</span>
    

### 4. GUI

 <img src="Image\GUI.png">

 <br>

The GUI is titled with "Weather API".

 * <span style="font-size:20px;color: Green;">Drop down menu 📋:
    
    Selecte city/country code

 * <span style="font-size:20px;color: Green;">"CHECK" button 🛎️

     Button to check and display data below.

 * <span style="font-size:20px;color: Green;">"SHOW STATISTICS" button 🛎️

     Button to show statistics of the selected location in a pop-up window.

<img src="Image\stat.JPG">

 * <span style="font-size:20px;color: Green;">"SHOW GRAPH" button 🛎️

     Button to display a graph of today's temperature and humidity for the selected location.

     <img src="Image\graphexample.png">

## Edit Cities/Countries Options

Please edit:

api_to_csv.py line 9
        
        city_list = ['Hong Kong, HK', 'Republic of the Congo, CG']

database.py line 5

        city_list = ['Hong Kong, HK', 'Republic of the Congo, CG']

gui.py line 13

        city_droplist = ["HK", "CG"]
