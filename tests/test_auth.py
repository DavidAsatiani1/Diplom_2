import allure
import requests

from data import Endpoint, Message
from helpers import *


class TestAuthUser:
    @allure.step('Авторизация пользователя')
    def test_auth_courier(self, create_user):
        login_pass = create_user
        r = requests.post(Endpoint.AUTH_USER, data={
            'email': login_pass[0],
            'password': login_pass[1]
        })
        assert r.status_code == 200
        assert r.json()['success'] is True


    @allure.step('Авторизация пользователя без логина')
    def test_auth_without_login(self, create_user):
        login_pass = create_user
        r = requests.post(Endpoint.AUTH_USER, data={
            'email': '',
            'password': login_pass[1]
        })
        assert r.status_code == 401
        assert r.json()['success'] is False
        assert r.json()['message'] == Message.INCORRECT_DATA


    @allure.step('Авторизация пользователя без пароля')
    def test_auth_without_password(self, create_user):
        login_pass = create_user
        r = requests.post(Endpoint.AUTH_USER, data={
            'email': login_pass[0],
            'password': ''
        })
        assert r.status_code == 401
        assert r.json()['success'] is False
        assert r.json()['message'] == Message.INCORRECT_DATA


    @allure.step('Авторизация несуществующего пользователя')
    def test_auth_not_existing_courier(self):
        r = requests.post(Endpoint.AUTH_USER, data={
            'email': 'Ivan123456',
            'password': '12345678'
        })
        assert r.status_code == 401
        assert r.json()['success'] is False
        assert r.json()['message'] == Message.INCORRECT_DATA