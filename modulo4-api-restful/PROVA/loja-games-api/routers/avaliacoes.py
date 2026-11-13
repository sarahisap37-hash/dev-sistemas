from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.orm import Session

import models
from database import get_db
from tags import TAG_AVALIACOES

router = APIRouter(prefix="/avaliacoes", tags=[TAG_AVALIACOES])


class AvaliacaoCreate(BaseModel):
    nota: int = Field(..., ge=1, le=5, description="Nota de 1 a 5")  # fora do intervalo -> 422
    comentario: str
    jogo_id: int


class AvaliacaoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nota: int
    comentario: str | None = None
    jogo_id: int


@router.post(
    "/",
    response_model=AvaliacaoOut,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar avaliação de um jogo",
)
def criar_avaliacao(dados: AvaliacaoCreate, db: Session = Depends(get_db)):
    jogo = db.get(models.Jogo, dados.jogo_id)
    if not jogo:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")

    avaliacao = models.Avaliacao(**dados.model_dump())
    db.add(avaliacao)
    db.commit()
    db.refresh(avaliacao)
    return avaliacao


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Remover uma avaliação")
def remover_avaliacao(id: int, db: Session = Depends(get_db)):
    avaliacao = db.get(models.Avaliacao, id)
    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")

    db.delete(avaliacao)
    db.commit()
