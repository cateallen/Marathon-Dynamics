
    # Import the needed packages in the Python 3 environment
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
    print(\Data from file 1:\)
    print(data1.head())

    print(\\\nData from file 2:\)
    print(data2.head())

    print(\\\nData from file 3:\)
    print(data3.head())

    # Get average weather values for min, max, and mean temps for each zip code
    weatherAgg = data3.groupby('Zip').agg(
        Min=('Min Temp', 'mean'),
        Max=('Max Temp', 'mean'),
        Mean=('Mean Temp', 'mean')
    ).reset_index()\
    
    # Assign bin values based on average min temp\n,
    bins = [-20, 30, 40, 50, 60, np.inf]\
    values = ['< 30F', '30-39F', '40-49F', '50-59F', '>= 60F']
    weatherAgg['Min Bins'] = pd.cut(weatherAgg['Min'], bins, labels=values)
 
    # Load the Boston Qualifying (BQ) standards to see if the athlete was on pace to qualify at the halfway point during the race
    athletes = pd.merge(left=data1, right=data2, left_on=['Gender', 'Age Group'], right_on=['Gender', 'Age Bracket'])
    athletes['BQ Pace'] = athletes.apply(lambda x: True if x['First Half'] < x['Standard'] / 2 else False, axis=1)\
    athletes.drop('Standard', axis=1, inplace=True)

    # Combine the dataframes into one results set that includes weather data and splits
    results = pd.merge(left=athletes, right=weatherAgg, how='left')

    # Data clean-up step, remove athletes that did not match with weather data
    results = results.dropna()

    # Make things pretty\n,
    results['Zip'] = results['Zip'].astype(str).str.pad(5, 'left', '0')
    results['Min'] = results['Min'].round(2)
    results['Max'] = results['Max'].round(2)
    results['Mean'] = results['Mean'].round(2)
    results['Percent Change'] = results['Percent Change'].round(4)

    # Change the sort order so that it goes youngest category to older
    results['Age Group'] = pd.Categorical(results['Age Group'], [\Under 35\, \35-39\, \40-44\, \45-49\, \50-54\, \55-59\, \60-64\, \65-69\, \70-74\, \75-79\, \80 and Over\])


    # Create a histogram of the number of runners by minimum temp
    subset = results[['Bib', 'Min']].copy()  # Create a copy to avoid SettingWithCopyWarning
    subset['Min'] = subset['Min'].round(0).astype(int)  # Round and convert to int

    # Group by 'Min' and count the number of 'Bib' entries\n,
    histo = subset.groupby('Min')['Bib'].count().reset_index(name='Finishers')
 

    # Is there a correlation between time to complete the first half and the percent change in pace?\
  
    import pandas as pd
    from tabulate import tabulate  # Ensure you have this import
    # Disaggregate the correlations by gender and age group
    corrs = results.groupby(['Gender', 'Age Group'], observed=False)[['First Half', 'Percent Change']].corr().reset_index()

    # Filter for 'First Half' correlations
    corrs = corrs.loc[corrs['level_2'] == 'First Half']
 
    # Exclude certain age groups\n,
    corrs = corrs.loc[~corrs['Age Group'].isin(['70-74', '75-79', '80 and Over'])]

    # Round the 'Percent Change' values\n,
    corrs['Percent Change'] = corrs['Percent Change'].round(3)

    # Replace gender codes with full names\n,
    corrs['Gender'] = corrs['Gender'].replace({'M': 'Men', 'F': 'Women'})

    # Pivot the DataFrame\n,
    corrs_pivot = corrs.pivot(index='Age Group', columns='Gender', values='Percent Change')

    
    # Is there a correlation between the min temp and the change in pace?\n,
    # subset = results.loc[(results['First Half'] < 5400)]\n,
    corrs = results.groupby(['Gender', 'Age Group'])[['Min', 'Percent Change']].corr().reset_index()
    corrs = corrs.loc[corrs['level_2'] == 'Min']
    corrs = corrs.loc[~corrs['Age Group'].isin(['70-74', '75-79', '80 and Over'])]
    corrs['Percent Change'] = corrs['Percent Change'].round(3)
    corrs['Gender'] = corrs['Gender'].replace({'M' : 'Men', 'F' : 'Women'})
    corrs = pd.pivot(data=corrs, index='Age Group', columns='Gender', values='Percent Change')

    # Is there a correlation between the max temp and the change in pace?\n,
    corrs = results.groupby(['Gender', 'Age Group'], observed=False)[['Max', 'Percent Change']].corr().reset_index()
    
    # Filter for 'Max' correlations\n,
    corrs = corrs.loc[corrs['level_2'] == 'Max']
    
    # Exclude certain age groups\n,
    corrs = corrs.loc[~corrs['Age Group'].isin(['70-74', '75-79', '80 and Over'])]

    # Round the 'Percent Change' values\n,
    corrs['Percent Change'] = corrs['Percent Change'].round(3)\

    # Replace gender codes with full names\n,
    corrs['Gender'] = corrs['Gender'].replace({'M': 'Men', 'F': 'Women'})

    # Pivot the DataFrame\n,
    corrs = pd.pivot(data=corrs, index='Age Group', columns='Gender', values='Percent Change')

    # Print the pivoted DataFrame using tabulate\n,
    print(tabulate(corrs, headers='keys', tablefmt='psql'))
  
    # Is there a correlation between mean temperature and the change in pace?\n,
    corrs = results.groupby(['Gender', 'Age Group'], observed=False)[['Mean', 'Percent Change']].corr().reset_index()

    # Filter for 'Mean' correlations\n,
    corrs = corrs.loc[corrs['level_2'] == 'Mean']\

    # Exclude certain age groups\n,
    corrs = corrs.loc[~corrs['Age Group'].isin(['70-74', '75-79', '80 and Over'])]

    # Pivot the DataFrame\n,
    corrs = pd.pivot(data=corrs, index='Age Group', columns='Gender', values='Percent Change')

    # Print the pivoted DataFrame using tabulate\n,
    print(tabulate(corrs, headers='keys', tablefmt='psql'))
  
    # How does the median change vary with gender, age group, and min temp?\n,
    median = results.groupby(['Gender', 'Age Group', 'Min Bins'], observed=False)['Percent Change'].median().reset_index()
 
    # Exclude certain age groups\n,
    median = median.loc[~median['Age Group'].isin(['70-74', '75-79', '80 and Over'])]
 
    # Round the 'Percent Change' values\n,
    median['Percent Change'] = median['Percent Change'].round(3)

    # Print the output for men\n,
    men = pd.pivot(median.loc[median['Gender'] == 'M'], index='Age Group', columns='Min Bins', values='Percent Change')
    print(tabulate(men, headers='keys', tablefmt='psql'))
    print()

    # Print the output for women\n,
    women = pd.pivot(median.loc[median['Gender'] == 'F'], index='Age Group', columns='Min Bins', values='Percent Change')
    print(tabulate(women, headers='keys', tablefmt='psql'))
    print()\

    # Prepare the data for an output file to create a visualization\n,
    output = pd.pivot(median, index=['Gender', 'Age Group'], columns='Min Bins', values='Percent Change').reset_index()
    output['Gender'] = output['Gender'].replace({'M': 'Men', 'F': 'Women'})

    print(tabulate(output, headers='keys', tablefmt='psql'))
  
    # Filter to only show men under 35 and export data for scatter plot\n,
    subset = results.loc[(results['Gender'] == 'M') & (results['Age Group'] == 'Under 35')]
    subset = subset[['First Half', 'Percent Change']]\
    subset['First Half'] = pd.to_datetime(subset['First Half'], unit='s').dt.strftime('%H:%M:%S')
 
    # Create histogram of runners by percent change in pace\n,
    subset = results[['Bib', 'Percent Change']]
    
    bins = [-np.inf, 0, 0.05, 0.10, 0.15, 0.20, 0.25, np.inf]
    values = ['Negative', '0 to 5%', '5% to 10%', '10% to 15%', '15% to 20%', '20% to 25%', 'Over 25%']
    
    # Subset['Percent Bins'] = np.select(conditions, values)\n,
    subset['Percent Bins'] = pd.cut(subset['Percent Change'], bins, labels=values, include_lowest=True)
    
    # Apply observed=False to groupby\n,
    output = subset.groupby('Percent Bins', observed=False)['Bib'].count().reset_index(name='Finishers')
 
    subset = results.groupby(['BQ Pace', 'Gender', 'Min Bins'], observed=False)['Percent Change'].median().reset_index(name='Change')
    display(pd.pivot(subset, index='Min Bins', columns=['Gender', 'BQ Pace'], values='Change'))
  
    corrs = results.groupby(['Gender', 'BQ Pace'])[['First Half', 'Percent Change']].corr().reset_index()
    corrs = corrs.loc[corrs['level_2'] == 'First Half']
    corrs['Percent Change'] = corrs['Percent Change'].round(3)
    corrs['Gender'] = corrs['Gender'].replace({'M' : 'Men', 'F' : 'Women'})
    corrs = pd.pivot(data=corrs, index='BQ Pace', columns='Gender', values='Percent Change')

    print(tabulate(corrs, headers='keys', tablefmt='psql'))


    corrs = results.groupby(['Gender', 'BQ Pace'])[['Min', 'Percent Change']].corr().reset_index()
    corrs = corrs.loc[corrs['level_2'] == 'Min']
    corrs['Percent Change'] = corrs['Percent Change'].round(3)
    corrs['Gender'] = corrs['Gender'].replace({'M' : 'Men', 'F' : 'Women'})
    corrs = pd.pivot(data=corrs, index='BQ Pace', columns='Gender', values='Percent Change')

    print(tabulate(corrs, headers='keys', tablefmt='psql'))
