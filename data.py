class URL:
    BASE = 'https://stellarburgers.nomoreparties.site/api'
    ORDER = f'{BASE}/orders'
    LOGIN = f'{BASE}/auth/login'
    REGISTER = f'{BASE}/auth/register'
    USER = f'{BASE}/auth/user'
    USER_ORDERS = f'{BASE}/orders'
    DELETE_USER = f'{BASE}/auth/user'


class Answers:
    DUPLICATE_USER = 'User already exists'
    REQUIRED_FIELD = 'Email, password and name are required fields'
    TRUE = True
    INCORRECT = 'email or password are incorrect'
    UNAUTHORISED = 'You should be authorised'
    NO_INGREDIENTS = 'Ingredient ids must be provided'
    UPDATE_EXIST_EMAIL = 'User with such email already exists'


class TestData:
    INGREDIENT = '61c0c5a71d1f82001bdaaa6d'

