from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_28.locators.home_page_locators import HomePageLocators

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_registration(self):
        self.wait.until(EC.element_to_be_clickable(HomePageLocators.SIGN_IN_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(HomePageLocators.REGISTRATION_TAB)).click()