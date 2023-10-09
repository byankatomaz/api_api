from main import session
from models import Questions


# Aqui é uma função onde faz uma query no banco para buscar todas as questões do banco e retorna isso
def findAllQuestion():
    query = session.query(Questions).all()
    
    return query