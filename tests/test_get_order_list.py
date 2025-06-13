import allure
import requests
import pytest

from data import Message
from helpers import get_token, get_order_list, delete_user

class TestOrderList:
    @allure.step('Получение заказов авторизованным пользователем')
    def test_get_order_list_auth_user(self, auth_user):
        token = auth_user
        response = get_order_list(token)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.step('Получение заказов неавторизованным пользователем')
    def test_get_order_list_unauth_user(self):
        token = ''
        response = get_order_list(token)
        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json()['message'] == Message.UNAUTH