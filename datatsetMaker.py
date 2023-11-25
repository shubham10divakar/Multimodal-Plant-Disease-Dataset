# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 11:30:13 2023

@author: Subham Divakar
"""
import pandas as pd

# Replace 'dataset1.csv' and 'dataset2.csv' with the actual file paths of your datasets
file_path1 = 'Crop_recommendation.csv'
file_path2 = 'image_dataset_all_categories.csv'

# Read both datasets into pandas DataFrames
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)

# Assuming both datasets have a 'Label' column
labels1 = df1['label'].unique()
labels2 = df2['Label'].unique()

# Create a mapping dictionary from labels in dataset1 to labels in dataset2
label_mapping = {label1: label2 for label1, label2 in zip(labels1, labels2)}

# Map labels in dataset1 using the created mapping
df1['Mapped Label'] = df1['label'].map(label_mapping)

# Save the updated df1 without the original 'Label' column to a new CSV file
output_file_path = 'mapped_dataset1.csv'
df1.drop(columns=['label'], inplace=True)
df1.to_csv(output_file_path, index=False)

print(f"Mapped DataFrame saved at: {output_file_path}")

# Display the count and range of rows for each label in the final DataFrame
label_counts = df1['Mapped Label'].value_counts()
print("\nMapped Label counts and their row ranges:")
for label, count in label_counts.items():
    label_rows = df1[df1['Mapped Label'] == label].index
    row_range = f"{label_rows.min()} - {label_rows.max()}"
    print(f"Mapped Label {label}: Count={count}, Rows={row_range}")
    
# Merge df1 with df2 based on the 'Mapped Label' column
final_df = pd.merge(df1, df2, left_on='Mapped Label', right_on='Label', how='left')

# Display the count and range of rows for each mapped label in the final DataFrame
label_counts = final_df['Mapped Label'].value_counts()
print("\nMapped Label counts and their row ranges:")
for label, count in label_counts.items():
    label_rows = final_df[final_df['Mapped Label'] == label].index
    row_range = f"{label_rows.min()} - {label_rows.max()}"
    print(f"Mapped Label {label}: Count={count}, Rows={row_range}")

# Save the final DataFrame to a new CSV file
final_output_path = 'plant_disease_multimodal_dataset.csv'
final_df.to_csv(final_output_path, index=False)

print(f"Final DataFrame saved at: {final_output_path}")
