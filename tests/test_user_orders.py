import pytest
import helpers
import allure

@allure.story('Тесты получения заказов пользователя')
class TestUserOrders:
    @allure.title('Тест получения заказов пользователя с авторизацией')
    def test_get_user_orders_with_auth(self, login_user):
        response = helpers.get_user_orders(login_user['accessToken'])
        print("Get user orders with auth response:", response.json())
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title('Тест получения заказов пользователя без авторизации')
    def test_get_user_orders_without_auth(self):
        response = helpers.get_user_orders()
        print("Get user orders without auth response:", response.json())
        assert response.status_code == 401
