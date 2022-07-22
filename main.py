
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


finalFilteredData = newFilteredData.loc[newFilteredData['Short description'] != '11']
finalFilteredData = finalFilteredData[finalFilteredData[['Occupation', 'Manner of death']].notnull().all(1)]

print(finalFilteredData)

# Find way to filter out date only descriptions