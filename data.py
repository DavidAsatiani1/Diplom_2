from faker import Faker


class Endpoint:
    STELLAR_BURGERS_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = f'{STELLAR_BURGERS_URL}/api/auth/register'
    AUTH_USER = f'{STELLAR_BURGERS_URL}/api/auth/login'
    ORDER = f'{STELLAR_BURGERS_URL}/api/orders'
    DATA_CHANGE = f'{STELLAR_BURGERS_URL}/api/auth/user'


class Order:
    ORDER_WITH_INGREDIENTS = {
        'ingredients': ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa75']
    }
    ORDER_DATA_WITHOUT_INGREDIENTS = {
        'ingredients': []
    }
    ORDER_DATA_WITH_WRONG_HASH = {
        'ingredients': ['60d3b41abdacab0026a733', '609646e4dc916e00276b28']
    }


class Message:
    EXIST_USER = 'User already exists'
    USER_WITHOUT_DATA = 'Email, password and name are required fields'
    INCORRECT_DATA = 'email or password are incorrect'
    UNAUTH = 'You should be authorised'
    ORDER_WITHOUT_INGREDIENTS = 'Ingredient ids must be provided'


class User:
    fake = Faker()
    FAKE_USER = {'email': fake.email(), 'password': fake.password()}