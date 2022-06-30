import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageobjects.loginpage import Login

from utilities.Baseclass import Baseclass


class Test_001_login(Baseclass):
    username="standard_user"
    password="secret_sauce"


    def test_homepage(self,setup):
        self.driver=setup
        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver= setup
        self.lp=Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.setlogin()
        self.lp.settask()
        self.lp.setlogout()
        act_title=self.driver.title
        if act_title == "Swag Labs":
            assert True
        else:
            assert False










