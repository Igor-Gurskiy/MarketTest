from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Base():
    def __init__(self, driver):
        self.driver = driver

    # Locators
    button_form_login = '//a[@id="login2"]'
    input_username = '//input[@id="loginusername"]'
    input_password = '//input[@id="loginpassword"]'
    button_login = '//button[contains(text(), "Log in")]'

    button_cart = '//a[@id="cartur"]'

    greetings = '//a[@id="nameofuser"]'

     # Getters
    def get_button_form_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_form_login)))

    def get_input_username(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_username)))

    def get_input_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))
    
    def get_greetings(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.greetings)))
    
    # Actions
    def action_click_button_form_login(self):
        self.get_button_form_login().click()
        print("Click button form login")

    def action_input_username(self, username):
        self.get_input_username().send_keys(username)
        print("Input username")

    def action_input_password(self, password):
        self.get_input_password().send_keys(password)
        print("Input password")

    def action_click_button_login(self):
        self.get_button_login().click()
        print("Click button login")
    
    def action_click_button_cart(self):
        self.get_button_cart().click()
        print("Click button cart")

    def accept_alert(self):
        self.driver.switch_to.alert.accept()
        
    # Methods
    def login(self, username, password):
        self.action_click_button_form_login()
        self.action_input_username(username)
        self.action_input_password(password)
        self.action_click_button_login()

    def assert_text(self, awaited_text, result_text):
        assert awaited_text == result_text