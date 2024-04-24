from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.openSearch_btn = (By.ID, "openSearch_h")
        self.search_text = (By.ID, "search_h")

    def open_page(self, url):
        self.driver.get(url)

    def click_openSearch(self):
        self.driver.find_element(*self.openSearch_btn).click()

    def enter_search(self, search_input):
        self.driver.find_element(*self.search_text).send_keys(search_input)
        self.driver.find_element(*self.search_text).send_keys(Keys.RETURN)


