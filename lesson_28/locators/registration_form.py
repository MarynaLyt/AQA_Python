from enum import Enum
from selenium.webdriver.common.by import By


class RegistrationFormLocators(Enum):
    NAME_INPUT_FIELD = (By.XPATH, "//input[@id='signupName']")
    LAST_NAME_INPUT_FIELD = (By.XPATH, "//input[@id='signupLastName']")
    EMAIL_INPUT_FIELD = (By.XPATH, "//input[@id='signupEmail']")
    PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@id='signupPassword']")
    RE_ENTER_PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@id='signupRepeatPassword']")
    REGISTER_BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")
