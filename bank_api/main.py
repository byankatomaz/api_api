from sqlalchemy.orm import Session
from connect import engine

# Session para fazer a conexão com o banco de dados
session  = Session(bind=engine)