import sys
default_path = "C:\\Users\\mob7ca\\Desktop\\api_api\\fastAPI"
sys.path.append(default_path)

from core.configs import settings
from core.database import engine
from models import __all_models

async def create_tables() -> None:
    print('Criando as tabelas no DB...')
    
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabelas criadas com sucesso')

if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tables())