import pytest
from pages.page import Page


@pytest.fixture
def page(browser):
    return Page()


class TestStructureERD:
    # publish_data_count = 4

    def test_check_set_info_in_table(self, page):
        main_page = page.open_main_page()
        view_package_info_page = main_page.click_on_set_info_btn()
        view_package_info_page.check_table_data(publish_data_count='4', model_count='103',
                                                multimedia_objects_count='298', developer_id='3504-9',
                                                provider_name='АО "Автомобильный завод "Урал"',
                                                kit_info='с 10-11-2020 по 12-10-2021',
                                                system_version='ПМ ИЭТР 4.4.0 / IETMWebServer 4.0.26')
        main_page = view_package_info_page.click_on_back_btn()
        main_page.check_title('Электронная эксплуатационная и ремонтная документация'.upper())

    def test_check_configurations_select_4x4(self, page):
        main_page = page.open_main_page()
        config_page = main_page.click_on_configuration_btn()
        config_page.choose_config(config_type='4x4')
        main_page = config_page.click_on_back_btn()
        public_view_page = main_page.click_on_publish_menu_item()
        manual_page = public_view_page.click_on_manual_ietp1()


    # для 4на4

    # def check_configurations_select_6x6(self, page):
    # для 6на6

    # def check_configurations_select_4x4_6x6(self, page):
    # когда выбраны 4на4 и 6на6

    # def check_configurations_not_select(self, page):
    # когда не выбрана ни одна
