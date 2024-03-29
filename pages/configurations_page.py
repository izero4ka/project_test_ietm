from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ConfigurationPage(BasePage):

    def back_btn(self):
        return self.browser.find_element(By.XPATH, "//div[@class='v-toolbar__content']/a")

    def config_4x4(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div.col-md-3:nth-child(1)")

    def config_6x6(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div.col-md-3:nth-child(2)")

    def choose_config(self, config_type='4x4'):
        if config_type == '4x4':
            self.config_4x4().click()
        else:
            self.config_6x6().click()
        return self

    def click_on_back_btn(self):
        from pages.main_page import MainPage
        self.back_btn().click()
        return MainPage()
