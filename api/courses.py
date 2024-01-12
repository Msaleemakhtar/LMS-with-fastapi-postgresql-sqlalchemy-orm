from typing import List
import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from pydantic_schema.course import CourseCreate, Course
from api.utils.courses import get_course, get_courses, create_course

router = fastapi.APIRouter()


@router.get("/courses", response_model=List[Course])
async def read_courses(db: Session = Depends(get_db)):
    courses = get_courses(db=db)
    return courses


@router.post("/courses", response_model=Course)
async def create_new_courses(
    course: CourseCreate, db: Session = Depends(get_db)
):
    return create_course(db=db, course=course)


@router.get("/courses/{course_id}")
async def read_courses(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return db_course


@router.patch("/courses/{course_id}")
async def update_courses():
    return {"courses; ": []}


@router.delete("/courses/{id}")
async def delete_courses():
    return {"courses; ": []}
