from main import session
from models import Questions



def find_Question(id):
    query = session.query(Questions).filter(Questions.id == id).first()

 
    id = query.id
    atributo1 = query.category
    atributo2 = query.type

    
    print(id, atributo1, atributo2, ...)


find_Question(12)