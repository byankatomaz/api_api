from main import session
from models import Questions


#Aqui é uma função onde faz uma query no banco para buscar apenas 1 questão no banco e retorna isso
def findOneQuestion(id):
    query = session.query(Questions).filter(Questions.id == id).first()

    return query
