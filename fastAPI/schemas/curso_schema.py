import sys
default_path = "C:\\Users\\mob7ca\\Desktop\\api_api\\fastAPI"
sys.path.append(default_path)

from typing import Optional
from pydantic import BaseModel as SchemaBaseMode

class CursoSchema(SchemaBaseMode):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    instrutor: str
    
    class config:
        from_attributes = True