import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import datetime

# Generate some random data for each day of the year
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', end='2023-12-31')
data = pd.Series(np.random.randn(len(dates)), index=dates)

# Reshape the data into a matrix where each row represents a week and each column represents a day
data_matrix = data.values.reshape(73, 5)

# Get the week numbers for each row
week_numbers = data.index.weekofyear[:364:7]

# Create a dataframe with the data matrix and week numbers
df = pd.DataFrame(data_matrix, index=week_numbers)

# Create a dictionary to map the day of the week to its name

# Use the map function to replace the day of the week integer with the day name
df.columns = df.columns.map(day_names)

# Create a calendar heatmap with dates
sns.set()
fig, ax = plt.subplots(figsize=(10, 7))
sns.heatmap(df, cmap='coolwarm', ax=ax, annot=True, fmt='d', cbar=False)
ax.set_title('Calendar Heatmap with Dates')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Week Number')
plt.show()
