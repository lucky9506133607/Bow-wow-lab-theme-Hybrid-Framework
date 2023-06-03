import time

from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_xpath = "//*[@id='CustomerEmail']"
    textbox_password_id = "CustomerPassword"
    button_login_xpath = "//*[@id='customer_login']/button"
    link_logout_linktext = "//*[@id='shopify-section-template--16097491189926__main']/div/div[1]/a"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()


