from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Welcome to Bookstore Chatbot"}
