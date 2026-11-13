from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco - SQLlite salva em um arquivo banco.db  nas pasta do projeto
DATABASE_URL = 'sqlite:///./banco.db'

# Engine: motor de conexão com o banco
engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thead': False} # necessário para SQLite
)
 