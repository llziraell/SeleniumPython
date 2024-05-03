import time
from POM.tests.pages.reg_page import RegPage


# @pytest.mark.parametrize("fullName, email, phone, password", [
#     ("Sasha Sasha0", "sasha0.sasha@sasha.com", "89787471374", "sashasasha0"),
#     ("Sasha Sasha1", "sasha1.sasha@sasha.com", "89787471377", "sashasasha1"),
#     ("Sasha Sasha2", "sasha2.sasha@sasha.com", "89787471376", "sashasasha2"),
# ])

def test_reg(driver):
    reg_page = RegPage(driver)

    reg_page.open_page("https://shop.tastycoffee.ru/create-account")
    time.sleep(1)

    reg_page.enter_fullName("Sasha Sasha0")
    time.sleep(1)

    reg_page.enter_email("sasha9.sasha@sasha.com")
    time.sleep(1)

    reg_page.enter_phone("88009456837")
    time.sleep(1)

    reg_page.enter_password("sashasasha0")
    time.sleep(1)

    reg_page.enter_passwordConfirmation("sashasasha0")
    time.sleep(1)

    # reg_page.click_agree()
    # time.sleep(1)

    reg_page.click_reg()
    time.sleep(1)

    assert "Authorisation Completed"




