import pytest
import requests
import helpers
from data import *
import allure

@allure.story('Тесты обновления данных пользователя')
class TestUserUpdate:
    @allure.title('Тест обновления данных пользователя с авторизацией')
    def test_update_user_with_auth(self, login_user):
        new_data = {
            "email": helpers.generate_random_email(),
            "name": helpers.generate_random_string()
        }
        headers = {"Authorization": login_user['accessToken']}
        response = requests.patch(URL.USER, json=new_data, headers=headers)
        print("Update user response:", response.json())
        assert response.status_code == 200

    @allure.title('Тест обновления данных пользователя без авторизации')
    def test_update_user_without_auth(self):
        # Тест на обновление данных пользователя без авторизации
        new_data = {
            "email": helpers.generate_random_email(),
            "name": helpers.generate_random_string()
        }
        response = requests.patch(URL.USER, json=new_data)
        print("Update user without auth response:", response.json())
        assert response.status_code == 401
        assert response.json()["message"] == Answers.UNAUTHORISED