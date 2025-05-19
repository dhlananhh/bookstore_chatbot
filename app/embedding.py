import ollama
import numpy as np
import os
from dotenv import load_dotenv

# Tải biến môi trường
load_dotenv()


def get_embedding(text):
    ollama_host = os.getenv("OLLAMA_HOST", "localhost")
    ollama_port = os.getenv("OLLAMA_PORT", "11434")
    client = ollama.Client(host=f"http://{ollama_host}:{ollama_port}")
    response = client.embeddings(model="mxbai-embed-large", prompt=text)
    return response["embedding"]


def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)


def find_similar_books(query, books, top_k=5):
    query_embedding = get_embedding(query)
    similarities = []

    for book in books:
        description = book["description"] or ""
        book_embedding = get_embedding(description)
        similarity = cosine_similarity(query_embedding, book_embedding)
        similarities.append((book, similarity))

    similarities.sort(key=lambda x: x[1], reverse=True)
    return [item[0] for item in similarities[:top_k]]
