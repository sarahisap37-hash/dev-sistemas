from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.orm import Session

import models
from database import get_db
from routers.avaliacoes import AvaliacaoOut
from tags import TAG_JOGOS

router = APIRouter(prefix="/jogos", tags=[TAG_JOGOS])


class JogoCreate(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=100, examples=["God of War"])
    genero: Optional[str] = Field(None, max_length=50, examples=["Ação"])
    preco: float = Field(..., gt=0, examples=[199.90])
    plataforma_id: int


class JogoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    titulo: str
    genero: Optional[str] = None
    preco: float
    plataforma_id: int


def _buscar_jogo_ou_404(db: Session, id: int) -> models.Jogo:
    jogo = db.get(models.Jogo, id)
    if not jogo:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return jogo


def _validar_plataforma(db: Session, plataforma_id: int) -> None:
    if not db.get(models.Plataforma, plataforma_id):
        raise HTTPException(status_code=404, detail="Plataforma não encontrada")


@router.get("/", response_model=List[JogoOut], summary="Listar todos os jogos")
def listar_jogos(db: Session = Depends(get_db)):
    return db.query(models.Jogo).all()


@router.get("/{id}", response_model=JogoOut, summary="Buscar jogo por ID")
def buscar_jogo(id: int, db: Session = Depends(get_db)):
    return _buscar_jogo_ou_404(db, id)


@router.post(
    "/",
    response_model=JogoOut,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar novo jogo",
)
def criar_jogo(dados: JogoCreate, db: Session = Depends(get_db)):
    _validar_plataforma(db, dados.plataforma_id)

    jogo = models.Jogo(**dados.model_dump())
    db.add(jogo)
    db.commit()
    db.refresh(jogo)
    return jogo


@router.put("/{id}", response_model=JogoOut, summary="Atualizar dados de um jogo")
def atualizar_jogo(id: int, dados: JogoCreate, db: Session = Depends(get_db)):
    jogo = _buscar_jogo_ou_404(db, id)
    _validar_plataforma(db, dados.plataforma_id)

    for campo, valor in dados.model_dump().items():
        setattr(jogo, campo, valor)

    db.commit()
    db.refresh(jogo)
    return jogo


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Remover um jogo")
def remover_jogo(id: int, db: Session = Depends(get_db)):
    jogo = _buscar_jogo_ou_404(db, id)
    db.delete(jogo)
    db.commit()


@router.get(
    "/{id}/avaliacoes",
    response_model=List[AvaliacaoOut],
    summary="Listar avaliações de um jogo",
)
def listar_avaliacoes_do_jogo(id: int, db: Session = Depends(get_db)):
    jogo = _buscar_jogo_ou_404(db, id)
    return jogo.avaliacoes
