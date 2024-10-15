#### About each of the data sources for this project

### Athletes.csv
- The age groups align with the age groups used by the BAA for qualifying purposes. The youngest age group is under 35 and the oldest age group is 80 years or more. All other age groups are five year increments (i.e. 40-44).
- Each athlete's record also includes results data.
- First Half is the amount of time, in seconds, it took them to complete the first half of the marathon.
- Second Half is the amount of time, in seconds, it took them to complete the second half of the marathon.
- Finish is the total amount of time, in seconds, it took them to complete the marathon.
- Positive Split is the difference, in seconds, of Second Half and First Half. A positive number means the athlete was slower in the second half, while a negative number means the athlete was faster in the second half.
- Percent Change is a calculation of Positive Split as a percent of the First Half. A percent change of 1% indicates that the second half took an additional 1% longer than the first half.

## Columns in Athletes.csv
- Bib (Unique identifier for each athlete)
- Zip (Five digit zip code w/o the leading zeros)
- Age (Actual age of the athlete in years)
- Age group (Age group based on BAA qualifying standards)
    - Under 35 = 31% / 40-44 = 14% / Other (56%)
- Gender (Male(M), or Female (F))
- First Half (Time in seconds to complete the first half of the race)
- Second half (Time in seconds to complete the second half of the race)
- Finish (Time in seconds to complete the full race)
- Postiive Split (Difference between seconds half and first half denoted in seconds)
- Percent Change (Positive Split as a percent of First Half)

### BQStandards.csv
- This file contains the Boston qualifying time, in seconds for each age group and gender.
- These qualifying times have been in effect since 2020 and can be found on the BAA website

## Columns in BQStandards.csv
- Gender (Male (M) 0r Female (F))
- Age Bracket (The age group used by BAA - from 18-34 to 80+)
- Standard (The qualifying time in seconds)

### Weather.csv
- This file contains daily weather data for each zip code represented in the Athletes file.
- The time period covers the two weeks prior to the 2024 Boston Marathon (April 1 to April 15). Each row includes the min temp, max temp, and mean temp, for an individual day in an individual zip code.

## Columns in Weather.csv
- Date (Date of weather measurement)
- Max Temp (Max daily temp in F)
- Min Temp (Min daily temp in F)
- Mean Temp (Average daily temp in F)
- Zip (Five digit zip code w/0 leading zeros of the location)