from builtins import input

from mysqlx import DbDoc
from selenium.webdriver.common.by import By

import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import Db_data
import time


class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()  # Logger

    def test_login_ddt(self, setup):
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        if self.driver.current_url.endswith('password'):
            self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('gloora')
            self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/form/button').click()
            self.driver.get('https://bow-wow-lab.myshopify.com/account/login')
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)



        #get data from Db_data
        query = "SELECT * FROM customers WHERE email = 'ls2170184@gmail.com'"
        self.customers_detail = Db_data.readData('bowwowlabdb', query)
        self.logger.info(self.customers_detail)


