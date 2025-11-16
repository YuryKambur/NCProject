import allure
from selene import browser, by, be, have
from selenium.webdriver.support.wait import WebDriverWait

from indeepa_tests.users.users import User


class SigninPage:

    def __init__(self):
        self.email = browser.element('[formcontrolname="email"]')
        self.password = browser.element('[formcontrolname="pass"]')
        self.submit = browser.element(
            by.xpath("//button[span[normalize-space(text())='Войти']]")
        )
        self.email_error = browser.element(by.text('Невалидный'))
        self.forgotpass = browser.element(by.text('Не помню пароль'))

    def open(self):
        with allure.step("Открыть страницу формы авторизации"):
            browser.open('https://id.indeepa.com/#/signin')
        return self

    def fill_email(self, value):
        with allure.step(f"Заполнить email: {value}"):
            self.email.type(value)
        return self

    def fill_password(self, value):
        with allure.step(f"Заполнить пароль"):
            self.password.type(value)
        return self

    def fill_signin_form(self, user: User):
        with allure.step(f"Заполнить форму данными пользователя {user.email}"):
            (self.fill_email(user.email).fill_password(user.password))
        return self

    def submit_form(self):
        with allure.step("Нажать кнопку Войти"):
            self.submit.should(be.visible).should(be.enabled)
            self.submit.click()
        return self

    def submit_without_validation(self):
        with allure.step("Кликнуть на кнопку Войти без проверки активности"):
            self.submit.click()
        return self

    def has_login_success(self):
        with allure.step("Проверить успешный вход"):
            browser.element(
                by.text('Ваши контактные данные для эффективной коммуникации')
            ).should(be.visible)
        return self

    def has_email_error(self, expected_text):
        with allure.step("Проверить валидацию email"):
            self.email_error.should(be.visible)
            self.email_error.should(have.text(expected_text))
        return self

    def switch_to_new_window(self):
        with allure.step("Переключиться на новую вкладку"):
            WebDriverWait(browser.driver, 10).until(lambda d: len(d.window_handles) > 1)
            browser.driver.switch_to.window(browser.driver.window_handles[-1])
        return self

    def forgotpass_form(self):
        with allure.step("Открыть форму смены забытого пароля"):
            self.forgotpass.should(be.visible).click()
            browser.element(by.text('СМЕНА ПАРОЛЯ')).should(be.visible)
        return self
