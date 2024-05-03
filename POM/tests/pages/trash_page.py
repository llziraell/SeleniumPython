import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class TrashPage:
    def __init__(self, driver):
        self.driver = driver
        self.addProduct_btn = (By.XPATH, "/html/body/div[3]/div[2]/div/div/div[1]/div/div[1]/form/div[6]/div/div[3]/a")
        self.openTrashPage_btn = (By.XPATH, "/html/body/div[7]/div/a")
        self.deleteProduct_btn = (By.XPATH, '//*[@id="basket-products"]/div[1]/div[1]/form/div/div[4]/a')

    def open_page(self, url):
        self.driver.get(url)

    def click_addProduct(self):
        self.driver.find_element(*self.addProduct_btn).click()

    def click_openTrashPage(self):
        self.driver.find_element(*self.openTrashPage_btn).click()

    def click_deleteProduct(self):
        self.driver.find_element(*self.deleteProduct_btn).click()

