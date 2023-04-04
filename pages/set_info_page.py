from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SetInfoPage(BasePage):

    def publish_data(self):
        return self.browser.find_element(By.XPATH, "//td[text()='Публикаций']/following-sibling::*")

    def check_table_data(self, publish_data: str):
        assert self.publish_data().text == publish_data, f'Не верные данные в кол. публикаций'
