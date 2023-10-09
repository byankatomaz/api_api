from main import session
from models import Questions, Correct, Incorrect

def deleteOneQuestion(id):
    correct = session.query(Correct).filter(Correct.idQuestion == id).first()
    incorrects = session.query(Incorrect).filter(Incorrect.idQuestion == id).all()
    question = session.query(Questions).filter(Questions.id == id).first()

    session.delete(correct)
    
    for incorrect in incorrects:
        session.delete(incorrect)

    session.delete(question)
    session.commit()
