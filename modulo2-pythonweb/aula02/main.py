from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from typing import Optional 

app = FastAPI(title='Cadastro - SENAI', version='0.2.0')

# Modelo Pydantic
class Usuario(BaseModel):
    nome: str
    email: str
    cargo: str
    ativo: bool = True # valor padrão
    salario: Optional[float] = None # campo opcional

    @field_validator('nome')
    @classmethod
    def validar_nome(cls, v):
        v = v.strip()
        if len(v) < 3:
            raise ValueError('Nome deve ter pelo menor 3 caracteres')
        return v.title()


class UsuarioResposta(BaseModel):
    id: int
    nome: str
    email: str
    ativo: bool
    salario: Optional[float] = None

usuarios_db: list[UsuarioResposta] = [
    UsuarioResposta(id=1, nome='Alice Silva', email='alice@gmail.com',
                    cargo='Designer Gráfico', ativo=True, salario=10000.0),
    UsuarioResposta(id=1, nome='Thiago', email='thzin@gmail.com',
                    cargo='Desenvolvedor', ativo=True, salario=15000.0),
    UsuarioResposta(id=1, nome='Gustavo', email='gustavogayemei@gmail.com',
                        cargo='Lixeiro', ativo=True, salario=500.0),                
]

proximo_id = 4

# GET /usuarios - Lista todos os usuários
@app.get('/usuarios', response_model=list[UsuarioResposta])
def listar_usuario():
    return usuarios_db

@app.get('/usuario/{usuario_id}', response_model=UsuarioResposta)
def buscar_usuario(usuario_id: int):
    for usuario in usuarios_db:
        if usuario.id == usuario_id:
            return usuario
        raise HTTPException(status_code=404, detail='Usuário não encontrado')