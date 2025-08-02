from base.base_class import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    product_name = '//h2[@class="name"]'
    button_add_to_cart = '//a[contains(text(), "Add to cart")]'

    # Getters
    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_name))
        )

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart))
        )

    # Actions
    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()
        print("Click button add to cart")

    # Methods
    # def add_product_to_cart(self):
    #     self.click_button_add_to_cart()
    #     self.accept_alert()