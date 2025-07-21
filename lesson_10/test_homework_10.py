import logging
import pytest
from homework_10 import log_event


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
