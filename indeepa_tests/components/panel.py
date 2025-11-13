from selene import browser, by


class Panel:
    def __init__(self):
        self.blog_button = browser.element(by.xpath("//a[@href='/blog']"))
        self.signin_button = browser.element(by.text('войти'))


    def open_signin_form(self):
        browser.open('https://www.indeepa.com/')
        self.signin_button.click()
        return self

    def open_blog(self):
        browser.open('https://www.indeepa.com/')
        self.blog_button.click()
        return self
