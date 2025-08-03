from enum import Enum
from selenium.webdriver.common.by import By


class HomePageLocators(Enum):
    SIGN_UP_BUTTON = (By.XPATH, "//button[@class='hero-descriptor_btn btn btn-primary']")