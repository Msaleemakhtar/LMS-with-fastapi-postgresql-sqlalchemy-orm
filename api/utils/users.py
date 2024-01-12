from sqlalchemy.orm import Session

# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select

from pydantic_schema.user import UserCreate
from db.models.user import User


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# async api is used here other can be changed
# async def get_users(db:AsyncSession, user_id:int):
#     query = select(User).where(User.id == user_id)
#     reult = await db.execute(query)
#     return reult.scalar_one_or_none()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
