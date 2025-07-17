import pytest
from nova_tracker import NovaPoshtaTracker


class TestNovaPoshtaTracker:

    def test_get_package_status_success(self):
        tracking_number = "20451195765998"
        with NovaPoshtaTracker(headless=True) as tracker:
            status = tracker.get_package_status(tracking_number)
            assert status is not None
            assert len(status) > 0

    def test_package_status_matches_expected(self):
        tracking_number = "20451195765998"
        expected_status = "Отримана"
        with NovaPoshtaTracker(headless=True) as tracker:
            actual_status = tracker.get_package_status(tracking_number)
            assert actual_status == expected_status

    def test_invalid_tracking_number(self):
        tracking_number = "invalid123"
        with NovaPoshtaTracker(headless=True) as tracker:
            status = tracker.get_package_status(tracking_number)
            assert status is None