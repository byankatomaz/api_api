import sys
default_path = "C:\\users\\mob7ca\\Desktop\\fastAPI"
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