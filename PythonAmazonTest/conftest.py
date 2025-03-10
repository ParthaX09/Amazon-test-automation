import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    # driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()