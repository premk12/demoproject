import pytest
from selenium import webdriver



# @pytest.fixture()
# def setup(request):
#     driver = webdriver.Chrome()
#     driver.get("https://www.saucedemo.com/")
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     request.cls.driver = driver
#
#     yield driver
#     driver.close()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name =request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver=webdriver.Chrome()
    elif browser_name == "firefox":
        driver= webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield driver
    driver.close()




