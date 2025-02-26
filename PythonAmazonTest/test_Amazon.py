import time

import pytest

from pageObject.BuyPage import BuyPage
from pageObject.HomePage import HomePage
from pageObject.LoginPage import LoginPage


class TestAmazon:

    @pytest.mark.usefixtures("setup")
    def test_Amazon(self):

        homePage = HomePage(self.driver)
        homePage.search()

        buyPage = BuyPage(self.driver)
        buyPage.sel()
        time.sleep(5)
        buyPage.buyNow()

        loginPage = LoginPage(self.driver)
        loginPage.get_number()
        loginPage.get_pswd()


        time.sleep(10)




