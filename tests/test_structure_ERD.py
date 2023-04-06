import pytest
from pages.page import Page


@pytest.fixture
def page(browser):
    return Page()


class TestStructureERD:
    #publish_data_count = 4

    def test_check_set_info_in_table(self, page):
        main_page = page.open_main_page()
        view_package_info_page = main_page.click_on_set_info_btn()
        view_package_info_page.check_table_data(publish_data_count='4', model_count='103')

        # set_info_page.check_MD_data('103')
        # set_info_page.check_table_data('298')
        # set_info_page.check_table_data('3504-9')
        # set_info_page.check_table_data('АО "Автомобильный завод "Урал"')
        # set_info_page.check_table_data('ПМ ИЭТР 4.4.0 / IETMWebServer 4.0.26')


#   Методика проверки просмотра структуры ЭРД      первый тест из ПМИ