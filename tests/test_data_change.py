import allure
import requests

from data import Message
from helpers import *


class TestDataChange:
    @allure.step('Изменение почты и пароля авторизованного пользователя')
    def test_change_data_auth_user(self):
        token = get_token()
        r = change_data_user(token)
        assert r.status_code == 200
        assert r.json()['success'] is True
        delete_user(token)


    @allure.step('Изменение почты и пароля неавторизованного пользователя')
    def test_change_data_unauth_user(self):
        token = ''
        r = change_data_user(token)
        assert r.status_code == 401
        assert r.json()['success'] is False
        assert r.json()['message'] == Message.UNAUTH