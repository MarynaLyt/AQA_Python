import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lesson_28.page_objects.registration_page import RegistrationPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    yield driver
    driver.quit()

@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)