import random
from db_client import DBClient
from models import Base


def generate_sample_data():
    db = DBClient(echo=False)  # Без SQL логів
    Base.metadata.create_all(db.engine)

    courses_data = [
        "Python Programming",
        "Database Management",
        "Web Development",
        "Software Testing",
        "Data Science"
    ]
    courses = []
    for course_name in courses_data:
        course = db.add_course(course_name)
        courses.append(course)

    names = [
        "Олександр Петренко", "Марія Іваненко", "Дмитро Коваленко", "Анна Сидоренко",
        "Сергій Мельник", "Катерина Шевченко", "Віктор Бондаренко", "Ольга Кравченко",
        "Андрій Лисенко", "Наталія Ткаченко", "Максим Гриценко", "Юлія Савченко",
        "Роман Поліщук", "Світлана Марченко", "Валентин Федоренко", "Ірина Павленко",
        "Богдан Данилко", "Тетяна Романенко", "Михайло Тарасенко", "Людмила Васильченко"
    ]
    students = []
    for name in names:
        age = random.randint(18, 35)
        num_courses = random.randint(1, 3)
        selected_courses = random.sample(courses, num_courses)
        course_ids = [course.id for course in selected_courses]
        student = db.add_student(name, age, course_ids=course_ids)
        students.append(student)
    total_enrollments = sum(len(db.get_courses_by_student(s.id)) for s in students)
    for course in courses:
        count = len(db.get_students_by_course(course.id))


if __name__ == "__main__":
    generate_sample_data()
