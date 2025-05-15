from fastapi import APIRouter
from app.database import fetch_books
from app.embedding import find_similar_books
from app.models import QueryRequest, QueryResponse

router = APIRouter()


@router.post("/recommend", response_model=QueryResponse)
async def recommend_books(request: QueryRequest):
    books = fetch_books()
    similar_books = find_similar_books(request.query, books)
    return QueryResponse(books=similar_books)
