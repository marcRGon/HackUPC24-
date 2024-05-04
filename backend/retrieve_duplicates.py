import pandas as pd
import numpy as np

threshold = 40

def calculate_distance(embedding1, embedding2):
    # Given two 1000 element dense vectors embedding1 and embedding2 as numpy arrays, calculate the Euclidean distance between them.
    distance = np.sqrt(np.sum((embedding1 - embedding2)**2))
    return distance

def find_files_with_low_distance(index):
    def read_embedding(row):
        embedding = np.zeros(1000)
        for i in range(0, 1000):
            #print(row[f'vector_{i}'])
            embedding[i] = row[f'vector_{i}']
        return embedding
    
    duplicates = []

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv('image_embeddings_test.csv')
    
    reference = df[df['index'] == index][df['version'] == 0]
    #print("Reference:", reference)
    reference_embedding = read_embedding(reference)

    # Iterate over the embedding vectors and calculate the distance
    for other_index, other_row in df.iterrows():
        if other_row['index'] != index:
            other_embedding = read_embedding(other_row)
            distance = calculate_distance(reference_embedding, other_embedding)
            if distance < threshold:
                duplicates.append(other_row['index'])
    return duplicates

# Usage example
index = 1
print(find_files_with_low_distance(index))