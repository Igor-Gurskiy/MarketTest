from base.base_class import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_place_order = '//button[contains(text(), "Place Order")]'

    input_name = '//input[@id="name"]'
    input_country = '//input[@id="country"]'
    input_city = '//input[@id="city"]'
    input_card = '//input[@id="card"]'
    input_month = '//input[@id="month"]'
    input_year = '//input[@id="year"]'
    button_purchase = '//button[contains(text(), "Purchase")]'

    confirm_title = '//h2[contains(., "Thank you for your purchase")]'
    confirm_button = '//button[contains(text(), "OK")]'
    # Getters
    def get_button_place_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_place_order)))
    
    def get_input_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_name)))
    
    def get_input_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_country)))
    
    def get_input_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_city)))
    
    def get_input_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_card)))
    
    def get_input_month(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_month)))
    
    def get_input_year(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_year)))
    
    def get_button_purchase(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_purchase)))
    
    def get_confirm_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_title)))
    
    def get_confirm_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_button)))
    
    # Actions
    def action_click_button_place_order(self):
        self.get_button_place_order().click()
        print("Click button place order")
    
    def action_input_name(self, name):
        self.get_input_name().send_keys(name)
        print("Input name")
    
    def action_input_country(self, country):
        self.get_input_country().send_keys(country)
        print("Input country")
    
    def action_input_city(self, city):
        self.get_input_city().send_keys(city)
        print("Input city")
    
    def action_input_card(self, card):
        self.get_input_card().send_keys(card)
        print("Input card")
    
    def action_input_month(self, month):
        self.get_input_month().send_keys(month)
        print("Input month")
    
    def action_input_year(self, year):
        self.get_input_year().send_keys(year)
        print("Input year")
    
    def action_click_button_purchase(self):
        self.get_button_purchase().click()
        print("Click button purchase")

    def action_click_confirm_button(self):
        self.get_confirm_button().click()
        print("Click confirm button")

    # Methods
    def place_order(self, name, country, city, card, month, year):
        self.action_click_button_place_order()
        self.action_input_name(name)
        self.action_input_country(country)
        self.action_input_city(city)
        self.action_input_card(card)
        self.action_input_month(month)
        self.action_input_year(year)
        self.action_click_button_purchase()
        self.assert_text("Thank you for your purchase!", self.get_confirm_title().text)
        self.action_click_confirm_button()

    