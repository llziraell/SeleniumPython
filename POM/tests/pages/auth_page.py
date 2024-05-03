import time

from selenium.webdriver.common.by import By

class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.authOpenBtn = (By.XPATH, "/html/body/div[1]/header/div[1]/div/div[5]/div/div[1]/button")
        self.inputEmail = (By.ID, "email")
        self.inputPass = (By.ID, "password")
        self.signInBtn = (By.ID, "sign-in")

    def open_page(self, url):
        self.driver.get(url)

    def test_auth(self):

        self.driver.find_element(*self.authOpenBtn).click()
        time.sleep(1)

        self.driver.find_element(*self.inputEmail).send_keys('email@qqq')
        time.sleep(1)

        self.driver.find_element(*self.inputPass).send_keys('12345678')
        time.sleep(1)

        self.driver.find_element(*self.signInBtn).click()
