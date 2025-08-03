class Employee:
    def __init__(self, name: str, salary: int | float):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name: str, salary: int | float, department: str):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f"{super().__str__()}, Department: {self.department}"


class Developer(Employee):
    def __init__(self, name: str, salary: int | float, programming_language: str):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def __str__(self):
        return f"{super().__str__()}, Language: {self.programming_language}"


class TeamLead(Manager, Developer):
    def __init__(self, name: str, salary: int | float, department: str, programming_language: str, team_size: int):
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size

    def __str__(self):
        return f"{Employee.__str__(self)}, Department: {self.department}, Language: {self.programming_language}, Team Size: {self.team_size}"