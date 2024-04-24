import time

from selenium.webdriver.common.by import By

class FiltrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.priceMenu = (By.XPATH, '//*[@id="form-catalog-left"]/div[1]/div[1]/div/button/div/div/div')
        self.priceMenu_select = (By.ID, 'bs-select-1-0')
        self.variant_btn = (By.XPATH, '//*[@id="form-catalog-left"]/div[3]/div[6]/a')
        self.nav_select = (By.XPATH, '//*[@id="form-catalog-top"]/div/div[4]/label')

    def open_page(self, url):
        self.driver.get(url)

    def select_priceMenu(self):
        self.driver.find_element(*self.priceMenu).click()
        time.sleep(1)
        self.driver.find_element(*self.priceMenu_select).click()

    def click_variant(self):
        self.driver.find_element(*self.variant_btn).click()
    def click_nav(self):
        self.driver.find_element(*self.nav_select).click()



