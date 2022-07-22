
"""
Primary goal is to get a decisive list of names of individuals who have lived extremely long and/or very short lives, and then 
these names can be conveniently accessed (likely in a .txt file) to be further researched at a later time
"""

# Pandas will be the primary tool to extract data 
import pandas as pd

primaryDataFrame = pd.read_csv('AgeDataset-V1.csv')

# Variable to hold the array of columns for the data frame for easy reference
arrayOfColumns = primaryDataFrame.columns

# New data frame with filtered data
newFilteredData = primaryDataFrame.loc[(primaryDataFrame['Age of death'] >= 90) | (primaryDataFrame['Age of death'] <= 21)]

# Occupations of filtered individuals
importantOccupations = newFilteredData['Occupation']

"""

Can be uncommented to loop through occupations

for index, value in importantOccupations.items():
    print(str(index) + "\t" + str(value))

"""
"""

Can be uncommented to loop through Names, occupations, and short descriptions of filtered individuals

for index, row in newFilteredData.iterrows():
    print(index, row['Name'], row['Occupation'], row['Short description'])

"""

# Data that has been further filtered to exclude indivduals without a stated occupation AND a stated short description


# Filters the data so that all the people with unaccounted for occupations, manners of death, and country are excluded (Data set is too large to worry about these individuals)
finalFilteredData = newFilteredData[newFilteredData[['Occupation', 'Manner of death', 'Country']].notnull().all(1)]

# Filters out anyone without a short description
finalFilteredData = finalFilteredData[(finalFilteredData['Short description'].str.len() > 11) | finalFilteredData['Short description'].notnull()]

# Sorts the rows in ascending order based off birth year (earliest births are at bottom of the dataframe)
finalFilteredSortedData = finalFilteredData.sort_values(by='Birth year', ascending=True)


"""
for index, row in finalFilteredSortedData.iterrows():
    print(index, row['Birth year'])
"""

print(finalFilteredSortedData.tail)
