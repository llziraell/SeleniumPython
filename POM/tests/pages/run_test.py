from selenium import webdriver

from POM.tests.reg_test import test_reg
from POM.tests.auth_test import test_auth
from POM.tests.search_test import test_search
from POM.tests.navigation_test import test_navigation
from POM.tests.filtration_test import test_filtration
from POM.tests.trash_test import test_trash

def run_all_tests():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    test_reg(driver)
    test_auth(driver)
    test_search(driver)
    test_navigation(driver)
    test_filtration(driver)
    test_trash(driver)

    driver.quit()

if __name__ == "__main__":
    run_all_tests()
