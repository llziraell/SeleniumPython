import time
from POM.tests.pages.search_page import SearchPage

def test_search(driver):
    search_page = SearchPage(driver)

    search_page.open_page("https://shop.tastycoffee.ru/")
    time.sleep(1)

    search_page.click_openSearch()
    time.sleep(1)

    search_page.enter_search("дрипы")
    time.sleep(2)

    assert "Searching Completed"




