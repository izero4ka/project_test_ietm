from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MD040Page(BasePage):

    def open(self):
        self.open_url('http://localhost:8082/viewdm/URALM-A-A2-00-00-00A-041A-A')
        return self

    def back_btn(self):
        return self.browser.find_element(By.XPATH,
                                         "//button[contains(@class, 'v-btn--tile theme--dark v-size--default primary')]")

    def click_on_back_btn(self):
        from pages.manual_page import ManualPage
        self.back_btn().click()
        return ManualPage()

    def page_title(self):
        return self.browser.find_element(By.XPATH, "//div[contains(@class, 'md-title')]")
