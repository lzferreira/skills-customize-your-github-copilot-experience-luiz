# 📘 Atividade: Persistindo Dados com SQLite e FastAPI

## 🎯 Objetivo

Adapte uma API de livros para armazenar dados em um banco SQLite, em vez de mantê-los apenas na memória. Você praticará criação de tabelas, consultas SQL parametrizadas e persistência de dados em uma API REST.

## 📝 Tarefas

### 🛠️ Criar o banco de dados

#### Descrição
Complete a função `initialize_database()` no código inicial para criar um arquivo `books.db` e uma tabela para armazenar os livros. A inicialização deve poder ser executada mais de uma vez sem apagar os dados existentes.

#### Requisitos
O programa concluído deve:

- Criar a tabela `books` com `id` inteiro como chave primária autoincremental
- Definir `title` e `author` como campos de texto obrigatórios
- Criar a tabela somente se ela ainda não existir
- Fechar as conexões SQLite depois de usá-las

### 🛠️ Conectar as rotas de consulta e criação

#### Descrição
Implemente as rotas para listar livros, consultar um livro pelo identificador e adicionar um novo livro. Use o banco de dados como fonte dos dados em todas essas operações.

#### Requisitos
O programa concluído deve:

- Criar `GET /books` e `GET /books/{book_id}` usando consultas `SELECT`
- Criar `POST /books` usando `INSERT` e retornar o livro criado com o código HTTP `201`
- Usar parâmetros SQL (`?`) em vez de montar consultas concatenando valores recebidos
- Retornar o código HTTP `404` quando um livro solicitado não existir
- Confirmar as alterações no banco de dados após inserir um livro

### 🛠️ Atualizar, remover e verificar a persistência

#### Descrição
Complete as operações de atualização e remoção e verifique que os dados continuam disponíveis depois que a API for encerrada e iniciada novamente.

#### Requisitos
O programa concluído deve:

- Criar `PUT /books/{book_id}` para atualizar título e autor de um livro existente
- Criar `DELETE /books/{book_id}` para remover um livro existente
- Retornar o código HTTP `404` quando o livro não existir para atualização ou remoção
- Atualizar e remover registros com comandos SQL parametrizados
- Demonstrar em `/docs` que um livro criado continua disponível após reiniciar a API

Para executar a atividade, instale o FastAPI caso ainda não esteja disponível e inicie o arquivo fornecido:

```bash
python -m pip install "fastapi[standard]"
fastapi dev starter-code.py
```
