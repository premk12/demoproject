import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/datepicker/")
##click on date
driver.switch_to.frame(0)
# driver.find_element(By.ID,"datepicker").send_keys("05/10/2022")  ##button
#
year="2022"
month="August"
date="15"
driver.find_element(By.ID,"datepicker").click()
while True:

    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text #month

    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text  #Year

    if mon==month and yr==year:
        break
    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()

#select date
time.sleep(1)
dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break





