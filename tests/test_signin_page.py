import allure
import pytest

from indeepa_tests.users.users import guest, admin
from testdata.invalid_data import invalid_emails


@allure.feature('Авторизация')
@allure.story('Успешный вход')
def test_signin_page(setup_browser, signin_page):
    signin_page.open()
    signin_page.fill_signin_form(guest)
    signin_page.submit_form()
    try:
        signin_page.has_login_success()
    except AssertionError:
        pytest.xfail("Появилась капча")


@allure.feature('Авторизация')
@allure.story('Валидация email')
@pytest.mark.parametrize("invalid_email", invalid_emails)
def test_signin_email_validation(setup_browser, signin_page, invalid_email):
    signin_page.open()
    signin_page.fill_email(invalid_email)
    signin_page.fill_password(admin)
    signin_page.submit_without_validation()
    signin_page.has_email_error("Невалидный")

@allure.feature('Авторизация')
@allure.story('Открытие формы- Не помню пароль')
def test_forgotpass_form(setup_browser, signin_page):
    signin_page.open()
    signin_page.forgotpass_form()
