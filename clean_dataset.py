# This script is designed to clean JobTech datasets. It will clean and reformat
# the data and prepare it for further use. When the script is finished, a new
# csv-file will be created at the specified location.

# STEP 1:
# Necessary libraries for this script are pandas and tqdm. If they are not already
# installed, use the following commands in your terminal before running this script:
# pip install tqdm
# pip install pandas

from tqdm import tqdm
import pandas as pd

# STEP 2:
# Replace the paths below to correspond with the location of your input dataset and
# the desired location for your cleaned output dataset.
path = 'C:\\Users\\your_username\\Desktop\\name_of_dataset.csv'
output_path = 'C:\\Users\\your_username\\Desktop\\name_of_dataset_cleaned.csv'

# STEP 3:
# Set the year according to your dataset
year = 2023

# STEP 4:
# Run the code :-)

# ----------------------------------------------------------------------------

# Notifies the user that the script has started
print('Loading...')

# Enables a progress bar for the script
tqdm.pandas()

# Loads the desired columns from the dataset
df = pd.read_csv(path, usecols=['description', 'occupation', 'occupation_field', 'workplace_address'])

# Reformats the columns by extracting relevant values from dictionary keys
df['description'] = df['description'].progress_apply(lambda x: eval(x).get('text', ''))
df['occupation'] = df['occupation'].progress_apply(lambda x: eval(x).get('label', ''))
df['occupation_field'] = df['occupation_field'].progress_apply(lambda x: eval(x).get('label', ''))
df['workplace_address'] = df['workplace_address'].progress_apply(lambda x: eval(x).get('city', eval(x).get('municipality', '')))

# Drops rows where 'description' or 'occupation_field' is null
df.dropna(subset=['description', 'occupation_field'], inplace=True)

# Drops rows where 'description' is an empty string
df = df[df['description'] != '']

# Filters rows where 'occupation_field' contains 'data/it'
df = df[df['occupation_field'].str.lower().str.contains('data/it')]

# Defines a list of cities to keep in the dataset and convert to lower case for matching
cities_to_keep = [city.lower() for city in ['Göteborg', 'Stockholm', 'Malmö', 'Uppsala', 'Örebro',
                  'Linköping', 'Helsingborg', 'Jönköping', 'Norrköping', 'Lund']]

# Keeps rows where 'workplace_address' matches a city in 'cities_to_keep'
df = df[df['workplace_address'].str.lower().isin(cities_to_keep)]

# Adds a 'year' column to the dataframe
df['year'] = year

# Removes duplicate rows
df.drop_duplicates(inplace=True)

# Saves the cleaned data to the specified output path
df.to_csv(output_path, index=False)
print('Process completed.')
