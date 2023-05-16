# This script pre-processes the cleaned datasets and prepares 
# them for analysis by our AI model.

import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tqdm.auto import tqdm

# Loads the data (change line below according to your path)
path = 'C:\\Users\\bergs\\Desktop\\2016-2023_cleaned.csv'
df = pd.read_csv(path)

# Downloads necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Defines preprocessing functions
def clean_text(text):
    # Removes URLs
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    # Removes all digits
    text = re.sub(r'\d+', '', text)
    # Removes punctuations
    text = re.sub(r'\W', ' ', text)
    # Lowercases all text
    text = text.lower()
    return text

def remove_stopwords(text):
    stop_words = set(stopwords.words('swedish'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return ' '.join(filtered_text)

# Applies preprocessing
tqdm.pandas()
df['description'] = df['description'].progress_apply(clean_text)
df['description'] = df['description'].progress_apply(remove_stopwords)

# Saves the processed DataFrame to a new CSV file (change line below according to your desired path)
output_path = 'C:\\Users\\bergs\\Desktop\\full_dataset(2016-2023).csv'
df.to_csv(output_path, index=False)