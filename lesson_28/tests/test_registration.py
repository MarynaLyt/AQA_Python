from lesson_28.page_objects.home_page import HomePage
from lesson_28.page_objects.registration_page import RegistrationPage


def test_user_registration(driver):
    home_page = HomePage(driver)
    registration_page = RegistrationPage(driver)

    home_page.go_to_registration()

    registration_page.fill_registration_form(
        name="Test",
        last_name="User",
        email="testuser@example.com",
        password="Password123"
    )
    registration_page.submit()

    assert driver.title == "Hillel Qauto"