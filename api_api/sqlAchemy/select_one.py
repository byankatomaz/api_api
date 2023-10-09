from main import session
from models import User


query = session.query(User).all()


print(f'ola {query}')