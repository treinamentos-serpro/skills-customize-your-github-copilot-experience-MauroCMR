# 📘 Assignment: Testing FastAPI Applications

## 🎯 Objective

Aprenda a testar endpoints de uma aplicação FastAPI com `pytest` e `TestClient`. Você irá verificar respostas de sucesso, validação de dados e tratamento de erros sem depender de testes manuais no Swagger UI.

## 📝 Tasks

### 🛠️ Test Successful API Requests

#### Descrição
Escreva testes automatizados para os endpoints que retornam dados válidos da API de livros.

#### Requisitos
O programa concluído deve:

- Usar `pytest` e `TestClient` para enviar requisições à aplicação.
- Verificar que `GET /` retorna status HTTP `200`.
- Verificar que `GET /books` retorna status HTTP `200` e uma lista JSON.
- Verificar o conteúdo essencial das respostas usando asserções claras.

### 🛠️ Test Request Validation

#### Descrição
Teste como a API reage a dados ausentes ou inválidos enviados ao endpoint de criação de livros.

#### Requisitos
O programa concluído deve:

- Verificar que um livro válido pode ser criado com `POST /books`.
- Verificar que uma requisição sem o campo obrigatório `title` retorna status HTTP `422`.
- Verificar que uma requisição com um ano inválido retorna status HTTP `422`.
- Conferir que a resposta de validação contém informações sobre o erro.

### 🛠️ Test API Error Handling

#### Descrição
Adicione testes para os casos em que o cliente solicita um livro que não existe e organize os testes para serem independentes.

#### Requisitos
O programa concluído deve:

- Verificar que `GET /books/{book_id}` retorna status HTTP `404` para um ID inexistente.
- Verificar que a mensagem de erro identifica o livro solicitado.
- Usar fixtures ou uma estratégia equivalente para preparar dados de teste previsíveis.
- Executar todos os testes com `pytest` sem falhas.

Exemplo de comando:

```bash
pytest -q
```
