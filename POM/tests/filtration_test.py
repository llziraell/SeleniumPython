import time
from POM.tests.pages.filtration_page import FiltrationPage

def test_filtration(driver):
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




