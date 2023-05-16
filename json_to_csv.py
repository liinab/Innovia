# This script converts all json files that are
# located on your desktop to csv format

import os
import pandas as pd
import json
from tqdm import tqdm

# Change this path to your actual desktop path
desktop_path = os.path.expanduser(r"C:\Users\bergs\Desktop")

files = os.listdir(desktop_path)

json_files = [file for file in files if file.endswith('.json')]

for json_file in tqdm(json_files, desc='Converting files', unit='file'):
    with open(os.path.join(desktop_path, json_file), 'r') as f:
        data = json.load(f)
       
    df = pd.DataFrame(data)

    df.to_csv(os.path.join(desktop_path, json_file.replace('.json', '.csv')), index=False)

print("All JSON files on desktop have been converted to CSV.")
