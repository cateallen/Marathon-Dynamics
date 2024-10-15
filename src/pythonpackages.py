# Import the needed packages in the Python 3 environment
import pandas as pd
import numpy as np

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

