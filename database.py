import sqlite3  # Import the SQLite library to handle database operations
import pandas as pd  # Import pandas for data manipulation

# List of cities with their respective country codes
city_list = ['Hong Kong, HK', 'Republic of the Congo, CG']

def create_table():
    """
    Create a table in the SQLite database.
    """
    conn = sqlite3.connect('weather_api.db')  # Connect to the SQLite database
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weatherapi(
            city_id INTEGER,  
            city_name VARCHAR(256),  
            timestamp DATETIME,  
            temperature FLOAT,  
            humidity FLOAT,  
            weather VARCHAR(256),  
            feels_like FLOAT  
        );
    ''')  # SQL command to create the table if it doesn't exist
    conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection

def insert_data():
    """
    Insert data from CSV files into the SQLite database.
    """
    for city in city_list:
        city_name = city.split(',')[1].strip()  # Extract the country code (e.g., "HK")
        df = pd.read_csv(f'{city_name}_weather.csv')  # Read the CSV file for the city
        conn = sqlite3.connect('weather_api.db')  # Connect to the SQLite database
        cursor = conn.cursor()  # Create a cursor object to execute SQL commands
        for row in df.itertuples():  # Iterate over each row in the DataFrame
            cursor.execute(
                """
                INSERT INTO weatherapi (city_id, city_name, timestamp, temperature, humidity, weather, feels_like)
                VALUES (?,?,?,?,?,?,?)
                """,
                (row.city_id, row.city_name, row.timestamp, row.temperature, row.humidity, row.weather, row.feels_like)
            )  # Insert the data into the table

        conn.commit()  # Commit the transaction
        conn.close()  # Close the database connection

if __name__ == "__main__":
    create_table()  # Create the table
    insert_data()  # Insert the data