import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestExample:


    def test_title(self):
        print(self.driver.title)
        assert self.driver.title == "Facebook – log in or sign up"


    def test_url(self):
        print(self.driver.current_url)
        assert self.driver.current_url == "https://www.facebook.com/"


    def test_login_button(self):

        assert self.driver.find_element(By.NAME,"login").is_displayed()



    def test_prem(self):

        button= self.driver.find_element(By.NAME,"login").click()
        assert self.driver.find_element(By.XPATH,"//img[@class='_9ay6 img']").is_displayed()

