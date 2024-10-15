## Loading and preprocessing the data

import pandas as pd
import numpy as np  # Importing the NumPy library for numerical operations and array manipulations
from IPython.display import display  # Import display for better output formatting

# Replace the URLs below with the raw URLs of your CSV files from GitHub
Athletes_file_url = 'https://raw.githubusercontent.com/cateallen/Marathon-Dynamics/refs/heads/main/data/Athletes.csv'
BQStandards_url = 'https://raw.githubusercontent.com/cateallen/Marathon-Dynamics/refs/heads/main/data/BQStandards.csv'
Weather_url = 'https://raw.githubusercontent.com/cateallen/Marathon-Dynamics/refs/heads/main/data/Weather.csv'

# Read the CSV files into DataFrames
data1 = pd.read_csv(Athletes_file_url)
data2 = pd.read_csv(BQStandards_url)
data3 = pd.read_csv(Weather_url)

# Display the first few rows of each DataFrame
print("Data from file 1:")
print(data1.head())

print("\nData from file 2:")
print(data2.head())

print("\nData from file 3:")
print(data3.head())

# Get average weather values for min, max, and mean temps for each zip code
weatherAgg = data3.groupby('Zip').agg(
    Min=('Min Temp', 'mean'),
    Max=('Max Temp', 'mean'),
    Mean=('Mean Temp', 'mean') 
).reset_index()

# Assign bin values based on average min temp
bins = [-20, 30, 40, 50, 60, np.inf]
values = ['< 30F', '30-39F', '40-49F', '50-59F', '>= 60F']
weatherAgg['Min Bins'] = pd.cut(weatherAgg['Min'], bins, labels=values)

# Load the Boston Qualifying (BQ) standards to see if the athlete was on pace to qualify at the halfway point during the race
athletes = pd.merge(left=data1, right=data2, left_on=['Gender', 'Age Group'], right_on=['Gender', 'Age Bracket'])
athletes['BQ Pace'] = athletes.apply(lambda x: True if x['First Half'] < x['Standard'] / 2 else False, axis=1)
athletes.drop('Standard', axis=1, inplace=True)

# Combine the dataframes into one results set that includes weather data and splits
results = pd.merge(left=athletes, right=weatherAgg, how='left')

# Data clean-up step, remove athletes that did not match with weather data
results = results.dropna()

# Make things pretty
results['Zip'] = results['Zip'].astype(str).str.pad(5, 'left', '0')
results['Min'] = results['Min'].round(2)
results['Max'] = results['Max'].round(2)
results['Mean'] = results['Mean'].round(2)
results['Percent Change'] = results['Percent Change'].round(4)

# Change the sort order so that it goes youngest category to older
results['Age Group'] = pd.Categorical(results['Age Group'], ["Under 35", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80 and Over"])

# Display the results
display(results.info())
display(results.head())