import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth
from car_helpers import build_query_params, fetch_cars, validate_response

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


@pytest.fixture(scope="class")
def auth_session(request):
    logger.info("Початок аутентифікації")

    session = requests.Session()
    auth_data = HTTPBasicAuth('test_user', 'test_pass')

    try:
        logger.info(f"Відправка запиту аутентифікації на {BASE_URL}/auth")
        response = session.post(f"{BASE_URL}/auth", auth=auth_data)

        logger.info(f"Статус код аутентифікації: {response.status_code}")
        logger.info(f"Відповідь аутентифікації: {response.text}")

        assert response.status_code == 200, f"Authentication failed with status {response.status_code}"

        token = response.json().get("access_token")
        assert token, "No token received in response"

        logger.info("Токен успішно отримано")
        session.headers.update({"Authorization": f"Bearer {token}"})

        request.cls.session = session
        logger.info("Аутентифікація завершена успішно")

        yield session

    except Exception as e:
        logger.error(f"Помилка під час аутентифікації: {str(e)}")
        raise
    finally:
        logger.info("Закриття сесії")


@pytest.mark.usefixtures("auth_session")
class TestCarSearch:

    @pytest.mark.parametrize("sort_by,limit,test_description", [
        ("price", 2, "Сортування за ціною, ліміт 2"),
        ("year", 3, "Сортування за роком, ліміт 3"),
        ("engine_volume", 5, "Сортування за об'ємом двигуна, ліміт 5"),
        ("brand", 4, "Сортування за брендом, ліміт 4"),
        ("price", 10, "Сортування за ціною, ліміт 10"),
        ("year", 1, "Сортування за роком, ліміт 1"),
        ("", 7, "Без сортування (за замовчуванням), ліміт 7"),
    ])
    def test_car_search(self, sort_by, limit, test_description):
        logger.info(f"Початок тесту: {test_description}")
        logger.info(f"Параметри тесту - sort_by: '{sort_by}', limit: {limit}")

        try:
            params = build_query_params(sort_by, limit)
            logger.info(f"Сформовані параметри: {params}")

            response = fetch_cars(self.session, params)

            validate_response(response, limit)

            cars = response.json()
            logger.info(f"Отримано автомобілів: {len(cars)}")

            if cars:
                logger.info(f"Перший автомобіль у відповіді: {cars[0]}")

            required_fields = ['brand', 'year', 'engine_volume', 'price']
            for i, car in enumerate(cars):
                for field in required_fields:
                    assert field in car, f"Missing field '{field}' in car {i + 1}: {car}"

            logger.info(f"Тест '{test_description}' пройшов успішно")

        except Exception as e:
            logger.error(f"Тест '{test_description}' провалився: {str(e)}")
            raise

    def test_car_search_without_limit(self):
        logger.info("Тест пошуку без ліміту")

        try:
            params = {"sort_by": "price"}
            logger.info(f"Параметри запиту: {params}")

            response = self.session.get(f"{BASE_URL}/cars", params=params)
            logger.info(f"Статус код: {response.status_code}")

            assert response.status_code == 200
            cars = response.json()
            logger.info(f"Отримано автомобілів без ліміту: {len(cars)}")

            assert len(cars) == 25, f"Expected 25 cars, got {len(cars)}"

            logger.info("Тест без ліміту пройшов успішно")

        except Exception as e:
            logger.error(f"Тест без ліміту провалився: {str(e)}")
            raise

    def test_car_search_invalid_sort_field(self):
        logger.info("Тест з невалідним полем сортування")

        try:
            params = {"sort_by": "invalid_field", "limit": 3}
            logger.info(f"Параметри запиту: {params}")

            response = self.session.get(f"{BASE_URL}/cars", params=params)
            logger.info(f"Статус код: {response.status_code}")
            logger.info(f"Відповідь: {response.text}")

            assert response.status_code == 200
            cars = response.json()
            assert len(cars) <= 3

            logger.info("Тест з невалідним полем сортування пройшов успішно")

        except Exception as e:
            logger.error(f"Тест з невалідним полем провалився: {str(e)}")
            raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])