from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ManualPage(BasePage):

    def title(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div.v-toolbar__title.ms-md-5")

    def wheels_tab(self):
        return self.browser.find_element(By.XPATH, "//span[text()='Подвеска и колёса']/../../../../../..")

    def tabs_inner_text(self):
        return self.browser.find_elements(By.XPATH, "//p[contains(@class, 'caption ma-0 d-inline-block')]")

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






