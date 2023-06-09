from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

