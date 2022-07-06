from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.makemytrip.com/")

print(driver.page_source)

# From = driver.find_element(By.ID,"fromCity").click()
#
# Del = driver.find_element(By.XPATH,"//input[@placeholder='From']").send_keys("j")
#
# cities = driver.find_elements(By.XPATH,"//div[@class='calc60']/p[@class='font14 appendBottom5 blackText']")
# print(len(cities))

# for cityname in cities:
#     print(cityname.text)
#     if cityname.text == "":
#         cityname.click()
#         break
# #








