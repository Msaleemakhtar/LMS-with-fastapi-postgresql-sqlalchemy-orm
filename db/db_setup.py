from sqlalchemy import create_engine

# from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f"postgresql://saleemakhtar864:YUaiSR4gF5Bj@ep-bold-cell-01190632.us-east-2.aws.neon.tech/lmspractice?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)

# async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

# asyncSessionLocal = sessionmaker(
#     async_engine, class_ = AsyncEngine, expire_on_commit = False
# )


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# async def async_get_db():
#     async with asyncSessionLocal() as db:
#         yield db
#         await db.commit()
