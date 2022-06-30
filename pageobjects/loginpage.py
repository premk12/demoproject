import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Login:
    text_username_xpath=(By.XPATH,"//input[@id='user-name']")
    text_password_xpath=(By.XPATH,"//input[@id='password']")
    button_login_xpath=(By.XPATH,"//input[@id='login-button']")
    button_taskbar_xpath=(By.XPATH,"//button[@id='react-burger-menu-btn']")
    button_logout_xpath=(By.XPATH,"//a[@id='logout_sidebar_link']")

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element(*Login.text_username_xpath).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(*Login.text_password_xpath).send_keys(password)

    def setlogin(self):
        self.driver.find_element(*Login.button_login_xpath).click()

    def settask(self):
        self.driver.find_element(*Login.button_taskbar_xpath).click()

    def setlogout(self):
        self.driver.find_element(*Login.button_logout_xpath).click()




