import the as the
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')



