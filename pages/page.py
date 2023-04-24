from helper.browser import Browser
from pages.main_page import MainPage
from pages.md_040_page import MD040Page

class Page(Browser):

    def open_main_page(self) -> MainPage:
        return MainPage().open()

    def open_md_040_page(self) -> MD040Page:
        return MD040Page().open()

    # def open_manaul_page(self) -> ManualPage:
    #     return ManualPage().open()