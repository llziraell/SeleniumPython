import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from POM.tests.pages.navigation_page import NavigationPage

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_navigation(driver):
    navigation_page = NavigationPage(driver)

    navigation_page.open_page("https://shop.tastycoffee.ru/")
    time.sleep(1)

    navigation_page.open_page_community()
    time.sleep(1)

    navigation_page.open_page_coffee()
    time.sleep(1)

    assert "Navigation Completed"