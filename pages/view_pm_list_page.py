from selenium.webdriver.common.by import By
from pages.manual_page import ManualPage
from pages.base_page import BasePage

class PublishListPage(BasePage):

    def manual_ietp1(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div.col-md-3:nth-child(4)")

    def manual_etpa2(self):
        return self.browser.find_element(By.XPATH, "//div[text()='Руководство по эксплуатации - Двигатель']/..")

    def click_on_manual_ietp1(self) -> ManualPage:
        self.manual_ietp1().click()
        return ManualPage()

    def search_input(self):
        return self.browser.find_element(By.CSS_SELECTOR, "#input-78")

    def search(self, search_text) -> ManualPage:
        self.search_input().send_keys(search_text)
        return self

    def click_on_manual_etpa2(self) -> ManualPage:
        self.manual_etpa2().click()
        return ManualPage()
