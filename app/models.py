from pydantic import BaseModel
from typing import List


class Book(BaseModel):
    id: int
    title: str
    author: str | None
    description: str | None
    price: float
    category: str | None
    publisher: str | None


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    books: List[Book]
