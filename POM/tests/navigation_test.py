import time
from POM.tests.pages.navigation_page import NavigationPage
def test_navigation(driver):
    navigation_page = NavigationPage(driver)

    navigation_page.open_page("https://shop.tastycoffee.ru/")
    time.sleep(1)

    navigation_page.open_page_community()
    time.sleep(1)

    navigation_page.open_page_coffee()
    time.sleep(1)

    assert "Navigation Completed"