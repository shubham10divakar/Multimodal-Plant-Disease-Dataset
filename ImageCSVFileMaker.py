# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 11:30:13 2023

@author: Subham Divakar
"""

from PIL import Image
import os
import pandas as pd

# Replace 'your_image_folder' with the actual path to your image folder
image_folder = 'color'

# Create a list to store image paths and corresponding labels
image_paths = []
labels = []

# Iterate through the folders in the image directory
for category in os.listdir(image_folder):
    category_folder = os.path.join(image_folder, category)

    # Check if the item in the folder is a subdirectory (category)
    if os.path.isdir(category_folder):
        # Collect the first 100 images from each category
        category_image_paths = [os.path.join(category_folder, image_name) for image_name in os.listdir(category_folder)][:100]

        # Append the image paths to the list
        image_paths.extend(category_image_paths)

        # Append the labels (category) to the labels list
        labels.extend([category] * len(category_image_paths))

# Create a DataFrame with the first 100 image paths and labels for all categories
data = {'Image Path': image_paths, 'Label': labels}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_file_path = 'image_dataset_all_categories.csv'
df.to_csv(csv_file_path, index=False)

print(f"CSV file saved at: {csv_file_path}")