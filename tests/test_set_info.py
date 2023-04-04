import pytest
from pages.main_page import MainPage
from pages.page import Page


@pytest.fixture
def page(browser):
    return Page()


class TestSetInfo:

    def test_check_set_info_in_table(self, page):
        main_page = page.open_main_page()
        set_info_page = main_page.click_on_set_info_btn()
        set_info_page.check_table_data('4')
