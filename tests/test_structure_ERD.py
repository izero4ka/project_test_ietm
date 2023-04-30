import allure
import pytest
from pages.page import Page


pytest_mark = [allure.parent_suite("ИЭТР"), allure.suite("Методика испытаний"), allure.sub_suite("ЭРД")]

@pytest.fixture
def page(browser):
    return Page()


class TestStructureERD:

    @pytest.mark.xfail(reason="Инициализация билда")
    def test_init_build(self, page):
        main_page = page.open_main_page()

    def test_check_set_info_in_table(self, page):
        main_page = page.open_main_page()
        main_page.check_title('Электронная эксплуатационная и ремонтная документация'.upper())
        view_package_info_page = main_page.click_on_set_info_btn()
        view_package_info_page.check_table_data(publish_data_count='4', model_count='103',
                                                multimedia_objects_count='298', developer_id='3504-9',
                                                provider_name='АО "Автомобильный завод "Урал"',
                                                kit_info='с 10-11-2020 по 12-10-2021',
                                                system_version='ПМ ИЭТР 4.4.6 / IETMWebServer 4.0.26')
        main_page = view_package_info_page.click_on_back_btn()
        main_page.check_title('Электронная эксплуатационная и ремонтная документация'.upper())

    def test_check_configurations_select_4x4(self, page):
        main_page = page.open_main_page()
        config_page = main_page.click_on_configuration_btn()
        config_page.choose_config(config_type='4x4')
        main_page = config_page.click_on_back_btn()
        public_view_page = main_page.click_on_publish_menu_item()
        manual_page = public_view_page.click_on_manual_ietp1()
        manual_page.open_tabs()
        manual_page.check_inner_text('4х4')

    def test_check_configurations_select_6x6(self, page):
        main_page = page.open_main_page()
        config_page = main_page.click_on_configuration_btn()
        config_page.choose_config(config_type='6x6')
        main_page = config_page.click_on_back_btn()
        public_view_page = main_page.click_on_publish_menu_item()
        manual_page = public_view_page.click_on_manual_ietp1()
        manual_page.open_tabs()
        manual_page.check_inner_text('6х6')

    def test_check_configurations_select_4x4_and_6x6(self, page):
        main_page = page.open_main_page()
        config_page = main_page.click_on_configuration_btn()
        config_page.choose_config(config_type='4x4')
        config_page.choose_config(config_type='6x6')
        main_page = config_page.click_on_back_btn()
        public_view_page = main_page.click_on_publish_menu_item()
        manual_page = public_view_page.click_on_manual_ietp1()
        manual_page.open_tabs()
        manual_page.check_inner_text_for_both_config()

    def test_check_configurations_not_selected(self, page):
        main_page = page.open_main_page()
        public_view_page = main_page.click_on_publish_menu_item()
        manual_page = public_view_page.click_on_manual_ietp1()
        manual_page.open_tabs()
        manual_page.check_inner_text_for_both_config()

    def test_search_view_pm_list(self, page):
        main_page = page.open_main_page()
        public_view_page = main_page.click_on_publish_menu_item()
        public_view_page.search(search_text="двигатель")
        public_view_page.manual_etpa2().is_displayed()
        manual_page = public_view_page.click_on_manual_etpa2()
        manual_page.text_should_be(manual_page.title(), expected_text='URALM-SFX44-ETPA2-00')
        manual_page.click_on_open_all_tabs_btn()
        manual_page.tab_should_be_opened(manual_page.radiator_tab())
        manual_page.radiator_block_replacement_md().is_displayed()
        md_040_page = manual_page.click_on_engine_device_description_md()
        md_040_page.text_should_be(md_040_page.page_title(), 'Двигатель - Описание устройства')
        manual_page = md_040_page.click_on_back_btn()
        manual_page.text_should_be(manual_page.title(), expected_text='URALM-SFX44-ETPA2-00')
        public_view_page = manual_page.click_on_back_btn()
        public_view_page.text_should_be(public_view_page.title(),
                                        'Выберите раздел эксплуатационной и ремонтной документации'.upper())
