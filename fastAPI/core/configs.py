from pydantic.v1 import BaseSettings #NEW
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    """
        config geral
    """
    API_V1_STR: str = '/api/v1' #não precisar inserir via hard coding
    DB_URL: str = 'mysql+asyncmy://root@127.0.0.1:3306/etscursos'
    DBBaseModel = declarative_base()
    
    class Config():
        case_sensitive = True
        

settings = Settings()