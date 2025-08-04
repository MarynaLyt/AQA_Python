import logging
import requests

BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('test_search.log', mode='w')
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def build_query_params(sort_by, limit):
    params = {"limit": limit}
    if sort_by:
        params["sort_by"] = sort_by
    logger.info(f"Testing with params: {params}")
    return params


def fetch_cars(session, params):
    response = session.get(f"{BASE_URL}/cars", params=params)
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {response.text}")
    return response


def validate_response(response, limit):
    assert response.status_code == 200, "Request failed"
    cars = response.json()
    assert isinstance(cars, list), "Response is not a list"
    assert len(cars) <= limit, f"Returned more cars than expected: {len(cars)} > {limit}"