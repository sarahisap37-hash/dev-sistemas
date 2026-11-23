# Loja de Games API

API REST desenvolvida com **FastAPI** para gerenciar jogos, plataformas e avaliações de clientes de uma loja de games.

## Tecnologias

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic

## Funcionalidades

- Cadastrar e listar plataformas.
- Cadastrar, consultar, atualizar e remover jogos.
- Registrar e remover avaliações.
- Consultar as avaliações de um jogo.

## Como executar

1. Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/sarahisap37-hash/dev-sistemas.git
cd dev-sistemas/modulo4-api-restful/PROVA/loja-games-api
```

2. (Opcional) Crie e ative um ambiente virtual:

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicie a API:

```bash
uvicorn main:app --reload
```

A API ficará disponível em http://127.0.0.1:8000.

## Documentação interativa

Com a aplicação em execução, acesse:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Rotas disponíveis

| Método | Rota | Descrição |
|---|---|---|
| GET | `/plataformas/` | Lista as plataformas |
| POST | `/plataformas/` | Cadastra uma plataforma |
| GET | `/jogos/` | Lista os jogos |
| GET | `/jogos/{id}` | Busca um jogo pelo ID |
| POST | `/jogos/` | Cadastra um jogo |
| PUT | `/jogos/{id}` | Atualiza um jogo |
| DELETE | `/jogos/{id}` | Remove um jogo |
| GET | `/jogos/{id}/avaliacoes` | Lista as avaliações de um jogo |
| POST | `/avaliacoes/` | Registra uma avaliação |
| DELETE | `/avaliacoes/{id}` | Remove uma avaliação |

## Banco de dados

O projeto utiliza SQLite. O arquivo `loja_games.db` é criado localmente e as tabelas são criadas automaticamente quando a aplicação é iniciada.

## Observações

- Para cadastrar um jogo, informe uma plataforma que já esteja cadastrada.
- A nota de uma avaliação deve ser um número de 1 a 5.
- Os campos obrigatórios e as validações podem ser consultados na documentação interativa.

## Autoria

Projeto acadêmico – Loja de Games API.
