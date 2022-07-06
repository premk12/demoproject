from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://seleniumbase.io/demo_page")


from selenium.webdriver import ActionChains

act=ActionChains(driver)

hover=driver.find_element(By.XPATH,"//div[@id='myDropdown']")
link2=driver.find_element(By.XPATH,"//a[@id='dropOption2']")


act.move_to_element(hover).move_to_element(link2).click().perform()
