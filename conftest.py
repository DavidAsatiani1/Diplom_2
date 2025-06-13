import pytest
import requests

from helpers import registration_user, delete_user, get_token, delete_user
from data import Endpoint


@pytest.fixture(scope='function')
def create_user():
    login_pass = registration_user()
    yield login_pass
    r_login = requests.post(Endpoint.AUTH_USER, data={
        'email': login_pass[0],
        'password': login_pass[1]
    })
    token = r_login.json()['accessToken']
    delete_user(token)

@pytest.fixture
def auth_user():
    token = get_token()
    yield token
    delete_user(token)