import pandas as pd
import numpy as np
import os
from numpy import int64

threshold = 40

def calculate_distance(embedding1, embedding2):
    # Given two 1000 element dense vectors embedding1 and embedding2 as numpy arrays, calculate the Euclidean distance between them.
    distance = np.sqrt(np.sum((embedding1 - embedding2)**2))
    return distance

def find_files_with_low_distance(index, version):
    def read_embedding(row):
        embedding = np.zeros(1000)
        for i in range(0, 1000):
            #print(row[f'vector_{i}'])
            embedding[i] = row[f'vector_{i}']
        return embedding
    
    duplicates = []

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv('image_embeddings_test.csv')
    # Take the row corresponding to the given index and version
    filtered_df = df[(df['index'] == int64(index)) & (df['version'] == int64(version))]
    if not filtered_df.empty:
        reference = filtered_df.iloc[0]
        reference_embedding = read_embedding(reference)
    else:
        print(f"No rows found with index {index} and version {version}")
        return []
    #reference = df[df['index'] == index][df['version'] == version]
    #print("Reference:", reference)
    reference_embedding = read_embedding(reference)

    # Iterate over the embedding vectors and calculate the distance
    for other_index, other_row in df.iterrows():
        if other_row['index'] != int64(index):
            other_embedding = read_embedding(other_row)
            distance = calculate_distance(reference_embedding, other_embedding)
            if distance < threshold:
                duplicates.append(int(other_row['index']))
    return duplicates

# Usage example
index = 6
print(find_files_with_low_distance(index, 0))