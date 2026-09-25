from app.database import engine, Base
from app import models #Para registrar os modelos na base
from app.seed import popular_banco

# create_all : cria as tabelas que não existem ainda
# Se a tabela já existe: não apaga, não muda nada
Base.metadata.create_all(bind=engine)
popular_banco()
print('A tabela criou vei')
