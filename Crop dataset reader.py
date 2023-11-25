# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 11:30:13 2023

@author: Subham Divakar
"""
from PIL import Image
import os
import pandas as pd


# Replace 'your_dataset.csv' with the actual file path of your CSV file
file_path = 'Crop_recommendation.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())

# Access specific columns
selected_columns = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'label']]

# Display the selected columns
print(selected_columns.head())

# Find unique labels and their range of rows
label_counts = df['label'].value_counts()
print("Number of unique labels:", len(label_counts))
print("\nLabel counts and their row ranges:")
for label, count in label_counts.items():
    label_rows = df[df['label'] == label].index
    row_range = f"{label_rows.min()} - {label_rows.max()}"
    print(f"Label {label}: Count={count}, Rows={row_range}")
    
    
# Print count of each label
print("\nLabel counts:")
for label, count in label_counts.items():
    print(f"Label {label}: Count={count}")

    
