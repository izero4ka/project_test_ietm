from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from helper.browser import Browser


class BasePage(Browser):

    def back_btn(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div.v-toolbar__content>a")
