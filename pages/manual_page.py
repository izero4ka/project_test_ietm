from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.md_040_page import MD040Page


class ManualPage(BasePage):

    def title(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div.v-toolbar__title.ms-md-5")

    def wheels_tab(self):
        return self.browser.find_element(By.XPATH, "//span[text()='Подвеска и колёса']/../../../../../..")

    def radiator_tab(self):
        return self.browser.find_element(By.XPATH, "//span[text()='Блок радиатора']/../../../../../..")

    def tabs_inner_text(self):
        return self.browser.find_elements(By.XPATH, "//p[contains(@class, 'caption ma-0 d-inline-block')]")

    def tab_should_be_opened(self, element):
        assert element.get_attribute(name='aria-expanded') == 'true', f'Папка не открыта'

    def open_all_tabs_btn(self):
        return self.browser.find_element(By.XPATH, "//div[@class='mt-1 col-sm-1 col-2']//span[@class='v-btn__content']")

    def radiator_block_replacement_md(self):
        return self.browser.find_element(By.XPATH, "//span[text()='URALM-A-A2-20-02-00A-920A-A']")

    def engine_device_description_md(self):
        return self.browser.find_element(By.XPATH, "//span[text()='URALM-A-A2-00-00-00A-041A-A']")

    def open_tabs(self):
        if self.wheels_tab().get_attribute(name='aria-expanded') == 'false':
            self.wheels_tab().click()
        return self

    def check_inner_text(self, expected_text: str):
        for item in self.tabs_inner_text():
            assert expected_text in item.text, f'Конфиг не содержит текст {expected_text}'
        return self

    def check_inner_text_for_both_config(self):
        for item in self.tabs_inner_text():
            assert '4х4' in item.text or '6х6' in item.text, f'Конфиг не содержит текст 4х4 и 6х6'
        return self

    def click_on_open_all_tabs_btn(self):
        self.open_all_tabs_btn().click()
        return self

    def click_on_engine_device_description_md(self):
        self.engine_device_description_md().click()
        return MD040Page()

    def click_on_back_btn(self):
        from pages.view_pm_list_page import PublishListPage
        self.back_btn().click()
        return PublishListPage()






