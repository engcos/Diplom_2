import pytest
import allure
import requests
import helpers
from data import URL, Answers

@allure.story('Тесты регистрации и логина')
class TestUserRegistration:
    @allure.title('Тест регистрации нового пользователя')
    def test_register_user(self):
        response = helpers.register_new_user()
        print("Register new user response:", response)
        assert response['status_code'] == 200
        assert response['json']['success'] == True

    @allure.title('Тест регистрации уже существующего пользователя')
    def test_register_existing_user(self):
        # регистрируем пользователя
        user_data = helpers.register_new_user()
        # Пробуем зарегистрировать его снова
        response = helpers.register_user(user_data['email'], user_data['password'], user_data['name'])
        print("Response for existing user:", response)
        assert response['status_code'] == 403

    @allure.title('Тест регистрации пользователя с отсутствующим полем')
    def test_register_user_missing_fields(self):
        # Тест на регистрацию пользователя с отсутствующим полем
        payload = {
            'email': helpers.generate_random_email(),
            'password': helpers.generate_random_string()
        }
        response = requests.post(URL.REGISTER, json=payload)
        print("Register user with missing fields response:", response.json())
        assert response.status_code == 403
        assert response.json()['message'] == Answers.REQUIRED_FIELD

@allure.story('Тесты логина')
class TestUserLogin:
    @allure.title('Тест логина с корректными данными')
    def test_login_user(self, create_user):
        response = helpers.login_user(create_user['email'], create_user['password'])
        print("Login user response:", response.json())
        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title('Тест логина с некорректными данными')
    def test_login_invalid_credentials(self):
        response = helpers.login_user('invalid@example.com', 'invalidpassword')
        print("Login with invalid credentials response:", response.json())
        assert response.status_code == 401
        assert response.json()['message'] == Answers.INCORRECT
