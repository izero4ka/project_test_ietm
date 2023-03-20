import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestPMI():

    @pytest.fixture(scope="function", autouse=True)
    def browser(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_link_and_button(self, browser):
        url = "http://localhost:8082/"
        time.sleep(3)
        browser.get(url)
        browser.find_element(By.XPATH,
                             "/html/body/div[1]/div/main/div/div/div/div[1]/div[2]/div/div[2]/div[2]/a/span/span").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div/div/header/div/a/span/i").click()
        time.sleep(3)

    @pytest.mark.pmi
    def test_TC85(self, browser):
    link = "http://localhost:8082/"


    @pytest.mark.pmi
    def test_TC86(self, browser):
    link = "http://localhost:8082/"


    @pytest.mark.pmi
    def test_TC87(self, browser):
    link = "http://localhost:8082/"


    @pytest.mark.pmi
    def test_TC88(self, browser):
    link = "http://localhost:8082/"


    @pytest.mark.pmi
    def test_TC89(self, browser):
    link = "http://localhost:8082/"


    @pytest.mark.pmi
    def test_TC90(self, browser):
    link = "http://localhost:8082/"


    @pytest.mark.pmi
    def test_TC91(self, browser):
    link = "http://localhost:8082/"


    @pytest.mark.pmi
    def test_TC92(self, browser):
    link = "http://localhost:8082/"


    @pytest.mark.pmi
    def test_TC93(self, browser):
    link = "http://localhost:8082/"


    @pytest.mark.pmi
    def test_TC95(self, browser):
    link = "http://localhost:8082/"


    @pytest.mark.pmi
    def test_TC96(self, browser):
    link = "http://localhost:8082/"


    @pytest.mark.pmi
    def test_TC102(self, browser):
    link = "http://localhost:8082/"


    @pytest.mark.pmi
    def test_TC103(self, browser):
    link = "http://localhost:8082/"


    @pytest.mark.pmi
    def test_TC104(self, browser):
    link = "http://localhost:8082/"


    @pytest.mark.pmi
    def test_TC105(self, browser):
    link = "http://localhost:8082/"
    