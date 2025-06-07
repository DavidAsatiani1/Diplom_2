import allure
import requests

from data import Message
from helpers import *


class TestOrderList:
    @allure.step('Получение заказов авторизованным пользователем')
    def test_get_order_list_auth_user(self):
        token = get_token()
        list = get_order_list(token)
        assert list.status_code == 200
        assert list.json()['success'] is True
        delete_user(token)


    @allure.step('Получение заказов неавторизованным пользователем')
    def test_get_order_list_unauth_user(self):
        token = ''
        list = get_order_list(token)
        assert list.status_code == 401
        assert list.json()['success'] is False
        assert list.json()['message'] == Message.UNAUTH