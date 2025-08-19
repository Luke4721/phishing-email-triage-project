import pandas as pd
import pathlib
import os
import re

# Set working directory relative to script location
currentdir = pathlib.Path(__file__).resolve().parent
os.chdir(currentdir)
file_path = os.path.join(os.getcwd(), 'data', 'CEAS_08.csv')
print(file_path)

# Load CSV
df = pd.read_csv(file_path)

# Drop rows missing core fields
df.dropna(subset=['sender', 'body', 'label'], inplace=True)

# Normalize text in 'body'
df['body'] = df['body'].str.strip()

# Extract URLs from 'body' into list
url_pattern = r'http[s]?://[^\s,"]+'
df['urls'] = df['body'].apply(lambda x: re.findall(url_pattern, str(x)))

# Convert list in 'urls' to tuple (hashable for drop_duplicates)
df['urls'] = df['urls'].apply(tuple)

# Remove duplicates based on 'urls' field
df = df.drop_duplicates(subset=['urls'])

# Save cleaned CSV
df.to_csv('cleaned_emails.csv', index=False)

# Optional: show unique URLs by flattening tuples
unique_urls = pd.Series([url for urls in df['urls'] for url in urls]).unique()
print(f"Unique URLs extracted: {len(unique_urls)}")
