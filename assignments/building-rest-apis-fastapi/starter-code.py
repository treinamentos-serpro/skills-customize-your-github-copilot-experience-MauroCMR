# Starter Code: Building REST APIs with FastAPI

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Books API")


class Book(BaseModel):
    """Representa um livro gerenciado pela API."""

    id: int
    title: str
    author: str
    year: int


books: list[Book] = []


@app.get("/")
def read_root():
    # TODO: Retorne uma mensagem de boas-vindas.
    pass


@app.get("/books")
def list_books():
    # TODO: Retorne a coleção de livros.
    pass


@app.post("/books", status_code=201)
def create_book(book: Book):
    # TODO: Adicione o livro à coleção e retorne-o.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Busque o livro pelo ID e trate IDs inexistentes.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    # TODO: Atualize o livro correspondente e trate IDs inexistentes.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Remova o livro correspondente e trate IDs inexistentes.
    pass
