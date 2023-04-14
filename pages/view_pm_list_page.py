from selenium.webdriver.common.by import By
from pages.manual_page import ManualPage
from pages.base_page import BasePage

class PublishListPage(BasePage):

    def manual_ietp1(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div.col-md-3:nth-child(4)")

    def click_on_manual_ietp1(self) -> ManualPage:
        self.manual_ietp1().click()
        return ManualPage()