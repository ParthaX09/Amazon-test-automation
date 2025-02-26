from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    searchBox = (By.ID, "twotabsearchtextbox")
    search_key = (By.ID, "nav-search-submit-button")

    def search(self):
        self.driver.find_element(*HomePage.searchBox).send_keys("iPhone")
        self.driver.find_element(*HomePage.search_key).click()


