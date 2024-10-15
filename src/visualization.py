## Data Visualization Section
import pandas as pd
import numpy as np

# Create a histogram of the number of runners by minimum temp
subset = results[['Bib', 'Min']].copy()  # Create a copy to avoid SettingWithCopyWarning
subset['Min'] = subset['Min'].round(0).astype(int)  # Round and convert to int

# Group by 'Min' and count the number of 'Bib' entries
histo = subset.groupby('Min')['Bib'].count().reset_index(name='Finishers')

import pandas as pd
from tabulate import tabulate  # Ensure you have this import

# Disaggregate the correlations by gender and age group
corrs = results.groupby(['Gender', 'Age Group'], observed=False)[['First Half', 'Percent Change']].corr().reset_index()

# Filter for 'First Half' correlations
corrs = corrs.loc[corrs['level_2'] == 'First Half']

# Exclude certain age groups
corrs = corrs.loc[~corrs['Age Group'].isin(['70-74', '75-79', '80 and Over'])]

# Round the 'Percent Change' values
corrs['Percent Change'] = corrs['Percent Change'].round(3)

# Replace gender codes with full names
corrs['Gender'] = corrs['Gender'].replace({'M': 'Men', 'F': 'Women'})

# Pivot the DataFrame
corrs_pivot = corrs.pivot(index='Age Group', columns='Gender', values='Percent Change')

# Is there a correlation between the min temp and the change in pace?
# subset = results.loc[(results['First Half'] < 5400)]
corrs = results.groupby(['Gender', 'Age Group'])[['Min', 'Percent Change']].corr().reset_index()
corrs = corrs.loc[corrs['level_2'] == 'Min']
corrs = corrs.loc[~corrs['Age Group'].isin(['70-74', '75-79', '80 and Over'])]
corrs['Percent Change'] = corrs['Percent Change'].round(3)
corrs['Gender'] = corrs['Gender'].replace({'M' : 'Men', 'F' : 'Women'})
corrs = pd.pivot(data=corrs, index='Age Group', columns='Gender', values='Percent Change')

# Is there a correlation between the max temp and the change in pace?
corrs = results.groupby(['Gender', 'Age Group'], observed=False)[['Max', 'Percent Change']].corr().reset_index()

# Filter for 'Max' correlations
corrs = corrs.loc[corrs['level_2'] == 'Max']

# Exclude certain age groups
corrs = corrs.loc[~corrs['Age Group'].isin(['70-74', '75-79', '80 and Over'])]

# Round the 'Percent Change' values
corrs['Percent Change'] = corrs['Percent Change'].round(3)

# Replace gender codes with full names
corrs['Gender'] = corrs['Gender'].replace({'M': 'Men', 'F': 'Women'})

# Pivot the DataFrame
corrs = pd.pivot(data=corrs, index='Age Group', columns='Gender', values='Percent Change')


# Is there a correlation between mean temperature and the change in pace?
corrs = results.groupby(['Gender', 'Age Group'], observed=False)[['Mean', 'Percent Change']].corr().reset_index()

# Filter for 'Mean' correlations
corrs = corrs.loc[corrs['level_2'] == 'Mean']

# Exclude certain age groups
corrs = corrs.loc[~corrs['Age Group'].isin(['70-74', '75-79', '80 and Over'])]

# Pivot the DataFrame
corrs = pd.pivot(data=corrs, index='Age Group', columns='Gender', values='Percent Change')

# Print the pivoted DataFrame using tabulate

# How does the median change vary with gender, age group, and min temp?
median = results.groupby(['Gender', 'Age Group', 'Min Bins'], observed=False)['Percent Change'].median().reset_index()

# Exclude certain age groups
median = median.loc[~median['Age Group'].isin(['70-74', '75-79', '80 and Over'])]

# Round the 'Percent Change' values
median['Percent Change'] = median['Percent Change'].round(3)

# Print the output for men
men = pd.pivot(median.loc[median['Gender'] == 'M'], index='Age Group', columns='Min Bins', values='Percent Change')

# Print the output for women
women = pd.pivot(median.loc[median['Gender'] == 'F'], index='Age Group', columns='Min Bins', values='Percent Change')

# Prepare the data for an output file to create a visualization
output = pd.pivot(median, index=['Gender', 'Age Group'], columns='Min Bins', values='Percent Change').reset_index()
output['Gender'] = output['Gender'].replace({'M': 'Men', 'F': 'Women'})


# Filter to only show men under 35 and export data for scatter plot
subset = results.loc[(results['Gender'] == 'M') & (results['Age Group'] == 'Under 35')]
subset = subset[['First Half', 'Percent Change']]
subset['First Half'] = pd.to_datetime(subset['First Half'], unit='s').dt.strftime('%H:%M:%S')


# Create histogram of runners by percent change in pace
subset = results[['Bib', 'Percent Change']]

bins = [-np.inf, 0, 0.05, 0.10, 0.15, 0.20, 0.25, np.inf]
values = ['Negative', '0 to 5%', '5% to 10%', '10% to 15%', '15% to 20%', '20% to 25%', 'Over 25%']

# Subset['Percent Bins'] = np.select(conditions, values)
subset['Percent Bins'] = pd.cut(subset['Percent Change'], bins, labels=values, include_lowest=True)

# Apply observed=False to groupby
output = subset.groupby('Percent Bins', observed=False)['Bib'].count().reset_index(name='Finishers')

subset = results.groupby(['BQ Pace', 'Gender', 'Min Bins'], observed=False)['Percent Change'].median().reset_index(name='Change')

corrs = results.groupby(['Gender', 'BQ Pace'])[['First Half', 'Percent Change']].corr().reset_index()
corrs = corrs.loc[corrs['level_2'] == 'First Half']
corrs['Percent Change'] = corrs['Percent Change'].round(3)
corrs['Gender'] = corrs['Gender'].replace({'M' : 'Men', 'F' : 'Women'})
corrs = pd.pivot(data=corrs, index='BQ Pace', columns='Gender', values='Percent Change')


corrs = results.groupby(['Gender', 'BQ Pace'])[['Min', 'Percent Change']].corr().reset_index()
corrs = corrs.loc[corrs['level_2'] == 'Min']
corrs['Percent Change'] = corrs['Percent Change'].round(3)
corrs['Gender'] = corrs['Gender'].replace({'M' : 'Men', 'F' : 'Women'})
corrs = pd.pivot(data=corrs, index='BQ Pace', columns='Gender', values='Percent Change')
