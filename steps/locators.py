from selenium.webdriver.common.by import By


class BasePageLocators():
    CHAPTER_SELECTION = (By.CSS_SELECTOR, "div.m-btn:nth-child(2)") # Выбор глав и разделов
    PLANNED_MAINTENANCE = (By.CSS_SELECTOR, "div.m-btn:nth-child(3)") # Плановое ТО
    CURRENT_REPAIRS = (By.CSS_SELECTOR, "div.m-btn:nth-child(4)") # Текущий ремонт
    DOCUMENTATION_SEARCH = (By.CSS_SELECTOR, "div.m-btn:nth-child(5)") # Поиск по документации
    SCENARIOS = (By.CSS_SELECTOR, "div.m-btn:nth-child(6)") # Сценарии
    COLLECTION_OPERATIONAL_DATA = (By.CSS_SELECTOR, "div.m-btn:nth-child(7)") # Сбор данных об эксплуатции
    LIBRARY = (By.CSS_SELECTOR, "a.mt-12:nth-child(3)") # Библотека
    INFORMATION_ABOUT_ERD = (By.CSS_SELECTOR, ".mr-10") # Сведения о комплекте ЭРД
    PRODUCT_CONFIGURATION_SELECTION = (By.CSS_SELECTOR, ".ml-10") # Выборрать конфигурацию изделия


class ChoisePublicationLocators():
    OPERATOR_MANUAL = (By.CSS_SELECTOR, "div.row:nth-child(3) > div:nth-child(1)") # 1 публикация
    MAINTENANCE_MANUAL = (By.CSS_SELECTOR, "div.col-md-3:nth-child(2)") # 2 публикация
    OPERATING_ENGINE_MANUAL = (By.CSS_SELECTOR, "div.row:nth-child(3) > div:nth-child(3)") # 3 публикация
    OPERATION_URAL_MANUAL = (By.CSS_SELECTOR, "div.col-md-3:nth-child(4)") # 4 публикация


class MainLocators():
    BACK_BLUE = (By.CSS_SELECTOR, ".mdi-arrow-left") # Кнопка синяя назад
    PROPERTIES_MD = (By.CSS_SELECTOR, ".mdi-information") # Кнопка свойства МД
    PLAY_VIDEO = (By.CSS_SELECTOR, "div.multimedia:nth-child(4)") # Кнопка старта видео


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
    FOUR_FOUR = (By.CSS_SELECTOR, "div.col-md-3:nth-child(1)") # 4x4
    SIX_SIX = (By.CSS_SELECTOR, "div.col-md-3:nth-child(2)") # 6x6

class Search():
    STR_SEARCH = (By.CSS_SELECTOR, "") # Строка поиска
    ADVANCED_SEARCH = (By.CSS_SELECTOR, "") # Расширенный поиск
    ACROSS_ALL_FOLDERS = (By.CSS_SELECTOR, "")
    WHOLE_WORD = (By.CSS_SELECTOR, "")
    CASE_SENSITIVE = (By.CSS_SELECTOR, "")
    SEARCH_REPLACEMENT = (By.CSS_SELECTOR, "")
    FULLTEXT_SEARCH = (By.CSS_SELECTOR, "")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "") # Кнопка поиска
    INSTRUCTIONS_CREW = (By.CSS_SELECTOR, "")
    DESCRIPTIVE = (By.CSS_SELECTOR, "")
    PROCEDURAL = (By.CSS_SELECTOR, "")
    ELECTRICAL_INSTALLATION = (By.CSS_SELECTOR, "")
    ILLUSTRATED_CATALOGS = (By.CSS_SELECTOR, "")
    PLANNING_TD = (By.CSS_SELECTOR, "")
    CONSUMPTION_RATES_SPARE_PARTS_MATERIALS = (By.CSS_SELECTOR, "")
    PROCESS = (By.CSS_SELECTOR, "")
    TROUBLESHOOTING = (By.CSS_SELECTOR, "")
    HISTORY = (By.CSS_SELECTOR, "") # Истоиря поиска