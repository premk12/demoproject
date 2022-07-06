import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.worldometers.info/geography/flags-of-the-world/")

# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


driver.execute_script("window.scrollBy(0,4374.39)","")

value=driver.execute_script("return window.pageYOffset;")

print("pixel moved",value)

# ##till element visible

# flag=driver.find_element(By.XPATH,"//img[@src='/img/flags/small/tn_in-flag.gif']")
#
# driver.execute_script("arguments[0].scrollIntoView();",flag)
#
# value=driver.execute_script("return window.pageYOffset;")
#
# print("pixel moved",value)
#
