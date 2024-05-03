import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class NavigationPage:
    def __init__(self, driver):
        self.driver = driver
        self.headerNav_community = (By.XPATH, '/html/body/div[1]/header/div[1]/div/div[8]/div[3]/a')
        self.headerNav_read = (By.XPATH, '/html/body/div[1]/header/div[1]/div/div[8]/div[4]/a')
        self.headerNav_read_coffee = (By.XPATH, '/html/body/div[1]/header/div[1]/div/div[8]/div[4]/ul/li[1]/a')

    def open_page(self, url):
        self.driver.get(url)

    def open_page_community(self):
        self.driver.find_element(*self.headerNav_community).click()

    def open_page_coffee(self):

        element = self.driver.find_element(*self.headerNav_read)

        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        time.sleep(1)

        self.driver.find_element(*self.headerNav_read_coffee).click()
        time.sleep(1)
