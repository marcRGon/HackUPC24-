import pandas as pd
from image_embeddings import extract_features
from utils import is_nan
import os
from warnings import simplefilter
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

image_dir = '../../../dataset'

# Read the CSV file
df = pd.read_csv('inditextech_hackupc_challenge_images.csv')

# Define a function to extract the file name from the URL
def extract_file_name(url):
    filename = os.path.basename(url).split('/')[-1]
    filename = filename.split('?')[0]
    return filename

def create_row(index, column_name, version):
    if is_nan(row[column_name]):
        return None
    file_name = extract_file_name(row[column_name])
    # Construct the path to the file in the given directory
    image_path = os.path.join(image_dir, file_name)
    # Extract features from the image using the file path
    vector = extract_features(image_path)
    # If vector is None, return None
    if vector is None:
        return None
    new_row = pd.DataFrame({
        'index': [index],
        'url': [row[column_name]],
        'version': [version]
    })
    # Add a column for every element of the vector in order.
    for i, value in enumerate(vector):
        new_row[f'vector_{i}'] = [value]
    return new_row

# Create a new DataFrame to store the results
columns = ['index', 'url', 'version'] + [f'vector_{i}' for i in range(0, 1000)]

result_df = pd.DataFrame(columns=columns)

# Iterate over each row in the original DataFrame
for index, row in df.iterrows():
    #if index >= 10:
    #    break
    # Extract the file name from the URL
    row0 = create_row(index, 'IMAGE_VERSION_1', 0)
    row1 = create_row(index, 'IMAGE_VERSION_2', 1)
    row2 = create_row(index, 'IMAGE_VERSION_3', 2)
    # Append the row to the result DataFrame if each row is not None
    if row0 is not None:
        result_df = pd.concat([result_df, row0], ignore_index=True)
    if row1 is not None:
        result_df = pd.concat([result_df, row1], ignore_index=True)
    if row2 is not None:
        result_df = pd.concat([result_df, row2], ignore_index=True)
    print(f"Processed {index+1}/{len(df)} rows.")
    if index % 100 == 0:
        result_df.to_csv('image_embeddings.csv', index=False)

# Save the result DataFrame as a CSV file
result_df.to_csv('image_embeddings.csv', index=False)