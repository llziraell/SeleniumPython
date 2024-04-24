import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from POM.tests.pages.search_page import SearchPage

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_reg(driver):
    search_page = SearchPage(driver)

    search_page.open_page("https://shop.tastycoffee.ru/")
    time.sleep(1)

    search_page.click_openSearch()
    time.sleep(1)

    search_page.enter_search("дрипы")
    time.sleep(2)

    assert "Searching Completed"




