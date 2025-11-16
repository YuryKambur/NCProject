import allure
import pytest

from indeepa_tests.users.users import admin
from testdata.invalid_data import invalid_password, invalid_emails


@allure.feature('Регистрация')
@allure.story('Валидация email')
@pytest.mark.parametrize("invalid_email", invalid_emails)
def test_signup_email_validation(setup_browser, signup_page, invalid_email):
    signup_page.open()
    signup_page.fill_email(invalid_email)
    signup_page.submit_without_validation()
    signup_page.has_email_error("Невалидный")

@pytest.mark.parametrize("invalid_password", invalid_password)
def test_signup_password_validation(setup_browser, signup_page, invalid_password):
    signup_page.open()
    signup_page.fill_password(invalid_password)
    signup_page.submit_without_validation()
    signup_page.has_password_error("Невалидный")