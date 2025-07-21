import requests
import time
import json

BASE_URL = "http://localhost:5001"  # Правильний порт 5001


def wait_for_app():
    """Очікування запуску додатку"""
    print("🔄 Очікування запуску додатку...")
    for i in range(30):
        try:
            response = requests.get(f"{BASE_URL}/health", timeout=5)
            if response.status_code == 200:
                print("✅ Додаток готовий!")
                return True
        except:
            pass
        print(f"Очікування... ({i + 1}/30)")
        time.sleep(2)
    return False


def test_health():
    """Тест 1: Health check"""
    print("\n🔍 Тест 1: Health check")
    try:
        response = requests.get(f"{BASE_URL}/health")
        data = response.json()
        print(f"Статус: {response.status_code}")
        print(f"Відповідь: {json.dumps(data, indent=2, ensure_ascii=False)}")
        assert response.status_code == 200
        assert data["status"] == "healthy"
        print("✅ Health check успішний")
        return True
    except Exception as e:
        print(f"❌ Health check провалений: {e}")
        return False


def test_database_connection():
    """Тест 2: Підключення до бази даних"""
    print("\n🔍 Тест 2: Підключення до БД")
    try:
        response = requests.get(f"{BASE_URL}/test-connection")
        data = response.json()
        print(f"Статус: {response.status_code}")
        print(f"Відповідь: {json.dumps(data, indent=2, ensure_ascii=False)}")
        assert response.status_code == 200
        assert data["status"] == "success"
        assert data["user"] == "marynalytvynenko"
        assert data["database"] == "mydatabase"
        print("✅ Підключення до БД успішне")
        return True
    except Exception as e:
        print(f"❌ Тест підключення до БД провалений: {e}")
        return False


def test_create_user():
    """Тест 3: Створення користувача (INSERT)"""
    print("\n🔍 Тест 3: Створення користувача")
    try:
        user_data = {
            "name": "Марина Литвиненко",
            "email": "marina.test@example.com"
        }

        response = requests.post(f"{BASE_URL}/users", json=user_data)
        data = response.json()
        print(f"Статус: {response.status_code}")
        print(f"Відповідь: {json.dumps(data, indent=2, ensure_ascii=False)}")

        assert response.status_code == 201
        assert data["status"] == "success"
        assert "user_id" in data

        print(f"✅ Користувач створений з ID: {data['user_id']}")
        return data["user_id"]
    except Exception as e:
        print(f"❌ Тест створення користувача провалений: {e}")
        return None


def test_get_users():
    """Тест 4: Отримання користувачів (SELECT)"""
    print("\n🔍 Тест 4: Отримання користувачів")
    try:
        response = requests.get(f"{BASE_URL}/users")
        data = response.json()
        print(f"Статус: {response.status_code}")
        print(f"Відповідь: {json.dumps(data, indent=2, ensure_ascii=False)}")

        assert response.status_code == 200
        assert data["status"] == "success"
        assert "users" in data
        assert "count" in data

        print(f"✅ Отримано {data['count']} користувачів")
        return data["users"]
    except Exception as e:
        print(f"❌ Тест отримання користувачів провалений: {e}")
        return None


def test_delete_user(user_id):
    """Тест 5: Видалення користувача (DELETE)"""
    print(f"\n🔍 Тест 5: Видалення користувача {user_id}")
    try:
        response = requests.delete(f"{BASE_URL}/users/{user_id}")
        data = response.json()
        print(f"Статус: {response.status_code}")
        print(f"Відповідь: {json.dumps(data, indent=2, ensure_ascii=False)}")

        assert response.status_code == 200
        assert data["status"] == "success"

        print("✅ Користувач видалений успішно")
        return True
    except Exception as e:
        print(f"❌ Тест видалення користувача провалений: {e}")
        return False


def test_crud_operations():
    """Повний CRUD тест"""
    print("\n🧪 Повний CRUD тест:")

    # CREATE - створити кілька користувачів
    users_created = []
    test_users = [
        {"name": "Тест Користувач 1", "email": "test1@example.com"},
        {"name": "Тест Користувач 2", "email": "test2@example.com"}
    ]

    for user_data in test_users:
        response = requests.post(f"{BASE_URL}/users", json=user_data)
        if response.status_code == 201:
            user_id = response.json()["user_id"]
            users_created.append(user_id)
            print(f"✓ Створено користувача: {user_data['name']} (ID: {user_id})")

    # READ - прочитати всіх
    response = requests.get(f"{BASE_URL}/users")
    if response.status_code == 200:
        count = response.json()["count"]
        print(f"✓ Загалом користувачів: {count}")

    # DELETE - видалити створених
    for user_id in users_created:
        response = requests.delete(f"{BASE_URL}/users/{user_id}")
        if response.status_code == 200:
            print(f"✓ Видалено користувача ID: {user_id}")

    print("🎉 CRUD тести завершені!")


def run_all_tests():
    """Запуск всіх тестів"""
    print("🚀 Початок тестування ДЗ 29.1")
    print("=" * 50)

    if not wait_for_app():
        print("❌ Додаток не запустився")
        return False

    tests_passed = 0
    total_tests = 5

    # Основні тести
    if test_health():
        tests_passed += 1

    if test_database_connection():
        tests_passed += 1

    user_id = test_create_user()
    if user_id:
        tests_passed += 1

    if test_get_users():
        tests_passed += 1

    if user_id and test_delete_user(user_id):
        tests_passed += 1

    # Додатковий CRUD тест
    test_crud_operations()

    # Результати
    print("\n" + "=" * 50)
    print(f"📊 Результати тестування:")
    print(f"✅ Пройдено: {tests_passed}/{total_tests}")
    print(f"❌ Провалено: {total_tests - tests_passed}/{total_tests}")

    if tests_passed == total_tests:
        print("🎉 Всі основні тести пройшли успішно!")
        print("✅ ДЗ 29.1 виконано правильно!")
        return True
    else:
        print("⚠️ Деякі тести провалились")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)