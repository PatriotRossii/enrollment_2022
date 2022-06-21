from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_PATH = "analyzer:root@localhost/analyzer"
ASYNC_DATABASE_URL = f"postgresql+asyncpg://{DATABASE_PATH}"
SYNC_DATABASE_URL = f"postgresql+psycopg2://{DATABASE_PATH}"

engine = create_async_engine(ASYNC_DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False, class_=AsyncSession)

convention = {
    "all_column_names": lambda constraint, table: "_".join([column.name for column in constraint.columns.values()]),
    # Именование индексов
    "ix": "ix__%(table_name)s__%(all_column_names)s",
    # Именование уникальных индексов
    "uq": "uq__%(table_name)s__%(all_column_names)s",
    # Именование CHECK-constraint-ов
    "ck": "ck__%(table_name)s__%(constraint_name)s",
    # Именование внешних ключей
    "fk": "fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s",
    # Именование первичных ключей
    "pk": "pk__%(table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)
