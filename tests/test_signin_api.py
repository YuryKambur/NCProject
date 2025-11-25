import allure
import requests
from jsonschema import validate

from indeepa_tests.users.users import guest
from testdata.expected_responses import SIGNIN_INVALID_SCHEMA, SIGNIN_SUCCESS_SCHEMA
from conftest import URL


@allure.feature('API Авторизация')
@allure.story('Успешная авторизация')
def test_api_signin_success():
    with allure.step('Отправить POST запрос на /Authorization/SignIn'):
        response = requests.post(
            f"{URL}/Authorization/SignIn",
            json={
                "email": guest.email,
                "password": guest.password,
            }
        )

    with allure.step('Проверить статус код 200'):
        assert response.status_code == 200, f"Получен статус {response.status_code}: {response.text}"

    with allure.step('Валидация структуры ответа'):
        response_data = response.json()
        allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.JSON)
        validate(instance=response_data, schema=SIGNIN_SUCCESS_SCHEMA)

    with allure.step('Проверить Content-Type в ответе'):
        assert 'application/json' in response.headers.get('Content-Type', ''), \
            f"Неверный Content-Type: {response.headers.get('Content-Type')}"


@allure.feature('API Авторизация')
@allure.story('Авторизация с невалидными данными')
def test_api_signin_invalid_password():
    with allure.step('Отправить запрос с неверным паролем'):
        response = requests.post(
            f"{URL}/Authorization/SignIn",
            json={
                "email": guest.email,
                "password": "wrong_password"
            }
        )

    with allure.step('Проверить статус код ошибки'):
        assert response.status_code == 400, f"Получен статус {response.status_code}: {response.text}"

    with allure.step('Валидация структуры ответа'):
        response_data = response.json()
        allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.JSON)
        validate(instance=response_data, schema=SIGNIN_INVALID_SCHEMA)

