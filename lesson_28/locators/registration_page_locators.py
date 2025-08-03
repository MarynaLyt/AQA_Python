from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    NAME = (By.ID, "signupName")
    LAST_NAME = (By.ID, "signupLastName")
    EMAIL = (By.ID, "signupEmail")
    PASSWORD = (By.ID, "signupPassword")
    PASSWORD_CONFIRM = (By.ID, "signupRepeatPassword")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Register']")