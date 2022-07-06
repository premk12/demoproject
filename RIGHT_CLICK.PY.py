from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://demo.guru99.com/test/simple_context_menu.html")

#right click

rclick=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
from selenium.webdriver import ActionChains

act=ActionChains(driver)

act.context_click(rclick).perform()

edit=driver.find_element(By.XPATH,"//li[@class='context-menu-item context-menu-icon context-menu-icon-edit']")

act.move_to_element(edit).click().perform()

#alert pop up

alertwindow=driver.switch_to.alert

alertwindow.accept() # click on ok

