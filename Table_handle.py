from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")

## print company name
company=driver.find_element(By.XPATH,"//*[@id='customers']/tbody/tr[1]/th[1]")

print(f"print company name:{company.text}")


# ##print all no of rows
#
norow=(driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr"))
nocolumn=(driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr/th"))
#
print("Number of Rows:",len(norow))
print("Number of column:",len(nocolumn))

##Read specific row and column data
#
microsoft=driver.find_element(By.XPATH,"//table[@id='customers']/tbody/tr[4]/td[1]")

print(f"value of fourth row {microsoft.text}")


##Read all rows and column data

print("Printing all rows and column data ")
for i in range(2,len(norow)+1):
    for j in range (1,len(nocolumn)+1):
        data1 = driver.find_element(By.XPATH,"//table[@id='customers']/tbody/tr[" + str(i) + "]/td[" + str(j) + "]").text
        print(data1, end="               ")
    print()

##Read data on condition
for r in range(2, len(norow)+1):
    contact=driver.find_element(By.XPATH,"//table[@id='customers']/tbody/tr[" + str(r) + "]/td[2]").text
    if contact == "	Francisco Chang":
        company=driver.find_element(By.XPATH,"//table[@id='customers']/tbody/tr[" + str(r) + "]/td[1]").text
        print(contact,company)



















