from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_title():
    driver=webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    print(driver.title)
    assert driver.title == "Facebook – log in or sign up"


def test_url():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    print(driver.current_url)
    assert driver.current_url == "https://www.facebook.com/"


def test_login_button():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    assert driver.find_element(By.NAME,"login").is_displayed()



def test_prem():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    button= driver.find_element(By.NAME,"login").click()
    assert driver.find_element(By.XPATH,"//img[@class='_9ay6 img']").is_displayed()













