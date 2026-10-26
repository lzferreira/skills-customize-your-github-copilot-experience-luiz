# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para consultar e gerenciar um catálogo de livros usando FastAPI. Você praticará rotas HTTP, validação de dados com modelos, códigos de status e respostas para recursos não encontrados.

## 📝 Tarefas

### 🛠️ Criar rotas para consultar livros

#### Descrição
Use o arquivo inicial fornecido para criar rotas que permitam consultar todos os livros do catálogo e buscar um livro específico pelo seu identificador. Execute a API e explore a documentação interativa gerada pelo FastAPI.

#### Requisitos
O programa concluído deve:

- Criar `GET /books` para retornar a lista de livros em formato JSON
- Criar `GET /books/{book_id}` para retornar um livro pelo identificador
- Retornar o código HTTP `404` quando o identificador não existir
- Iniciar localmente e exibir as rotas em `/docs`

### 🛠️ Adicionar livros com validação

#### Descrição
Permita que clientes adicionem livros ao catálogo. Defina um modelo de entrada com os campos necessários e use a validação do Pydantic para rejeitar dados incompletos ou inválidos.

#### Requisitos
O programa concluído deve:

- Criar `POST /books` para receber um título e um autor em JSON
- Validar que título e autor não estejam vazios
- Gerar um identificador único para cada novo livro
- Retornar o livro criado com o código HTTP `201`

Exemplo de corpo da requisição:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```

### 🛠️ Completar as operações do catálogo

#### Descrição
Implemente as operações para atualizar e remover livros existentes. Teste os diferentes caminhos, incluindo solicitações para identificadores que não estão no catálogo.

#### Requisitos
O programa concluído deve:

- Criar `PUT /books/{book_id}` para substituir o título e o autor de um livro existente
- Criar `DELETE /books/{book_id}` para remover um livro existente
- Retornar o livro atualizado após uma substituição bem-sucedida
- Retornar o código HTTP `404` para atualizações ou remoções de livros inexistentes
- Demonstrar as operações e respostas na interface `/docs`

Para começar, instale o FastAPI com suporte ao servidor de desenvolvimento e inicie o arquivo fornecido:

```bash
python -m pip install "fastapi[standard]"
fastapi dev starter-code.py
```
