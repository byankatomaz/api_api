from models import Base
from connect import engine

print("CREATING TABLES>>>>>")
Base.metadata.create_all(bind=engine)