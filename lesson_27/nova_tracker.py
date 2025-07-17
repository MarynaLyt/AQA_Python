import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class NovaPoshtaTracker:
    def __init__(self, headless=True, timeout=10):
        self.url = "https://tracking.novaposhta.ua/#/uk"
        self.timeout = timeout
        self.driver = None
        self.wait = None
        self._setup_driver(headless)

    def _setup_driver(self, headless):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_package_status(self, tracking_number):
        try:
            self.driver.get(self.url)
            time.sleep(5)
            input_xpaths = [
                "//input[@id='en']",
                "//input[@class='track__form-group-input']",
                "//input[@placeholder='Номер посилки']"
            ]
            input_field = None
            for xpath in input_xpaths:
                try:
                    input_field = self.wait.until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    )
                    break
                except TimeoutException:
                    continue
            if not input_field:
                return None
            input_field.clear()
            input_field.send_keys(tracking_number)
            button_xpaths = [
                "//input[@id='np-number-input-desktop-btn-search-en']",
                "//input[@class='track__form-group-btn']",
                "//input[@value='Пошук']",
                "//input[@type='submit']"
            ]
            search_button = None
            for xpath in button_xpaths:
                try:
                    search_button = self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, xpath))
                    )
                    break
                except TimeoutException:
                    continue
            if not search_button:
                return None
            search_button.click()
            time.sleep(7)
            status_xpaths = [
                "//div[contains(text(), 'Отримана')]",
                "//*[contains(text(), 'Отримана')]",
                "//div[text()='Отримана']",
                "//span[contains(text(), 'Отримана')]",
                "//*[text()='Отримана']",
                "//div[contains(@class, 'status')]//text()[contains(., 'Отримана')]/..",
                "//*[contains(text(), 'отримана')]"
            ]
            for xpath in status_xpaths:
                try:
                    status_element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    )
                    status_text = status_element.text.strip()
                    if status_text:
                        return status_text
                except TimeoutException:
                    continue
            return None
        except Exception:
            return None

    def close(self):
        if self.driver:
            self.driver.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()