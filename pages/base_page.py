from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from helper.browser import Browser


class BasePage(Browser):

    def back_btn(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div.v-toolbar__content>a")

    def click_on_back_btn(self):
        from pages.main_page import MainPage
        self.back_btn().click()
        return MainPage()

    @staticmethod
    def text_should_be(element, expected_text):
        assert element.text == expected_text, f'Неверный текст элемента'
