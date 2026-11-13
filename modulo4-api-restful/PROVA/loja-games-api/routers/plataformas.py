from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.orm import Session

import models
from database import get_db
from tags import TAG_PLATAFORMAS

router = APIRouter(prefix="/plataformas", tags=[TAG_PLATAFORMAS])


class PlataformaCreate(BaseModel):
    nome: str = Field(..., min_length=1, max_length=50, examples=["PlayStation 5"])


class PlataformaOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nome: str


@router.get("/", response_model=List[PlataformaOut], summary="Listar todas as plataformas")
def listar_plataformas(db: Session = Depends(get_db)):
    return db.query(models.Plataforma).all()


@router.post(
    "/",
    response_model=PlataformaOut,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar nova plataforma",
)
def criar_plataforma(dados: PlataformaCreate, db: Session = Depends(get_db)):
    existente = (
        db.query(models.Plataforma).filter(models.Plataforma.nome == dados.nome).first()
    )
    if existente:
        raise HTTPException(status_code=400, detail="Plataforma já cadastrada")

    plataforma = models.Plataforma(nome=dados.nome)
    db.add(plataforma)
    db.commit()
    db.refresh(plataforma)
    return plataforma
