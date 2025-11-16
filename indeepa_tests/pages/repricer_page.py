import allure
from selene import browser, by, be

class RepricerPage:

    def __init__(self):
        self.presentation = browser.element(by.text('Скачать презентацию'))

    @allure.step("Открыть страницу формы тарифы")
    def open(self):
        browser.open('https://start.indeepa.com/')
        return self

    @allure.step("Кликнуть по кнопке 'Скачать презентацию'")
    def open_form_presentation(self):
        self.presentation.click()
        return self

    @allure.step("Проверить открытие формы заполнения контактных данных")
    def has_form_presentation_success(self):
        browser.element(
            by.text(
                'Оставьте ваши контакты, чтобы мы могли прислать презентацию о репрасере Indeepa.'
            )
        ).should(be.visible)
        return self
