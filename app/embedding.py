from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text):
    return model.encode(text).tolist()


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
        combined_info = " ".join(
            [
                book["title"] or "",
                book["author"] or "",
                str(book["price"] or 0),
                book["description"] or "",
                book["category"] or "",
            ]
        )

        book_embedding = get_embedding(combined_info)
        similarity = cosine_similarity(query_embedding, book_embedding)
        similarities.append((book, similarity))

    similarities.sort(key=lambda x: x[1], reverse=True)
    return [item[0] for item in similarities[:top_k]]
