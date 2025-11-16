import allure
from selene import browser, by, be, have


class SignupPage:

    def __init__(self):
        self.email = browser.element('[formcontrolname="email"]')
        self.password = browser.element('[formcontrolname="pass"]')
        self.submit = browser.element(
            by.xpath("//button[span[normalize-space(text())='Зарегистрироваться']]")
        )
        self.email_error = browser.element(by.text('Невалидный'))
        self.password_error = browser.element(by.text('Невалидный'))
        self.forgotpass = browser.element(by.text('Не помню пароль'))

    def open(self):
        with allure.step("Открыть страницу формы регистрации"):
            browser.open('https://id.indeepa.com/#/signup')
        return self

    def has_email_error(self, expected_text):
        with allure.step("Проверить валидацию email"):
            self.email_error.should(be.visible)
            self.email_error.should(have.text(expected_text))
        return self

    def has_password_error(self, expected_text):
        with allure.step("Проверить валидацию password"):
            self.password_error.should(be.visible)
            self.password_error.should(have.text(expected_text))
        return self

    def fill_email(self, value):
        with allure.step(f"Заполнить email: {value}"):
            self.email.type(value)
        return self

    def fill_password(self, value):
        with allure.step(f"Заполнить пароль"):
            self.password.type(value)
        return self

    def submit_without_validation(self):
        with allure.step("Кликнуть на кнопку Войти без проверки активности"):
            self.submit.click()
        return self
