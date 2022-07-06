from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")

##print company name

company=driver.find_element(By.XPATH,"//th[normalize-space()='Company']")

print(company.text)

## print allno of rows

norow=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")

print(len(norow))

nocolumn=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr/th")

print(len(nocolumn))


##read specific row and column data
for i in range(4,len(norow)-2):
    for s in range(1,len(nocolumn)+1):
        data2=driver.find_element(By.XPATH,"//table[@id='customers']/tbody/tr["+str(i)+"]/td["+str(s)+"]").text

        print(data2, end="       ")
    print()

##Read all rows and column data

# print("All data of table")
#
for a in range(2,len(norow)+1):
    for b in range(1,len(nocolumn)+1):
        data1=driver.find_element(By.XPATH,"//table[@id='customers']/tbody/tr["+str(a)+"]/td["+str(b)+"]").text
        print(data1, end="        ")
    print()
#

