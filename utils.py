import faiss
import numpy as np
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def save_to_vector_database(vectors):
    filename = os.getenv("INDEX_PATH")
    # Initialize the FAISS Index
    d = 4096 #len(vectors[0])
    index = faiss.IndexFlatIP(d)
    

    # # Add the vectors to the index
    for _, vec in enumerate(vectors):
        index.add(np.array([vec]))

    # Save the index to disk
    faiss.write_index(index, filename)

# Function to find the closest embeddings using FAISS
def find_closest_embedding(query_embedding):
    # Path to saved index
    index_path = os.getenv("INDEX_PATH")

    # Load index
    index = faiss.read_index(index_path)
    # Perform a nearest neighbor search in the FAISS index
    distances, idx = index.search(np.array([query_embedding]), 1)
    
    
    return idx
