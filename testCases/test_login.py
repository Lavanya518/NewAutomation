import time
import os
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()
    def test_homePageTitle(self):
        self.logger.info("******* Test_001_Login ****** ")
        self.logger.info("********* Verifying HomePage Title*******")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login123":
            assert True
            self.driver.close()
        else:
            #self.driver.save_screenshot("\\Screenshots\\" + r"\test_homePageTitle.png")
            #os.path.join(os.path.dirname(os.path.realpath(__file__)), 'NameOfScreenShotDirectory',
                             #
            self.driver.save_screenshot(
                "C:\\Users\\LAVANYA\\PycharmProjects\\nopcommernceApp\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("*********** Home page title is failed *********")
            assert False


    def test_login_page(self):
        self.logger.info("******** Verifying Login test******")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***** Login test is Passed")
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "C:\\Users\\LAVANYA\\PycharmProjects\\nopcommernceApp\\Screenshots\\" + "testt_login_page.png")
            self.driver.close()
            self.logger.error(" ****** Lognin test is faile ")
            assert False


