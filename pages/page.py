from helper.browser import Browser
from pages.main_page import MainPage


class Page(Browser):

    def open_main_page(self) -> MainPage:
        return MainPage().open()
