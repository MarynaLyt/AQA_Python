from typing import List, Optional
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker, joinedload
from models import Student, Course, student_course
import config


class DBClient:
    def __init__(self, echo: bool = False):
        if config.DB_PASSWORD:
            url = f"postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
        else:
            url = f"postgresql://{config.DB_USER}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
        self.engine = create_engine(url, echo=echo, future=True)
        self.Session = sessionmaker(bind=self.engine, autoflush=False)

    def add_course(self, title: str) -> Course:
        with self.Session() as s:
            existing = s.query(Course).filter_by(name=title).first()
            if existing:
                return existing
            course = Course(name=title)
            s.add(course)
            s.commit()
            s.refresh(course)
            return course

    def add_student(self, name: str, age: int, course_ids: Optional[List[int]] = None) -> Student:
        with self.Session() as s:
            parts = name.split()
            first_name = parts[0] if parts else "Unknown"
            last_name = " ".join(parts[1:]) if len(parts) > 1 else "Student"
            base_email = f"{first_name.lower()}.{last_name.lower()}@university.edu"
            email = base_email
            counter = 1
            while s.query(Student).filter_by(email=email).first():
                email = f"{first_name.lower()}.{last_name.lower()}{counter}@university.edu"
                counter += 1
            student = Student(first_name=first_name, last_name=last_name, email=email, age=age)
            if course_ids:
                courses = s.query(Course).filter(Course.id.in_(course_ids)).all()
                student.courses.extend(courses)
            s.add(student)
            s.commit()
            s.refresh(student)
            return student

    def get_students_by_course(self, course_id: int) -> List[Student]:
        with self.Session() as s:
            course = s.query(Course).options(joinedload(Course.students)).filter(Course.id == course_id).first()
            return course.students if course else []

    def get_courses_by_student(self, student_id: int) -> List[Course]:
        with self.Session() as s:
            student = s.query(Student).options(joinedload(Student.courses)).filter(Student.id == student_id).first()
            return student.courses if student else []

    def update_student_age(self, student_id: int, new_age: int) -> None:
        with self.Session() as s:
            s.execute(update(Student).where(Student.id == student_id).values(age=new_age))
            s.commit()

    def delete_student(self, student_id: int) -> None:
        with self.Session() as s:
            student = s.get(Student, student_id)
            if student:
                student.courses.clear()
                s.delete(student)
                s.commit()

    def clear_all_data(self) -> None:
        with self.Session() as s:
            s.execute(student_course.delete())
            s.query(Student).delete()
            s.query(Course).delete()
            s.commit()