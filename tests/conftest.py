import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="module")
def set_group():
    print("Enter System")
    yield
    print("Exit System")


@pytest.fixture()
def setup():
    print("initiating chrome driver")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service("C:\\Users\\Диана\\PycharmProjects\\resource\\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=g)

    yield driver
    driver.close()
