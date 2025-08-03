from enum import Enum
from selenium.webdriver.common.by import By


class ProfileLocators(Enum):
    USER_DROPDOWN_BUTTON = (By.XPATH, "//button[@id='userNavDropdown']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@class='btn btn-link text-danger btn-sidebar sidebar_btn']")