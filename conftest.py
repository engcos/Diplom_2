import pytest
import helpers

@pytest.fixture
def create_user():
    user_data = helpers.register_new_user()
    assert user_data['status_code'] == 200
    yield user_data
    helpers.delete_user(user_data['json']['accessToken'])

@pytest.fixture
def login_user(create_user):
    response = helpers.login_user(create_user['email'], create_user['password'])
    assert response.status_code == 200
    return response.json()
