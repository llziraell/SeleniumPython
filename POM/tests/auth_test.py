import time
from POM.tests.pages.auth_page import AuthPage

def test_auth(driver):
    auth_page = AuthPage(driver)

    auth_page.open_page("https://shop.tastycoffee.ru")
    time.sleep(1)

    auth_page.test_auth()
    time.sleep(2)

    assert "Authorization Completed"


# @pytest.mark.parametrize("fullName, email, phone, password", [
#     ("Sasha Sasha0", "sasha0.sasha@sasha.com", "89787471374", "sashasasha0"),
#     ("Sasha Sasha1", "sasha1.sasha@sasha.com", "89787471377", "sashasasha1"),
#     ("Sasha Sasha2", "sasha2.sasha@sasha.com", "89787471376", "sashasasha2"),
# ])

