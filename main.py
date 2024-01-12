from fastapi import FastAPI

from api import users, courses, sections
from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

description = """
"LMS for managing Students and Courses". 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""
app = FastAPI(
    title="FastAPI LMS",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Muhammad saleem Akhtar",
        "email": "saleemakhtar864@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
