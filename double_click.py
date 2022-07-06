from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.guru99.com/test/simple_context_menu.html")


##double click

doublec=driver.find_element(By.XPATH,"//button[contains(text(),'Double-Click Me To See Alert')]")

from selenium.webdriver import ActionChains

act=ActionChains(driver)

act.double_click(doublec).perform()

# aler

alertwindow=driver.switch_to.alert

alertwindow.accept()