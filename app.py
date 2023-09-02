from langchain.embeddings import CohereEmbeddings
import os
from utils import find_closest_embedding
import pandas as pd
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

cohere_api_key = os.getenv("COHERE_API_KEY")
mental_health_faq_filename = os.getenv("FAQ_DB")

df = pd.read_csv(mental_health_faq_filename)
embeddings = CohereEmbeddings(cohere_api_key=cohere_api_key)

prompt = input('Enter your question about medical health: ')

# Generate an embedding for the question using the Cohere API
embedding = embeddings.embed_query(prompt)

index = find_closest_embedding(embedding)

print(df.iloc[index[0][0]]["Answers"])