import os
import requests
import json
from openai import OpenAI

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        
    def generate_embedding(self, text:str, model="text-embedding-3-large"):
        response = self.client.embeddings.create(input=[text], model=model)
        return response.data[0].embedding
    
    def generate_embeddings(self, texts:list, model="text-embedding-3-small"):
        response = self.client.embeddings.create(input=texts, model=model)
        return [embedding.embedding for embedding in response.data]