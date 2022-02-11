import pytest

from selenium import webdriver

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********************* Test_001_Login*****8**************")
        self.logger.info("**********Verifying Home Page Title ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************ Home page title test is passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********** Home Page Failed ************")
            assert False
    @pytest.mark.sanity
    @pytest.mark.regression

    def test_login(self, setup):
        self.logger.info("****************Verifying the login test**********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        # self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            # self.logger.error("************LOGIN TEST FAILED*********************")
            assert False
