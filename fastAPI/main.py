from fastapi import FastAPI
from core.configs import settings
from api.v1._api import api_router

app = FastAPI(title='API de Cursos da ETS')
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='localhost', port=8000, log_level='info', reload=True)