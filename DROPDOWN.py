
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://seleniumbase.io/demo_page")


inputElement = driver.find_element(By.XPATH, '//*[@id="mySelect"]/option[3]')
inputElement.click()        # Manual way to do this.. which creates complexity when we multiple combinations

## -------------------------------------------------------------------

inputElement = driver.find_element(By.ID, "mySelect")
dropdown = Select(inputElement)
#
time.sleep(3)
dropdown.select_by_index(3)

time.sleep(3)
dropdown.select_by_value("25%")

time.sleep(3)
dropdown.select_by_visible_text("Set to 100%")


print(len(dropdown.options))

for option in dropdown.options:
    print(option.text)
    print(option.get_attribute('value'))


