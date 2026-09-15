from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class Book(BaseModel):
    id: int
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(ge=0)


books = [
    Book(id=1, title="The Hobbit", author="J. R. R. Tolkien", year=1937),
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Books API"}


@app.get("/books")
def list_books():
    return books


@app.post("/books", status_code=201)
def create_book(book: Book):
    books.append(book)
    return book


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail=f"Book {book_id} not found")
