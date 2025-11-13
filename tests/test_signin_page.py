import allure
import pytest

from indeepa_tests.pages.signin_page import SigninPage
from indeepa_tests.users.users import guest, admin
from testdata.invalid_emails import invalid_emails


@allure.feature('Авторизация')
@allure.story('Успешный вход')
def test_signin_page(setup_browser, panel, signin_page):
    panel.open_signin_form()
    signin_page.switch_to_new_window()
    signin_page.fill_signin_form(guest)
    signin_page.submit_form()
    signin_page.has_login_success()


@allure.feature('Авторизация')
@allure.story('Валидация email')
@pytest.mark.parametrize("invalid_email", invalid_emails)
def test_signin_email_validation(setup_browser, signin_page, invalid_email):
    signin_page.open()
    signin_page.fill_email(invalid_email)
    signin_page.fill_password(admin)
    signin_page.submit_click()
    signin_page.has_email_error("Невалидный")


# def test_blog_page
# def test_rates_page
# def test_rates_page_download_pdf