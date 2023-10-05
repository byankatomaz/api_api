from main import session
from models import Questions

def findAllQuestion():
    query = session.query(Questions).all()
    
    return query