import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome() #if not added in PATH
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()

@pytest.fixture()
def loaddata():
    print("user data will be proceed")
    return ["9372301650","Prem1896@"]