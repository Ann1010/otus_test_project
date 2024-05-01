import random
import string

import os
import random

import allure
import datetime

from api_tests.api_testing.pet_api import PetApi
from api_tests.api_testing.user_api import UserApi
from api_tests.helpers import checker as check

def generate_random_text_value(length: int = 8) -> str:
    """Генерация рандомной строки с длиной length"""
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def create_user(logger_test):
    with allure.step('Создание тестового пользователя'):
        user_api = UserApi(logger=logger_test)
        username = 'ivan_test'
        password = 'ivanov_ivan_password'
        body = {"id": 0,
                "username": username,
                "firstName": "Иван",
                "lastName": "Иванов",
                "email": "test@test.ru",
                "password": password,
                "phone": "+7(901)111-11-11",
                "userStatus": 0}
        response = user_api.post_user(body=body)
        return username, password
