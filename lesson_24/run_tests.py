#!/usr/bin/env python3

import subprocess
import sys
import time
import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

BASE_URL = "http://127.0.0.1:8080"


def check_server_status():
    try:
        response = requests.get(f"{BASE_URL}/cars", timeout=5)
        return True
    except requests.exceptions.RequestException:
        return False


def wait_for_server(max_attempts=10, delay=2):
    logger.info("Перевірка доступності сервера...")

    for attempt in range(max_attempts):
        if check_server_status():
            logger.info("Сервер доступний")
            return True

        logger.info(f"Спроба {attempt + 1}/{max_attempts}: сервер недоступний, очікування...")
        time.sleep(delay)

    return False


def run_tests():
    if not wait_for_server():
        logger.error("Сервер недоступний. Переконайтесь, що Flask додаток запущено на http://127.0.0.1:8080")
        logger.error("Для запуску сервера виконайте: python cars_app.py")
        return False

    logger.info("Запуск тестів...")

    cmd = [
        sys.executable, "-m", "pytest",
        "test_cars_api.py",
        "-v",
        "--tb=short",
        "--capture=no",
        "-s",
        "--color=yes"
    ]

    try:
        result = subprocess.run(cmd, check=False)

        if result.returncode == 0:
            logger.info("Всі тести пройшли успішно!")
            return True
        else:
            logger.error(f"Деякі тести провалилися. Код виходу: {result.returncode}")
            return False

    except Exception as e:
        logger.error(f"Помилка під час запуску тестів: {e}")
        return False


def main():
    logger.info("Автоматизований запуск тестів Flask API")

    required_files = ["test_cars_api.py", "car_helpers.py"]
    missing_files = []

    import os
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)

    if missing_files:
        logger.error(f"Відсутні файли: {', '.join(missing_files)}")
        return False

    success = run_tests()

    if success:
        logger.info("Тестування завершено успішно")
        logger.info("Детальні логи збережено у файл: test_search.log")
    else:
        logger.info("Тестування завершено з помилками")
        logger.info("Детальні логи збережено у файл: test_search.log")

    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)