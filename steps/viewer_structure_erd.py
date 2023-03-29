from .locators import ErdInformationLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage():
    # Добавляем конструктор (__init__) — метод, который вызывается, когда мы создаем объект.
    # передаем в качестве параметров экземпляр драйвера и url адрес.
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # добавляем метод open - он будет открывать нужную страницу в браузере, используя метод get().
    def open(self):
        self.browser.get(self.url)