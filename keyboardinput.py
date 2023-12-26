import numpy as np

def calculate_weather(a, b, c):
    # Generate 100 evenly spaced values between -10 and 10 for representing time
    x = np.linspace(-10, 10, 100)  
    
    # Calculate weather conditions (y) based on a quadratic equation using input parameters a, b, and c
    y = wind * x**2 + pressure * x + humidity  # Quadratic equation representing weather conditions

    return x, y

# Request user input for coefficients of wind, pressure, and humidity
wind = float(input("Enter coefficient of wind: "))
pressure = float(input("Enter coefficient of pressure: "))
humidity = float(input("Enter coefficient of humidity: "))

# Calculate weather data using the provided coefficients
x_values, y_values = calculate_weather(wind, pressure, humidity)

# Display the generated weather data for the single set of inputs
print("Generated Weather Data for a Single Set of Inputs:")
for i in range(len(x_values)):
    print(f"x={x_values[i]}, y={y_values[i]}")

