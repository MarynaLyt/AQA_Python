import pytest
from Employee import Employee, Manager, Developer, TeamLead


class Test_Manager:
    def test_manager_without_attributes(self) -> None:
        manager = Manager("Test_1", 1000, "")
        assert hasattr(manager, 'name'), "Manager повинен мати атрибут 'name'"
        assert hasattr(manager, 'salary'), "Manager повинен мати атрибут 'salary'"
        assert hasattr(manager, 'department'), "Manager повинен мати атрибут 'department'"
        assert manager.department == "", "Атрибут 'department' відсутній"

    def test_manager_with_attributes(self) -> None:
        manager = Manager("Test_2", 1000.50, "Engineering")
        assert hasattr(manager, 'name'), "Manager повинен мати атрибут 'name'"
        assert hasattr(manager, 'salary'), "Manager повинен мати атрибут 'salary'"
        assert hasattr(manager, 'department'), "Manager повинен мати атрибут 'department'"
        assert manager.department != "", "Атрибут 'department' присутній"


class Test_Developer:
    def test_developer_without_attributes(self) -> None:
        developer = Developer("Test_3", 100, "")
        assert hasattr(developer, 'name'), "Developer повинен мати атрибут 'name'"
        assert hasattr(developer, 'salary'), "Developer повинен мати атрибут 'salary'"
        assert hasattr(developer, 'programming_language'), "Developer повинен мати атрибут 'programming_language'"
        assert developer.programming_language == "", "Атрибут 'programming_language' відсутній"

    def test_developer_with_attributes(self) -> None:
        developer = Developer("Test_4", 100, "Python")
        assert hasattr(developer, 'name'), "Developer повинен мати атрибут 'name'"
        assert hasattr(developer, 'salary'), "Developer повинен мати атрибут 'salary'"
        assert hasattr(developer, 'programming_language'), "Developer повинен мати атрибут 'programming_language'"
        assert developer.programming_language != "", "Атрибут 'programming_language' присутній"


class Test_TeamLead:
    def test_teamlead_without_attributes(self) -> None:
        lead = TeamLead("Test_5", 1000, "Engineering", "Python", 0)
        assert hasattr(lead, 'name'), "TeamLead повинен мати атрибут 'name'"
        assert hasattr(lead, 'salary'), "TeamLead повинен мати атрибут 'salary'"
        assert hasattr(lead, 'department'), "TeamLead повинен мати атрибут 'department'"
        assert hasattr(lead, 'programming_language'), "TeamLead повинен мати атрибут 'programming_language'"
        assert hasattr(lead, 'team_size'), "TeamLead повинен мати атрибут 'team_size'"
        assert lead.team_size == 0, "Атрибут 'team_size' відсутній"

    def test_teamlead_with_attributes(self) -> None:
        lead = TeamLead("Test_6", 1000, "Engineering", "Python", 7)
        assert hasattr(lead, 'name'), "TeamLead повинен мати атрибут 'name'"
        assert hasattr(lead, 'salary'), "TeamLead повинен мати атрибут 'salary'"
        assert hasattr(lead, 'department'), "TeamLead повинен мати атрибут 'department'"
        assert hasattr(lead, 'programming_language'), "TeamLead повинен мати атрибут 'programming_language'"
        assert hasattr(lead, 'team_size'), "TeamLead повинен мати атрибут 'team_size'"
        assert lead.team_size != 0, "Атрибут 'team_size' присутній"

    def test_teamlead_has_all_attributes(self) -> None:
        lead = TeamLead("Test_Lead", 2000, "Engineering", "Python", 5)
        assert hasattr(lead, 'name'), "TeamLead повинен мати атрибут 'name' з Employee"
        assert hasattr(lead, 'salary'), "TeamLead повинен мати атрибут 'salary' з Employee"
        assert hasattr(lead, 'department'), "TeamLead повинен мати атрибут 'department' з Manager"
        assert hasattr(lead, 'programming_language'), "TeamLead повинен мати атрибут 'programming_language' з Developer"
        assert hasattr(lead, 'team_size'), "TeamLead повинен мати власний атрибут 'team_size'"

    def test_teamlead_attribute_values(self) -> None:
        lead = TeamLead("John Doe", 2500, "IT", "JavaScript", 8)
        assert lead.name == "John Doe", "Значення атрибуту 'name' неправильне"
        assert lead.salary == 2500, "Значення атрибуту 'salary' неправильне"
        assert lead.department == "IT", "Значення атрибуту 'department' неправильне"
        assert lead.programming_language == "JavaScript", "Значення атрибуту 'programming_language' неправильне"
        assert lead.team_size == 8, "Значення атрибуту 'team_size' неправильне"

    def test_teamlead_inheritance(self) -> None:
        lead = TeamLead("Jane Smith", 3000, "QA", "Java", 3)
        assert isinstance(lead, Employee), "TeamLead повинен успадковуватися від Employee"
        assert isinstance(lead, Manager), "TeamLead повинен успадковуватися від Manager"
        assert isinstance(lead, Developer), "TeamLead повинен успадковуватися від Developer"
        assert isinstance(lead, TeamLead), "Об'єкт повинен бути екземпляром TeamLead"