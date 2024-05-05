import pandas as pd
import numpy as np
import heapq
from numpy import int64

distance_type = 'euclidean'

# threshold = 40 for Euclidean, Manhattan and dot product distance
# threshold = 0.125 for cosine distance
THRESHOLD = 40
K = 7

def matching_classes(row1, row2):
    classes1 = row1['url'].split('///')[1].split('/')[1:4]
    classes2 = row2['url'].split('///')[1].split('/')[1:4]
    return classes1 == classes2

def calculate_distance(embedding1, embedding2):
    if distance_type == 'euclidean':
        # Given two 1000 element dense vectors embedding1 and embedding2 as numpy arrays, calculate the Euclidean distance between them.
        distance = np.sqrt(np.sum((embedding1 - embedding2)**2))
    elif distance_type == 'cosine':
        # Given two 1000 element dense vectors embedding1 and embedding2 as numpy arrays, calculate the cosine distance between them.
        distance = 1 - np.dot(embedding1, embedding2)/(np.linalg.norm(embedding1) * np.linalg.norm(embedding2))
    elif distance_type == 'manhattan':
        # Given two 1000 element dense vectors embedding1 and embedding2 as numpy arrays, calculate the Manhattan distance between them.
        distance = np.sum(np.abs(embedding1 - embedding2))
    elif distance_type == 'dot_product':
        # Given two 1000 element dense vectors embedding1 and embedding2 as numpy arrays, calculate the dot product between them.
        distance = np.dot(embedding1, embedding2)
    return distance

def find_files_with_low_distance(index, version):
    def read_embedding(row):
        embedding = np.zeros(1000)
        for i in range(0, 1000):
            #print(row[f'vector_{i}'])
            embedding[i] = row[f'vector_{i}']
        return embedding
    
    # Initialize an empty heap
    heap = []

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv('image_embeddings_PABLO_0.csv')
    # Take the row corresponding to the given index and version
    filtered_df = df[(df['index'] == int64(index)) & (df['version'] == int64(version))]
    if not filtered_df.empty:
        reference = filtered_df.iloc[0]
        reference_embedding = read_embedding(reference)
    else:
        print(f"No rows found with index {index} and version {version}")
        return []
    reference_embedding = read_embedding(reference)

    # Iterate over the embedding vectors and calculate the distance
    for other_index, other_row in df.iterrows():
        if matching_classes(other_row, reference) and other_row['index'] != int64(index) and other_row['index'] not in [int64(heap_item[1]) for heap_item in heap]:
            other_embedding = read_embedding(other_row)
            distance = calculate_distance(reference_embedding, other_embedding)
            if distance > THRESHOLD:
                continue

            # Use a tuple (distance, index), which sorts by distance first and then index
            if len(heap) < K:
                # If the heap has less than K items, just push the new item onto the heap
                heapq.heappush(heap, (distance, int(other_row['index'])))
            else:
                # If the heap already has K items, push the new item and then pop the smallest item
                heapq.heappushpop(heap, (distance, int(other_row['index'])))

    # Sort the heap by distance
    heap.sort(key=lambda x: x[0])

    # At this point, heap contains the K smallest distances and their corresponding indices
    # Convert it to a list of indices
    duplicates = [index for distance, index in heap]
    return duplicates

# Usage example
#for j in range(0, 1190):
#    print(f"{j}:", find_files_with_low_distance(j, 0))
#index = 1190
#print(find_files_with_low_distance(index, 0))