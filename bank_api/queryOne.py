from main import session
from models import Questions



def findOneQuestion(id):
    query = session.query(Questions).filter(Questions.id == id).first()

    return query
