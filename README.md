## Fast API LMS

### This is a learning management system where teachers can manage student and students can see their courses.
* Teachers can perform CRUD operations on students.
* Teachers can create courses with sections and content blocks in each section.
* Teachers can assign courses to students.
* Students can interact view their courses in a list.
* Students can see the sections and content blocks for individual courses that they are taking.
* Students are able to see their progress for each course.


### Running the App Locally

* Make sure Python, Poetry, and Postgres are installed. Postgres must be running. If you need help with this,       please follow the instructions in the video linked at the top of this README.
* Create a virtual environment: python -m venv venv
* Install packages: poetry install
* Run the development server: uvicorn main:app --reload

### Tech Stack

* Fast API
* Python 3.9+
* Poetry
* Postgres
* SQL Alchemy 1.4+
* Alembic
* Pydantic
* Black
* Flake8
* Pre-commit

## Schema

### User

* email: str
* role: enum (student, teacher)
* is_active: bool

### profile
* first_name: str
* last_name: str
* bio: str (TextField)
* user_id: fk


### Course

* title: str
* description: str (TextField)
* user_id: fk

### Section

* title
* description
* course_id


### ContentBlock

* title
* description
* type
* url
* content
* section_id

### StudentCourse

This model is used for teachers to assign courses to students. The 'completed' boolean is False until the student has completed the whole course.

* student_id
* course_id
* c* ompleted

### CompletedContentBlock

Every time the student completes a content block, a row is created in this table. The teacher can then go and edit this information when they grade the content block and provide feedback.

* student_id
* content_block_id
* url
* feedback
* grade
