import pytest
import requests
from requests.auth import HTTPBasicAuth
from lesson_24.car_helpers import build_query_params, fetch_cars, validate_response

BASE_URL = "http://127.0.0.1:8080"

@pytest.fixture(scope="class")
def auth_session(request):
    session = requests.Session()
    auth_data = HTTPBasicAuth('test_user', 'test_pass')
    response = session.post(f"{BASE_URL}/auth", auth=auth_data)
    assert response.status_code == 200, "Authentication failed"
    token = response.json().get("access_token")
    assert token, "No token received"
    session.headers.update({"Authorization": f"Bearer {token}"})
    request.cls.session = session


@pytest.mark.usefixtures("auth_session")
class TestCarSearch:

    @pytest.mark.parametrize("sort_by,limit", [
        ("price", 2),
        ("year", 3),
        ("engine_volume", 5),
        ("brand", 4),
        ("price", 10),
        ("year", 1),
        ("", 3),
    ])
    def test_car_search(self, sort_by, limit):
        params = build_query_params(sort_by, limit)
        response = fetch_cars(self.session, params)
        validate_response(response, limit)