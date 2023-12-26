import numpy as np
import pandas as pd

def calculate_weather(a, b, c):
    # Generate x and y for representing time and temperature
    x = np.linspace(-10, 10, 100)  
    y = wind * x**2 + pressure * x + humidity  # Quadratic equation representing weather report

    return x, y

# Read data from a CSV file using pandas
data = pd.read_csv('multiple.csv')

# Iterate through each row in the data
for index, row in data.iterrows():
    wind = row['a']        # Extract wind value from the 'a' column in the current row
    pressure = row['b']    # Extract pressure value from the 'b' column in the current row
    humidity = row['c']    # Extract humidity value from the 'c' column in the current row

    # Calculate weather data using the extracted wind, pressure, and humidity values
    x_values, y_values = calculate_weather(wind, pressure, humidity)
    
    # Display the generated weather data for the current set of inputs
    print(f"Generated Weather Data for Set {index + 1}:")
    for i in range(len(x_values)):
        print(f"x={x_values[i]}, y={y_values[i]}")
