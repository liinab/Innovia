import pandas as pd
import os
import re
from tqdm import tqdm

# Define the path to your file
path = r'C:\Users\bergs\Desktop\full_dataset(2016-2023).csv'

# Check if the file exists
if os.path.exists(path):
    # Read the csv file
    df = pd.read_csv(path)
    
    # Define keywords related to IT-security
    keywords = ['informationssäkerhet', 'cybersäkerhet', 'driftsäkerhet', 'malware', 
                'cyber security', 'cybersecurity', 'virus', 'it säkerhet', 'it security', 'databreach', 
                'databreach', 'information security', 'informationsecurity', 'informationcyber', 'ransomware', 
                'säkerhetstest', 'cyberhot', 'cyberattack', 'cyber attack', 'firewall', 
                'brandvägg', 'kryptering', 'datasäkerhet', 'encryption', 'phishing', 
                'nätverkssäkerhet', 'network security', 'networksecurity', 'dataskydd', 
                'cyber', 'systemsäkerhet', 'system security', 'DDoS', 
                'pharming', 'botnet', 'botnät', 'lösenordsfisk', 'keylogging', 'hijack', 
                'dataintrång', 'webbutvecklingsattack', 'web application attack', 
                'cyber utpressning', 'cyberutpressning' 'cyberangrepp', 'it attack', 
                'itattack', 'cyberattack', 'cyber hot', 'ethical hacking', 'attack',
                'distributed denial of service attack', 'säkerhet',
                'security', 'intrusion', 'informationssekretess', 'spyware', 'spion',
                'malicious', 'security threat', 'rootkit', 'unauthorized access', 'vulnerabilit',
                'darknet']

    # Combine them into a single regular expression
    regex_pattern = '|'.join(keywords)

    # Create a new column 'it_security' and apply the regular expression to the 'description' column
    tqdm.pandas(desc="Processing")
    df['it_security'] = df['description'].progress_apply(lambda x: 1 if re.search(regex_pattern, str(x), re.IGNORECASE) else 0)

    # Save the new dataframe to a new csv file
    df.to_csv(r'C:\Users\bergs\Desktop\training_dataset(2016-2023).csv', index=False)
    
    print("The file has been processed and saved as 'training_dataset(2016-2023).csv'.")
else:
    print('The file does not exist.')


