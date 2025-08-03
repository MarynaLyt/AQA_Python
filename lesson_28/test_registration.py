import time
import random


def test_user_registration(driver, home_page, registration_form, account_page):
    driver.find_element(*home_page.SIGN_UP_BUTTON).click()
    driver.find_element(*registration_form.NAME_INPUT).send_keys("Марина")
    driver.find_element(*registration_form.LAST_NAME_INPUT).send_keys("Тест")

    random_email = f"maryna_test_{random.randint(1000, 9999)}@mail.com"
    driver.find_element(*registration_form.EMAIL_INPUT).send_keys(random_email)

    driver.find_element(*registration_form.PASSWORD_INPUT).send_keys("StrongPassword1")
    driver.find_element(*registration_form.CONFIRM_PASSWORD_INPUT).send_keys("StrongPassword1")

    driver.find_element(*registration_form.REGISTER_BUTTON).click()

    time.sleep(2)

    assert driver.find_element(*account_page.USER_DROPDOWN).is_displayed()
