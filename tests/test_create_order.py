import allure
import requests

from data import Message, Order
from helpers import *


class TestCreateOrder:
    @allure.step('Создать заказ с авторизацией')
    def test_create_order_auth_user(self, create_user):
        user = create_user
        order = create_order(Order.ORDER_WITH_INGREDIENTS)
        assert order.status_code == 200
        assert order.json()['success'] is True


    @allure.step('Создать заказ без авторизации')
    def test_create_order_unauth_user(self):
        order = create_order(Order.ORDER_WITH_INGREDIENTS)
        assert order.status_code == 200
        assert order.json()['success'] is True


    @allure.step('Создать заказ без ингредиентов')
    def test_create_order_auth_user_without_ingredients(self, create_user):
        user = create_user
        order = create_order(Order.ORDER_DATA_WITHOUT_INGREDIENTS)
        assert order.status_code == 400
        assert order.json()['success'] is False
        assert order.json()['message'] == Message.ORDER_WITHOUT_INGREDIENTS


    @allure.step('Создать заказ с неверным хешем ингредиентов')
    def test_create_order_auth_user_wrong_hash(self, create_user):
        user = create_user
        order = create_order(Order.ORDER_DATA_WITH_WRONG_HASH)
        assert order.status_code == 500
        assert 'Internal Server Error' in order.text