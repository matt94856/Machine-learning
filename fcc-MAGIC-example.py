import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r"C:\Users\matt9\Documents\Sublime Text\Machine Learning Practice\household_power_consumption.txt", delimiter=";")

# Explore the dataset
print(data.head())  # Print the first few rows of the dataset

# Perform further analysis or visualization with the dataset
# Example: Plotting a line graph of global active power
plt.plot(data['Global_active_power'])
plt.xlabel('Time')
plt.ylabel('Global Active Power')
plt.title('Household Power Consumption')
plt.show()
