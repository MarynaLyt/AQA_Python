from selenium.webdriver.common.by import By


class HomePageLocators:
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(@class, 'header_signin') and text()='Sign In']")
    REGISTRATION_TAB = (By.XPATH, "//button[@type='button' and contains(@class, 'btn-link') and text()='Registration']")