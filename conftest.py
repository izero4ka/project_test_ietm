import pytest

from selenium import webdriver

from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):#определяет функцию pytest_addoption, которая будет вызвана перед началом выполнения тестов Pytest
    parser.addoption('--browser_name', action='store', default="Chrome",#добавляет опцию командной строки --browser_name, которая указывает, какой браузер должен быть запущен для тестирования. Значение по умолчанию - Chrome
                     help="Выберите браузер: Chrome или Firefox")
    parser.addoption('--language', action='store', default="en",#добавляет опцию командной строки --language, которая указывает, какой язык должен быть использован для локализации веб-страниц. Значение по умолчанию - английский
                     help="Выберите язык: ru, en or fr")


@pytest.fixture(scope="function")#определяет фикстуру Pytest, которая обеспечивает запуск браузера и его закрытие после каждого тестирования.
def browser(request):#определяет функцию browser, которая вызывается Pytest для создания браузера
    browser_name = request.config.getoption("browser_name")#получает значение параметра --browser_name из командной строки, который указывает, какой браузер должен быть запущен
    user_language = request.config.getoption("language")#получает значение параметра --language из командной строки, который указывает, на каком языке должны быть локализованы веб-страницы.
    browser = None#создает переменную browser и присваивает ей значение None
    if browser_name == "Chrome":#проверяет, какой браузер был выбран для тестирования
        options = Options()#создает экземпляр класса Options, используемый для настройки предпочтений пользователя в Chrome
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})#добавляет параметр 'intl.accept_languages' для опции 'prefs' класса Options, который указывает нужный пользовательский язык.
        print("\nЗапуск браузера Chrome для теста..")#добавляет параметр 'intl.accept_languages' для опции 'prefs' класса Options, который указывает нужный пользовательский язык
        browser = webdriver.Chrome(options=options)#создает экземпляр класса webdriver для браузера Firefox с настройками, определенными в профиле Firefox
    elif browser_name == "Firefox":#если был выбран неверный браузер, то вызывается исключение
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nЗапуск браузера Firefox для теста..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name должно быть Chrome или Firefox")#вызывает ошибку использования TypeError, если параметр --browser_name был указан неверно
    yield browser#возвращает браузер
    print("\nЗакрытие браузера..")#выводит сообщение о том, что браузер закрывается
    browser.quit()#закрывает браузер после завершения теста
