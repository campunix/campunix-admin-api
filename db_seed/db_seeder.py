import asyncio
import json
from pathlib import Path

from sqlalchemy import MetaData, Table, insert, text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from db_seed.seed import data
from src.core.config import settings

DATABASE_URL = str(settings.DATABASE_URL)
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
metadata = MetaData()

SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Load the JSON data
def load_seed_data(file_path: str):
    with open(file_path, 'r') as f:
        return json.load(f)

# Insert data asynchronously into each table
async def insert_data(table_name, records):
    async with engine.connect() as conn:
        await conn.execute(text(
            "SET session_replication_role = 'replica';"))

        await conn.execute(text(
            f"DELETE FROM {table_name};"))

        await conn.execute(text(
            "SET session_replication_role = 'origin';"))

        seq_name = f"public.{table_name}_id_seq"
        await conn.execute(text(f"ALTER SEQUENCE {seq_name} RESTART WITH 1;"))

        await conn.run_sync(
            lambda sync_conn: sync_conn.execute(insert(Table(table_name, metadata, autoload_with=sync_conn)), records))
        print(f"Inserted data into {table_name}.")
        await conn.commit()


# Seed the database with data
async def seed_database(data: dict):
    async with SessionLocal() as session:
        for table_name, records in data.items():
            await insert_data(table_name, records)

        await session.commit()


async def main():
    #seed_data = json.load(data)
    #print(seed_data)
    await seed_database(data)

    # file_path = "db_seed/seed.py"
    # if not Path(file_path).exists():
    #     print(f"Seed file {file_path} does not exist.")
    # else:
    #     seed_data = load_seed_data(file_path)
    #     seed_data = json.load(data)
    #     await seed_database(seed_data)


if __name__ == "__main__":
    asyncio.run(main())
