from app.database import engine, Base
from app import models
from app.seed import popular_banco
from app.crud import escola

# create_ cria as tabelas que nãpo existem ainda
# se a tabela já  existe : não apaga, muda nada
Base.metadata.create_all(bind=engine)
popular_banco('pronto')
