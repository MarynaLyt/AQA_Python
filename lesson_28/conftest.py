import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.home_page import HomePage
from page_objects.registration_form import RegistrationForm
from page_objects.account_page import AccountPage


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless")  # Прибери, якщо хочеш бачити браузер
    driver = webdriver.Chrome(options=options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    yield driver
    driver.quit()


@pytest.fixture
def home_page():
    return HomePage


@pytest.fixture
def registration_form():
    return RegistrationForm


@pytest.fixture
def account_page(driver):
    return AccountPage