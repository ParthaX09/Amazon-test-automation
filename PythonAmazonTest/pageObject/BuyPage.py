from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BuyPage:
    def __init__(self, driver):
        self.driver = driver

    select = (By.XPATH, "//h2[@aria-label='iPhone 16 128 GB: 5G Mobile Phone with Camera Control, A18 Chip and a Big Boost in Battery Life. Works with AirPods; Pink']//span[contains(text(),'iPhone 16 128 GB: 5G Mobile Phone with Camera Cont')]")
    byNowbtn = (By.ID, "buy-now-button")

    def sel(self):
        self.driver.find_element(*BuyPage.select).click()

    def buyNow(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        buy_now_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(BuyPage.byNowbtn)
        )
        buy_now_button.click()

    def check(self):
        pass


