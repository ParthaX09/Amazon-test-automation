from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    number = (By.CSS_SELECTOR, "#ap_email")
    cont = (By.XPATH, "//input[@id='continue']")
    pswd = (By.XPATH, "//input[@id='ap_password']")
    submit = (By.XPATH, "//input[@id='signInSubmit']")

    def get_number(self):
        numberBox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPage.number)
        )
        numberBox.send_keys("--userId--")
        
        self.driver.find_element(*LoginPage.cont).click()

    def get_pswd(self):
        self.driver.find_element(*LoginPage.pswd).send_keys("--password--")
        self.driver.find_element(*LoginPage.submit).click()


