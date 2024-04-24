import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from POM.tests.pages.filtration_page import FiltrationPage

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
    filtration_page = FiltrationPage(driver)

    filtration_page.open_page("https://shop.tastycoffee.ru/coffee")
    time.sleep(1)

    filtration_page.select_priceMenu()
    time.sleep(1)

    filtration_page.click_variant()
    time.sleep(1)

    filtration_page.click_nav()
    time.sleep(2)

    assert "Filtration Completed"




