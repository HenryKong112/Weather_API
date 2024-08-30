import pandas as pd  # Import pandas for data manipulation
from tkinter import *  # Import all tkinter modules for GUI
from tkinter import ttk  # Import ttk for themed widgets
import tkinter as tk  # Import tkinter with an alias
import weather_graph as wg  # Import custom module for weather graph functions

# Create the main window - GUI - Graphical User Interface
root = tk.Tk()
root.title("Weather API")  # Set the title of the window
root.geometry("1650x400")  # Set the size of the window

# Dropdown menu for selecting the city
city_droplist = ["HK", "CG"]  # List of city codes
option = tk.StringVar(root)  # Create a StringVar to hold the selected option
option.set(city_droplist[0])  # Set the default value to the first city code
city_dropdown = ttk.Combobox(root, textvariable=option, values=city_droplist)  # Create a dropdown menu
city_dropdown.grid(row=1, column=1)  # Place the dropdown menu in the grid

# Treeview widget to display CSV data
tree = ttk.Treeview(root, columns=("Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7"), show="headings")
tree.heading("Column1", text="City_ID")
tree.heading("Column2", text="City_Name")
tree.heading("Column3", text="Timestamp")
tree.heading("Column4", text="Temperature")
tree.heading("Column5", text="Humidity")
tree.heading("Column6", text="Weather")
tree.heading("Column7", text="Feels_Like")
tree.grid(row=4, column=1, columnspan=10)  # Place the treeview in the grid

def gui_run():
    def check():
        """
        Function for the 'Check' button to update the treeview with data from the selected city's CSV file.
        """
        selected_option = option.get()  # Get the selected city/country code
        file_path = f"{selected_option}_weather.csv"  # Construct the file path for the CSV file
        df_treeview = pd.read_csv(file_path)  # Read the CSV file into a DataFrame
        
        # Clear existing data in the treeview
        for row in tree.get_children():
            tree.delete(row)
        
        # Insert new data into the treeview
        for index, row in df_treeview.iterrows():
            tree.insert("", "end", values=list(row))

    def stat():
        """
        Function to display statistics for the selected city's weather data.
        """
        selected_option = option.get()  # Get the selected city/country code
        df = pd.read_csv(f"{selected_option}_weather.csv")  # Read the CSV file into a DataFrame

        # Calculate statistics for temperature
        temperature_mean = df['temperature'].mean()
        temperature_median = df['temperature'].median()
        temperature_mode = df['temperature'].mode()[0]
        temperature_range = df['temperature'].max() - df['temperature'].min()
        temperature_variance = df['temperature'].var()
        temperature_std_dev = df['temperature'].std()

        # Calculate statistics for humidity
        humidity_mean = df['humidity'].mean()
        humidity_median = df['humidity'].median()
        humidity_mode = df['humidity'].mode()[0]
        humidity_range = df['humidity'].max() - df['humidity'].min()
        humidity_variance = df['humidity'].var()
        humidity_std_dev = df['humidity'].std()

        # Calculate statistics for feels_like
        feels_like_mean = df['feels_like'].mean()
        feels_like_median = df['feels_like'].median()
        feels_like_mode = df['feels_like'].mode()[0]
        feels_like_range = df['feels_like'].max() - df['feels_like'].min()
        feels_like_variance = df['feels_like'].var()
        feels_like_std_dev = df['feels_like'].std()

        stats_text = (  # Stats
            f"City / Country: {selected_option}\n"
            f"Temperature Statistics:\n"
            f"Mean: {temperature_mean}\n"
            f"Median: {temperature_median}\n"
            f"Mode: {temperature_mode}\n"
            f"Range: {temperature_range}\n"
            f"Variance: {temperature_variance}\n"
            f"Standard Deviation: {temperature_std_dev}\n\n"
            f"Humidity Statistics:\n"
            f"Mean: {humidity_mean}\n"
            f"Median: {humidity_median}\n"
            f"Mode: {humidity_mode}\n"
            f"Range: {humidity_range}\n"
            f"Variance: {humidity_variance}\n"
            f"Standard Deviation: {humidity_std_dev}\n\n"
            f"Feels Like Statistics:\n"
            f"Mean: {feels_like_mean}\n"
            f"Median: {feels_like_median}\n"
            f"Mode: {feels_like_mode}\n"
            f"Range: {feels_like_range}\n"
            f"Variance: {feels_like_variance}\n"
            f"Standard Deviation: {feels_like_std_dev}\n"
        )

        # Pop out a window to show statistics of a city/country 
        stat_pop_win = tk.Tk()  # Create a new Tkinter window
        stat_pop_win.geometry("700x500")  # Set the size of the window
        stat_pop_win.title("Show Statistics")  # Set the title of the window
        
        # Create a label to display the statistics text
        Label(stat_pop_win, text=stats_text, justify="left", font=("Arial", 12)).pack()
        
        # Start the event loop for the statistics window
        stat_pop_win.mainloop()
        
    
    # Labels
    city_label = tk.Label(root, text="City/Country:")  # Label for city/country selection
    city_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")  # Place the label in the grid

    interval_label = tk.Label(root, text="Interval(min): ")  # Label for interval input
    interval_label.grid(row=2, column=0)  # Place the label in the grid

    interval_Time_label = tk.Label(root, text=" every 5 minute ")  # Label indicating the interval time
    interval_Time_label.grid(row=2, column=1)  # Place the label in the grid

    record_label = tk.Label(root, text="Record:")  # Label for record display
    record_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")  # Place the label in the grid

    # Buttons
    check_btn = tk.Button(root, text="CHECK", command=check)  # Button to check and display data
    check_btn.grid(row=1, column=3)  # Place the button in the grid

    stat_btn = tk.Button(root, text="SHOW STATISTICS", command=stat)  # Button to show statistics
    stat_btn.grid(row=1, column=4)  # Place the button in the grid

    graph_btn = tk.Button(root, text="SHOW GRAPH", command=wg.show_graph)  # Button to show graph
    graph_btn.grid(row=1, column=5)  # Place the button in the grid

    # Run the main loop
    root.mainloop()  # Start the GUI event loop

if __name__ == "__main__": 
    gui_run()  # Run the GUI