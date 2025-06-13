import requests
from faker import Faker
from data import Endpoint, User
import allure

fake = Faker()

def generate_data():
    email = fake.email()
    password = fake.password()
    name = fake.name()
    return email, password, name

def generate_data_payload():
    email, password, name = generate_data()
    payload = {
        'email': email,
        'password': password,
        'name': name
    }
    return payload

@allure.step('Регистрация пользователя')
def registration_user():
    login_pass = []
    payload = generate_data_payload()
    r = requests.post(Endpoint.CREATE_USER, data=payload)
    if r.status_code == 200:
        login_pass.append(payload['email'])
        login_pass.append(payload['password'])
        login_pass.append(payload['name'])
    return login_pass

@allure.step('Логин пользователя')
def login_user():
    login_pass = registration_user()
    payload = {
        'email': login_pass[0],
        'password': login_pass[1]
    }
    r = requests.post(Endpoint.AUTH_USER, data=payload)
    return r

@allure.step('Получение токена')
def get_token():
    login = login_user()
    token = login.json()['accessToken']
    return token

@allure.step('Удаление пользователя')
def delete_user(token):
    headers = {"Authorization": token}
    requests.delete(Endpoint.DATA_CHANGE, headers=headers)

@allure.step('Изменение данных пользователя')
def change_data_user(token):
    body = User.FAKE_USER
    r = requests.patch(Endpoint.DATA_CHANGE, json=body, headers={"Authorization": token})
    return r

@allure.step('Создание заказа')
def create_order(data):
    r = requests.post(Endpoint.ORDER, json=data)
    return r

@allure.step('Получение списка заказов')
def get_order_list(token):
    r = requests.get(Endpoint.ORDER, headers={"Authorization": token})
    return r