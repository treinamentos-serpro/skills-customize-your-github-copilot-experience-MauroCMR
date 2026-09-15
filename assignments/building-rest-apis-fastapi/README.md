# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a criar uma API REST em Python usando o framework FastAPI, definindo rotas, validando dados com modelos e implementando operações CRUD para um recurso em memória.

## 📝 Tasks

### 🛠️ Create the API Foundation

#### Descrição
Configure uma aplicação FastAPI para gerenciar uma coleção de livros e crie endpoints básicos para consultar a API.

#### Requisitos
O programa concluído deve:

- Criar uma instância de `FastAPI`.
- Implementar `GET /` retornando uma mensagem de boas-vindas.
- Implementar `GET /books` retornando a lista de livros cadastrados.
- Iniciar a aplicação com um servidor compatível com ASGI, como Uvicorn.

### 🛠️ Define Data Models and Validation

#### Descrição
Defina modelos Pydantic para representar livros e valide os dados recebidos ao criar um novo livro.

#### Requisitos
O programa concluído deve:

- Criar um modelo `Book` com `id`, `title`, `author` e `year`.
- Usar tipos apropriados para cada campo.
- Exigir `title` e `author` com valores não vazios.
- Implementar `POST /books` para validar e adicionar um livro à coleção.
- Retornar o livro criado com status HTTP `201`.

### 🛠️ Implement CRUD Operations

#### Descrição
Expanda a API para permitir consultar, atualizar e remover livros individualmente.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}` para buscar um livro pelo identificador.
- Implementar `PUT /books/{book_id}` para atualizar os dados de um livro.
- Implementar `DELETE /books/{book_id}` para remover um livro.
- Retornar status HTTP `404` quando o identificador não existir.
- Retornar o recurso atualizado ou removido na resposta apropriada.

### 🛠️ Handle API Errors Clearly

#### Descrição
Melhore a experiência de quem consome a API usando respostas de erro consistentes e documentação automática do FastAPI.

#### Requisitos
O programa concluído deve:

- Usar `HTTPException` para comunicar erros de recursos não encontrados.
- Retornar mensagens de erro que identifiquem o `book_id` procurado.
- Verificar os endpoints no Swagger UI em `/docs`.
- Incluir pelo menos um teste manual documentado com método, URL, corpo enviado e resposta esperada.
