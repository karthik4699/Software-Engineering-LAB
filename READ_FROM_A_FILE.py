import numpy as np

def calculate_weather(a, b, c):
    # Generating 100 evenly spaced values between -10 and 10 for representing time
    x = np.linspace(-10, 10, 100)
    
    # Using input parameters a, b, and c to calculate y values based on a quadratic equation
     y = wind * x**2 + pressure * x + humidity  # Quadratic equation representing weather conditions

    return x, y

# Setting values for wind, pressure, and humidity (these can be loaded from files in practice)
wind = 4
pressure = 1
humidity = 3

# Calling the calculate_weather function with the given wind, pressure, and humidity values
x_values, y_values = calculate_weather(wind, pressure, humidity)

# Displaying the generated weather data for the single set of inputs
print("Generated Weather Data for a Single Set of Inputs:")
for i in range(len(x_values)):
    print(f"x={x_values[i]}, y={y_values[i]}")

