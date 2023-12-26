import numpy as np
import pandas as pd

def calculate_weather(a, b, c):
    # Generating 100 equally spaced time values between -10 and 10
    x = np.linspace(-10, 10, 100)     
    y = wind * x**2 + pressure * x + humidity   # Quadratic equation representing weather report

    return x, y

# Reading data from a CSV file named 'single.csv' using pandas
data = pd.read_csv('single.csv')

# Iterating through each row in the CSV file
for index, row in data.iterrows():
    wind = row['a']        # Extracting 'a' column values as wind
    pressure = row['b']    # Extracting 'b' column values as pressure
    humidity = row['c']    # Extracting 'c' column values as humidity

    # Calculating weather data using the extracted wind, pressure, and humidity values
    x_values, y_values = calculate_weather(wind, pressure, humidity)
    
    # Displaying the generated weather data for the current set of inputs
    print(f"Generated Weather Data for Set {index + 1}:")
    for i in range(len(x_values)):
        print(f"x={x_values[i]}, y={y_values[i]}")
