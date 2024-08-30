import threading  # Import threading to run tasks in parallel
import time  # Import time to handle sleep intervals
import schedule  # Import schedule to manage task scheduling
import api_to_csv as atc  # Import custom module for fetching weather data and saving to CSV
import database as db  # Import custom module for database operations
import gui  # Import custom module for GUI operations

# Initialize the database and fetch initial weather data
db.create_table()  # Create the database table if it doesn't exist
atc.fetch_weather_data()  # Fetch weather data and save to CSV
db.insert_data()  # Insert the fetched data into the database

def run_scheduler():
    """
    Fetch data every 5 minutes and update the database.
    """
    interval = 5  # Set the interval for fetching data
    schedule.every(interval).minutes.do(atc.fetch_weather_data)  # Schedule the fetch_weather_data function
    schedule.every(interval).minutes.do(db.insert_data)  # Schedule the insert_data function
    print(f"Scheduler started. Fetching weather data from Hong Kong and Congo every {interval} minute(s).")
    while True:
        schedule.run_pending()  # Run scheduled tasks
        time.sleep(1)  # Sleep for 1 second before checking again

# Start the scheduler thread
scheduler_thread = threading.Thread(target=run_scheduler)  # Create a new thread for the scheduler
scheduler_thread.start()  # Start the scheduler thread

# Run the GUI
gui.gui_run()  # Start the GUI