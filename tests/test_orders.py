import allure
import helpers
from data import TestData, Answers
import requests

@allure.story('Тесты создания заказов')
class TestOrderCreating:
    @allure.title('Тест создания заказа с авторизацией')
    def test_order_creating_with_authorization(self, login_user):
        response = helpers.create_order([TestData.INGREDIENT], login_user['accessToken'])
        print("Order creation with authorization response:", response.json())
        assert response.status_code == 200 and response.json()['success'] == Answers.TRUE

    @allure.title('Тест создания заказа без авторизации')
    def test_order_creating(self):
        response = helpers.create_order([TestData.INGREDIENT])
        print("Order creation without authorization response:", response.json())
        assert response.status_code == 200  # Проверка на создание заказа без авторизации

    @allure.title('Тест создания заказа без ингредиента')
    def test_order_creating_without_ingredient(self, login_user):
        response = helpers.create_order([], login_user['accessToken'])
        print("Order creation without ingredient response:", response.json())
        assert (response.status_code == 400 and
                response.json()['message'] == Answers.NO_INGREDIENTS)

    @allure.title('Тест создания заказа с неверным хэшем')
    def test_order_creating_with_incorrect_hash(self, login_user):
        response = helpers.create_order(['invalid_ingredient'], login_user['accessToken'])
        try:
            print("Order creation with incorrect hash response:", response.json())
        except requests.exceptions.JSONDecodeError:
            print("Order creation with incorrect hash response (non-JSON):", response.text)
        assert response.status_code == 500
