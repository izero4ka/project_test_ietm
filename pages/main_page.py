from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from pages.set_info_page import SetInfoPage


class MainPage(BasePage):
    home_page_link = "http://localhost:8082/"

    def open(self):
        self.open_url(self.home_page_link)
        return self

    def set_info_btn(self) -> WebElement:
        # Сведения о комплекте ЭРД
        return self.browser.find_element(By.CSS_SELECTOR, ".mr-10")

    def click_on_set_info_btn(self) -> SetInfoPage:
        self.set_info_btn().click()
        return SetInfoPage()
