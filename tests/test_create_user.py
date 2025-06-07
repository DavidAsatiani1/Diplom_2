import allure
import requests
import pytest


class TestUser:
    @allure.step('Регистрация пользователя')
    def test_create_user(self):
        email, password, name = generate_data()
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        r = requests.post(Endpoint.CREATE_USER, data=payload)
        assert r.status_code == 200
        assert r.json()['success'] is True


    @allure.step('Регистрация существующего пользователя')
    def test_create_exist_user(self):
        login_pass = registration_user()
        r = requests.post(Endpoint.CREATE_USER, data={
            'email': login_pass[0],
            'password': login_pass[1],
            'name': login_pass[2]
        })
        assert r.status_code == 403
        assert r.json()['success'] is False
        assert r.json()['message'] == Message.EXIST_USER


    @allure.step('Регистрация пользователя без почты/пароля')
    @pytest.mark.parametrize('field', ['email', 'password'])
    def test_create_user_without_one_field(self, field):
        payload = generate_data_payload()
        del payload[field]
        r = requests.post(Endpoint.CREATE_USER, data=payload)
        assert r.status_code == 403
        assert r.json()['success'] is False
        assert r.json()['message'] == Message.USER_WITHOUT_DATA