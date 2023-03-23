from selenium.webdriver.common.by import By


class BasePageLocators():
    CHAPTER_SELECTION = (By.CSS_SELECTOR, "div.m-btn:nth-child(2)")
    PLANNED_MAINTENANCE = (By.CSS_SELECTOR, "div.m-btn:nth-child(3)")
    CURRENT_REPAIRS = (By.CSS_SELECTOR, "div.m-btn:nth-child(4)")
    DOCUMENTATION_SEARCH = (By.CSS_SELECTOR, "div.m-btn:nth-child(5)")
    SCENARIOS = (By.CSS_SELECTOR, "div.m-btn:nth-child(6)")
    COLLECTION_OPERATIONAL_DATA = (By.CSS_SELECTOR, "div.m-btn:nth-child(7)")
    LIBRARY = (By.CSS_SELECTOR, "a.mt-12:nth-child(3)")
    INFORMATION_ABOUT_ERD = (By.CSS_SELECTOR, ".mr-10")
    PRODUCT_CONFIGURATION_SELECTION = (By.CSS_SELECTOR, ".ml-10")


class ChoisePublicationLocators():
    OPERATOR_MANUAL = (By.CSS_SELECTOR, "div.row:nth-child(3) > div:nth-child(1)")
    MAINTENANCE_MANUAL = (By.CSS_SELECTOR, "div.col-md-3:nth-child(2)")
    OPERATING_ENGINE_MANUAL = (By.CSS_SELECTOR, "div.row:nth-child(3) > div:nth-child(3)")
    OPERATION_URAL_MANUAL = (By.CSS_SELECTOR, "div.col-md-3:nth-child(4)")


class MainLocators():
    BACK_BLUE = (By.CSS_SELECTOR, ".mdi-arrow-left")
    PROPERTIES_MD = (By.CSS_SELECTOR, ".mdi-information")
    PLAY_VIDEO = (By.CSS_SELECTOR, "div.multimedia:nth-child(4)")


class ErdInformationLocators():
    PUBLICATIONS = (By.CSS_SELECTOR,
                    ".v-data-table__wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)")
    MD = (By.CSS_SELECTOR,
          ".v-data-table__wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(2)")
    MULTIMEDIA = (By.CSS_SELECTOR,
                  ".v-data-table__wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2)")
    DEVELOPER = (By.CSS_SELECTOR,
                 ".v-data-table__wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(2)")
    VENDOR = (By.CSS_SELECTOR,
              ".v-data-table__wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(2)")
    KIT_INFORMATION = (By.CSS_SELECTOR,
                       ".v-data-table__wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(2)")
    ESO = (By.CSS_SELECTOR,
           ".v-data-table__wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(7) > td:nth-child(2)")
class ConfigurationSelectionLocators():
    FOUR_FOUR = (By.CSS_SELECTOR, "div.col-md-3:nth-child(1)")
    SIX_SIX = (By.CSS_SELECTOR, "div.col-md-3:nth-child(2)")
