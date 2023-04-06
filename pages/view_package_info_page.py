from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ViewPackageInfoPage(BasePage):

    def publish_data_count_text(self):
        return self.browser.find_element(By.XPATH, "//td[text()='Публикаций']/following-sibling::*")

    def model_count_test(self):
        return self.browser.find_element(By.XPATH, "//td[text()='Модулей данных']/following-sibling::*")

    def click_on_back_btn(self):
        from pages.main_page import MainPage
        self.back_btn().click()
        return MainPage()

    def check_table_data(self, publish_data_count: str, model_count: str):
        publish_count = self.publish_data_count_text().text
        assert publish_count == publish_data_count,\
            f'Неверные данные в кол. публикаций, expected count: {publish_data_count}' \
            f' actual count: {publish_count}'
        assert self.model_count_test().text == model_count, f'Неверные данные в кол. модулей данных'

    # def MD_data(self):
    #     return self.browser.find_element(By.XPATH, "//td[text()='Модулей данных']/following-sibling::*")
    #
    # def check_MD_data(self, MD_data: str):
    #     assert self.MD_data().text == MD_data, f'Неверные данные в кол. МД'
