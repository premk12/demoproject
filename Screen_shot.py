from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://demo.guru99.com/test/simple_context_menu.html")


driver.get_screenshot_as_file("screenshot2.png")