import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import FrameLocators

URL = "http://localhost:8000/dz.html"


@pytest.mark.parametrize("frame_id, input_id, secret_text", [
    ("frame1", "input1", "Frame1_Secret"),
    ("frame2", "input2", "Frame2_Secret"),
])
def test_frame_verification(driver, frame_id, input_id, secret_text):
    wait = WebDriverWait(driver, 10)
    driver.get(URL)
    time.sleep(1)

    driver.switch_to.default_content()
    driver.switch_to.frame(frame_id)
    time.sleep(1)

    input_field = driver.find_element(*FrameLocators.INPUT)
    input_field.clear()
    time.sleep(0.5)
    input_field.send_keys(secret_text)
    time.sleep(1)

    driver.find_element(*FrameLocators.BUTTON).click()
    time.sleep(1)

    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    print(f"[{frame_id}] Alert: {alert_text}")
    assert alert_text == "Верифікація пройшла успішно!"
    time.sleep(1)
    alert.accept()

    time.sleep(1)
