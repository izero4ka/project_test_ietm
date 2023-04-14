from selenium import webdriver


class Browser:
    browser: webdriver.Firefox

    def __init__(self):
        pass

    def open_url(self, url):
        return self.browser.get(url)

    def refresh_page(self):
        return self.browser.refresh()

    def get_url(self):
        return self.browser.current_url

    def objects_should_be_equal(self, first_object, second_object):
        assert first_object == second_object, f'Объект {first_object} должен ровняться объекту {second_object}'
        return self