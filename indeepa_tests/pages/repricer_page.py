
import allure
from selene import browser, by, be



class RepricerPage:

    def __init__(self):
        self.presentation = browser.element(by.text('Скачать презентацию'))

    def open(self, retries=3):
        with allure.step("Открыть страницу формы тарифы"):
            browser.open('https://start.indeepa.com/')
            return self

    def open_form_presentation(self):
        self.presentation.click()
        return self

    def has_form_presentation_success(self):
        with allure.step("Проверить открытие формы заполнения контактных данных"):
            browser.element(by.text('Оставьте ваши контакты, чтобы мы могли прислать презентацию о репрасере Indeepa.')).should(be.visible)
        return self
