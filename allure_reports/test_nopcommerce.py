from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest


@allure.severity(allure.severity_level.NORMAL)
class TestnopCommerce:
    @allure.severity(allure.severity_level.NORMAL)
    def test_self):
        self.driver = webdriver.Chrome(r"C:\Users\welcome\Documents\Web_driver\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status = self.driver.find_element_by_xpath(
            '//img[@src="/webres_61fc6c20769f65.38023256/themes/default/images/login/logo.png"]').is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.close()
    def test_listemplot(self):
        pytest.skip('Skipping test baad me chalaunga')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome(r"C:\Users\welcome\Documents\Web_driver\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        self.driver.find_element_by_id("btnLogin").click()
        act_title = self.driver.title

        if act_title == 'OrangeHRM0':
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
