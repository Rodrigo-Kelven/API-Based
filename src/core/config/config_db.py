from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.future import select
import logging

# URL do banco de dados PostgreSQL
DATABASE_URL = "postgresql+asyncpg://user:password@my-db/fastapi_db"

# Criação do engine assíncrono
engine_auth = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_size=20,  # Tamanho do pool de conexões
    max_overflow=0,  # Conexões adicionais permitidas
    pool_pre_ping=True, # Verificando conexão do banco
)

# Criação do gerenciador de sessões assíncronas
AsyncSessionLocal = sessionmaker(bind=engine_auth, class_=AsyncSession, expire_on_commit=False)

# Criação da base para os modelos
Base_auth = declarative_base()

# Função para obter a sessão de banco de dados
async def get_user_db():
    async with AsyncSessionLocal() as session:
        yield session