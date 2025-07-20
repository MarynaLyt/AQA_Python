from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
student_course = Table(
    'student_course',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)
    courses = relationship(
        "Course",
        secondary=student_course,
        back_populates="students"
    )

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.first_name} {self.last_name}', email='{self.email}')>"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    credits = Column(Integer, default=3)
    students = relationship(
        "Student",
        secondary=student_course,
        back_populates="courses"
    )

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', credits={self.credits})>"

    def get_students_count(self):
        return len(self.students)