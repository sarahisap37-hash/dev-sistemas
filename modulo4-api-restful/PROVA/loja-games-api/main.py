from fastapi import FastAPI

import models
from database import engine
from routers import avaliacoes, jogos, plataformas
from tags import tags_metadata

# Cria as tabelas no banco (SQLite) caso ainda não existam
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Loja de Games API",
    description=(
        "API para gerenciar o catálogo de jogos de uma loja de games, "
        "controlar as plataformas disponíveis (PlayStation, Xbox, PC...) "
        "e registrar avaliações dos clientes."
    ),
    version="1.0.0",
    openapi_tags=tags_metadata,
)

app.include_router(plataformas.router)
app.include_router(jogos.router)
app.include_router(avaliacoes.router)


@app.get("/", include_in_schema=False)
def raiz():
    return {"mensagem": "Loja de Games API no ar. Acesse /docs para a documentação."}
