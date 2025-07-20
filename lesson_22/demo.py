from db_client import DBClient
from models import Base, Course, Student
from data import generate_sample_data

def main():
    db = DBClient(echo=False)
    Base.metadata.create_all(db.engine)

    db.clear_all_data()
    generate_sample_data()

    with db.Session() as s:
        course = s.query(Course).first()
        student = s.query(Student).first()

    print(f"Курс: {course.name}")
    print(f"Студент: {student.first_name} {student.last_name}")

    students_on_course = db.get_students_by_course(course.id)
    student_courses = db.get_courses_by_student(student.id)

    print(f"Студентів на курсі: {len(students_on_course)}")
    print(f"Курсів у студента: {len(student_courses)}")

    db.update_student_age(student.id, 36)
    print(f"Оновлено вік до: 36")

    db.delete_student(student.id)
    remaining_students = db.get_students_by_course(course.id)
    print(f"Студентів після видалення: {len(remaining_students)}")


if __name__ == "__main__":
    main()