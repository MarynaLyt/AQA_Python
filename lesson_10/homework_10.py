"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import pytest


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'

    )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)
    for handler in logger.handlers:
        handler.flush()


LOG_FILE = "login_system.log"


def log_event(username: str, status: str):
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Налаштування логера
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger("log_event")

    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)
    for handler in logger.handlers:
        handler.flush()


@pytest.mark.parametrize(
    "username, status, expected_level",
    [
        ("test_user_success", "success", "INFO"),
        ("test_user_expired", "expired", "WARNING"),
        ("test_user_failed", "failed", "ERROR"),
        ("test_user_unknown", "blocked", "ERROR")
    ]
)
def test_log_event(username: str, status: str, expected_level: str, caplog):
    with caplog.at_level(logging.INFO):
        log_event(username, status)
    assert f"Username: {username}, Status: {status}" in caplog.text
    assert expected_level in caplog.text