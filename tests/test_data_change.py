import allure
import requests
import pytest

from data import Message, Endpoint
from helpers import registration_user, change_data_user, delete_user, get_token


class TestDataChange:
    @allure.step('Изменение почты и пароля авторизованного пользователя')
    def test_change_data_auth_user(self, create_user):
        token = get_token()  # Получаем токен для авторизованного пользователя
        r = change_data_user(token)
        assert r.status_code == 200
        assert r.json()['success'] is True

    @allure.step('Изменение почты и пароля неавторизованного пользователя')
    def test_change_data_unauth_user(self):
        token = ''
        r = change_data_user(token)
        assert r.status_code == 401
        assert r.json()['success'] is False
        assert r.json()['message'] == Message.UNAUTH
