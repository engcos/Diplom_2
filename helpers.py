import requests
import allure
import random
import string
from data import URL

@allure.step('Генерация случайной строки')
def generate_random_string(length=10):
    """Генерируем случайную строку указанной длины."""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

@allure.step('Генерация случайного email')
def generate_random_email():
    """Генерируем случайный email адрес."""
    return f"{generate_random_string()}@example.com"

@allure.step('Регистрация нового пользователя и возврат его данных')
def register_new_user():
    """Регистрация нового пользователя и возврат его данных."""
    email = generate_random_email()
    password = generate_random_string()
    name = generate_random_string()

    payload = {
        'email': email,
        'password': password,
        'name': name
    }

    response = requests.post(URL.REGISTER, json=payload)
    if response.status_code == 200:
        return {
            'email': email,
            'password': password,
            'name': name,
            'status_code': response.status_code,
            'json': response.json()
        }
    print("Register new user response:", response.json())
    return response.json()

@allure.step('Регистрация пользователя с указанными данными')
def register_user(email, password, name):
    """Регистрация пользователя с указанными данными."""
    payload = {
        'email': email,
        'password': password,
        'name': name
    }
    response = requests.post(URL.REGISTER, json=payload)
    return {
        'email': email,
        'password': password,
        'name': name,
        'status_code': response.status_code,
        'json': response.json()
    }

@allure.step('Удаление пользователя')
def delete_user(access_token):
    """Удаление пользователя по access token."""
    headers = {'Authorization': f'Bearer {access_token}' if not access_token.startswith('Bearer ') else access_token}
    response = requests.delete(URL.DELETE_USER, headers=headers)
    print("Delete user response:", response.json())
    return response

@allure.step('Авторизация пользователя')
def login_user(email, password):
    """Авторизация пользователя с указанным email и паролем."""
    payload = {'email': email, 'password': password}
    response = requests.post(URL.LOGIN, json=payload)
    print("Login user response:", response.json())
    return response

@allure.step('Создание заказа')
def create_order(ingredients=None, access_token=None):
    """Создание заказа с указанными ингредиентами и access token."""
    payload = {'ingredients': ingredients or []}
    headers = {'Authorization': f'Bearer {access_token}' if access_token and not access_token.startswith(
        'Bearer ') else access_token} if access_token else {}
    response = requests.post(URL.ORDER, json=payload, headers=headers)
    try:
        print("Create order response:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("Create order response (non-JSON):", response.text)
    return response

@allure.step('Получение списка заказов')
def get_user_orders(access_token=None):
    """Получение списка заказов пользователя по access token."""
    headers = {'Authorization': f'Bearer {access_token}' if access_token and not access_token.startswith(
        'Bearer ') else access_token} if access_token else {}
    response = requests.get(URL.USER_ORDERS, headers=headers)
    try:
        print("Get user orders response:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("Get user orders response (non-JSON):", response.text)
    return response
