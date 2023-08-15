import numpy as np
import matplotlib.pyplot as plt

# Input data for the three curves (12 points each)
voltage_red = np.array([0.24, 0.34, 0.44, 0.55, 0.60, 0.61, 0.62, 0.62, 0.62, 0.62, 0.62, 0.62])
current_red = np.array([0.2, 0.3, 0.4, 1.1, 2.6, 4.3, 5.7, 7.7, 9.6, 11.6, 13.8, 15.7])

voltage_blue = np.array([0.23, 0.32, 0.45, 0.54, 0.58, 0.61, 0.62, 0.62, 0.63, 0.64, 0.64, 0.65])
current_blue = np.array([0.2, 0.3, 0.5, 0.8, 2.3, 3.7, 5.7, 7.6, 9.2, 11.3, 13.1, 15.0])

voltage_green = np.array([0.21, 0.32, 0.45, 0.54, 0.58, 0.61, 0.62, 0.63, 0.63, 0.64, 0.64, 0.65])
current_green = np.array([0.1, 0.3, 0.5, 1.1, 2.5, 3.7, 5.6, 7.4, 9.3, 11.0, 13.0, 14.9])

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(voltage_red, current_red, color='red', label='Red Curve(2V)')
plt.plot(voltage_blue, current_blue, color='blue', label='Blue Curve(6V)')
plt.plot(voltage_green, current_green, color='green', label='Green Curve(10V)')

# Add labels and title
plt.xlabel('Voltage (V)')
plt.ylabel('Current (μA)')
plt.title('Current vs Voltage')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
