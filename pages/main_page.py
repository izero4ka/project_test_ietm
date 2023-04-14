from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from pages.view_package_info_page import ViewPackageInfoPage
from pages.configurations_page import ConfigurationPage
from pages.view_pm_list_page import PublishListPage


class MainPage(BasePage):
    home_page_link = "http://localhost:8082/"

    def open(self):
        self.open_url(self.home_page_link)
        return self

    def title(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div.d-flex.flex-column>div.mt-12>p")

    def check_title(self, title_text):
        self.objects_should_be_equal(self.title().text, title_text)

    def configuration_btn(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".ml-10")

    def set_info_btn(self) -> WebElement:
        # Сведения о комплекте ЭРД
        return self.browser.find_element(By.CSS_SELECTOR, ".mr-10")

    def publish_list_menu_item(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div.m-btn:nth-child(2)")

    def click_on_set_info_btn(self) -> ViewPackageInfoPage:
        self.set_info_btn().click()
        return ViewPackageInfoPage()

    def click_on_configuration_btn(self) -> ConfigurationPage:
        self.configuration_btn().click()
        return ConfigurationPage()

    def click_on_publish_menu_item(self) -> PublishListPage:
        self.publish_list_menu_item().click()
        return PublishListPage()
