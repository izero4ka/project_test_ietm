from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ViewPackageInfoPage(BasePage):

    def back_btn(self):
        return self.browser.find_element(By.XPATH, "//div[@class='v-toolbar__content']/a")

    def publish_data_count_text(self):
        return self.browser.find_element(By.XPATH, "//td[text()='Публикаций']/following-sibling::*")

    def model_count_text(self):
        return self.browser.find_element(By.XPATH, "//td[text()='Модулей данных']/following-sibling::*")

    def multimedia_objects_count_text(self):
        return self.browser.find_element(By.XPATH, "//td[text()='Иллюстраций и мультимедиа объектов']/following-sibling::*")

    def developer_id_text(self):
        return self.browser.find_element(By.XPATH, "//td[text()='Разработчик']/following-sibling::*")

    def provider_name_text(self):
        return self.browser.find_element(By.XPATH, "//td[text()='Поставщик']/following-sibling::*")

    def kit_info_text(self):
        return self.browser.find_element(By.XPATH, "//td[text()='Комплект содержит сведения']/following-sibling::*")

    def system_version_text(self):
        return self.browser.find_element(By.XPATH, "//td[text()='Версия ЭСО']/following-sibling::*")

    def check_table_data(self, publish_data_count, model_count, multimedia_objects_count, developer_id,
                         provider_name, kit_info, system_version):
        self.objects_should_be_equal(publish_data_count, self.publish_data_count_text().text)
        self.objects_should_be_equal(self.model_count_text().text, model_count)
        self.objects_should_be_equal(self.multimedia_objects_count_text().text, multimedia_objects_count)
        self.objects_should_be_equal(developer_id, self.developer_id_text().text)
        self.objects_should_be_equal(self.provider_name_text().text, provider_name)
        self.objects_should_be_equal(self.kit_info_text().text, kit_info)
        self.objects_should_be_equal(self.system_version_text().text, system_version)

    def click_on_back_btn(self):
        from pages.main_page import MainPage
        self.back_btn().click()
        return MainPage()
