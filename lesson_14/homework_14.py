from student import Student


student: Student = Student(name="Chandler", sur_name="Bing", age=26, average_score=75.5)
print(student.name)


student.update_average_score(85.2)
print(student)
