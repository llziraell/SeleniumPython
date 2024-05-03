import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from POM.tests.pages.trash_page import TrashPage

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_trash(driver):
    trash_page = TrashPage(driver)

    trash_page.open_page("https://shop.tastycoffee.ru/")
    time.sleep(1)

    trash_page.click_addProduct()
    time.sleep(1)

    trash_page.click_openTrashPage()
    time.sleep(1)

    trash_page.click_deleteProduct()
    time.sleep(2)

    assert "Add/Remove -Trash Completed"







