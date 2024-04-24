from selenium.webdriver.common.by import By


class RegPage:
    def __init__(self, driver):
        self.driver = driver
        self.fullName_textbox = (By.NAME, "full_name")
        self.email_textbox = (By.XPATH, "/html/body/div[3]/div/form/div[3]/input[3]")
        self.phone_textbox = (By.XPATH, "/html/body/div[3]/div/form/div[3]/input[4]")
        self.password_textbox = (By.XPATH, "/html/body/div[3]/div/form/div[5]/input[1]")
        self.passwordConfirmation_textbox = (By.XPATH, "/html/body/div[3]/div/form/div[5]/input[2]")
        self.agree_checkbox = (By.XPATH, '/html/body/div[3]/div/form/div[5]/div[1]/label/span[1]')
        self.createAccount_btn = (By.ID, "create_account")

    def open_page(self, url):
        self.driver.get(url)

    def enter_fullName(self, fullName):
        self.driver.find_element(*self.fullName_textbox).send_keys(fullName)

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(*self.phone_textbox).send_keys(phone)

    def enter_password(self, password):
            self.driver.find_element(*self.password_textbox).send_keys(password)

    def enter_passwordConfirmation(self, passwordConfirmation):
        self.driver.find_element(*self.passwordConfirmation_textbox).send_keys(passwordConfirmation)

    def click_agree(self):
        self.driver.find_element(*self.agree_checkbox).click()
    def click_reg(self):
        self.driver.find_element(*self.createAccount_btn).click()