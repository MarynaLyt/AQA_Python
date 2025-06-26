import pytest


from Employee import Employee, Manager, Developer, TeamLead


class Test_Manager:
    def test_manager_without_attributes(self) -> None:
        manager = Manager("Test_1", 1000, "")
        assert manager.department == "", "Атрибут 'department' відсутній"

    def test_manager_with_attributes(self) -> None:
        manager = Manager("Test_2", 1000.50, "Engineering")
        assert manager.department != "", "Атрибут 'department' присутній"


class Test_Developer:
    def test_developer_without_attributes(self) -> None:
        developer = Developer("Test_3", 100, "")
        assert developer.programming_language == "", "Атрибут 'programming_language' відсутній"

    def test_developer_with_attributes(self) -> None:
        developer = Developer("Test_4", 100, "Python")
        assert developer.programming_language != "", "Атрибут 'programming_language' присутній"


class Test_TeamLead:
    def test_teamlead_without_attributes(self) -> None:
        """
        Tests that attributes in TeamLead are empty when not provided
        :return: None
        """
        lead = TeamLead("Test_5", 1000, "Engineering", "Python", 0)
        assert lead.team_size == 0, "Атрибут 'team_size' відсутній"

    def test_teamlead_with_attributes(self) -> None:
        """
        Tests that attributes in TeamLead are filled when provided
        :return: None
        """
        lead = TeamLead("Test_6", 1000, "Engineering", "Python", 7)
        assert lead.team_size != 0, "Атрибут 'team_size' присутній"
