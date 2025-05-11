class Student:
    def __init__(self, name: str, sur_name: str, age: int, average_score: float):
        self.name = name
        self.sur_name = sur_name
        self.age = age
        self.average_score = average_score

    def update_average_score(self, updated_score: float) -> str:
        self.average_score = updated_score

    def __str__(self) -> str:
        return f"Студент: {self.name} {self.sur_name}, вік якого: {self.age} років, має середній бал: {self.average_score}"