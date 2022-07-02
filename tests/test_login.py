import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageobjects.loginpage import Login

from utilities.Baseclass import Baseclass
from utilities.custom_logger import LogGen


class Test_001_login(Baseclass):
    username="standard_user"
    password="secret_sauce"
    logger = LogGen.loggen()


    def test_homepage(self,setup):
        self.logger. ("**********Test 001_login********")
        self.logger.("***********Verify home page********")
        self.driver=setup
        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
            self.logger.info("****Home page title passes*****")
        else:
            self.logger.info("****Home page title found error*****")

            assert False

    def test_login(self,setup):
        self.logger.info("****verify login test***")
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
            self.logger.info("****verify login test is pass****")
        else:
            self.logger.info("****login test fail*****")
            assert False










