from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://seleniumbase.io/demo_page")


dropper=driver.find_element(By.ID,"mySelect")

dropper1=Select(dropper)

dropper1.select_by_value("75%")


alloptions=dropper1.options
print(len(alloptions))

for opt in alloptions:
    opt.text
    print(opt.text)
