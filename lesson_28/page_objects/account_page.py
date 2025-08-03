from locators.account import AccountLocators


class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element(*AccountLocators.USER_NAME_LABEL.value).text
