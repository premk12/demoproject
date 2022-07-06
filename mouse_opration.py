from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.softwaretestingmaterial.com/blog/")

# Click on Tutorials


from selenium.webdriver import ActionChains

act=ActionChains(driver)
tutorials=driver.find_element(By.XPATH,"//span[@class='nav-drop-title-wrap']")
api=driver.find_element(By.XPATH,"//li[@id='menu-item-17002']")

act.move_to_element(tutorials).perform()  ## move on tutorials

act.move_to_element(api).click().perform()  ## click on api


