import pytest
from fastapi.testclient import TestClient

from starter_code import app


@pytest.fixture
def client():
    return TestClient(app)


def test_root_returns_welcome_message(client):
    # TODO: Faça uma requisição para GET / e verifique o status e a mensagem.
    pass


def test_list_books_returns_a_list(client):
    # TODO: Faça uma requisição para GET /books e verifique a lista JSON.
    pass


def test_create_book_returns_created_book(client):
    payload = {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
    }

    # TODO: Envie payload para POST /books e verifique status 201 e os dados.
    pass


def test_missing_title_is_rejected(client):
    payload = {"id": 3, "author": "Ursula K. Le Guin", "year": 1969}

    # TODO: Verifique que a validação retorna status 422 e informa o campo title.
    pass


def test_invalid_year_is_rejected(client):
    payload = {
        "id": 4,
        "title": "A Wizard of Earthsea",
        "author": "Ursula K. Le Guin",
        "year": -1,
    }

    # TODO: Verifique que a validação retorna status 422.
    pass


def test_missing_book_returns_not_found(client):
    # TODO: Verifique status 404 e a mensagem para um ID inexistente.
    pass
