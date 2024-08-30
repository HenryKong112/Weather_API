import datetime  # Import datetime to handle date and time operations
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import matplotlib.dates as mdates  # Import mdates for handling date formatting in plots
import pandas as pd  # Import pandas for data manipulation
import gui  # Import gui for user interface interactions

def show_graph():
    """
    Display a graph of today's temperature and humidity for the selected location.
    """
    selected_option = gui.option.get()  # Get the selected city/country from the GUI
    df_graph = pd.read_csv(f"{selected_option}_weather.csv")  # Read the weather data from the CSV file
    
    # Convert 'timestamp' column to datetime objects
    df_graph['timestamp'] = pd.to_datetime(df_graph['timestamp'])
    
    # Filter the data to include only today's records
    today = datetime.datetime.now().date()
    df_graph_today = df_graph[df_graph['timestamp'].dt.date == today]
    
    fig, ax1 = plt.subplots()  # Create a figure and a set of subplots

    # Plot temperature data on the primary y-axis
    ax1.plot(df_graph_today['timestamp'], df_graph_today['temperature'], 'r-', linewidth=3, label='Temperature')
    ax1.set_xlabel('Timestamp')  # Set the label for the x-axis
    ax1.set_ylabel('Temperature (°C)', color='r')  # Set the label for the primary y-axis
    ax1.tick_params(axis='y', labelcolor='r')  # Set the color of the y-axis ticks
    
    # Set x-ticks to show hourly intervals
    ax1.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    
    # Create a secondary y-axis for humidity data
    ax2 = ax1.twinx()
    ax2.plot(df_graph_today['timestamp'], df_graph_today['humidity'], 'b--', linewidth=3, label='Humidity')
    ax2.set_ylabel('Humidity (%)', color='b')  # Set the label for the secondary y-axis
    ax2.tick_params(axis='y', labelcolor='b')  # Set the color of the secondary y-axis ticks
    
    # Add a title and improve layout
    plt.title(f"{selected_option}'s Temperature and Humidity Today")
    fig.tight_layout()  # Adjust the layout to prevent overlap
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.grid(True)  # Add a grid to the plot
    plt.show()  # Display the plot