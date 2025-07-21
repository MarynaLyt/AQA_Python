import logging

LOG_FILE = "login_system.log"


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.
    status: Статус події входу: success, expired або failed.
    """
    log_message = f"Login event - Username: {username}, Status: {status}"
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        force=True
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
