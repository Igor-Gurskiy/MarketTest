from base.base_class import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://www.demoblaze.com/index.html"

    # Locators
    button_monitors = '//a[contains(text(), "Monitors")]'
    product = '//div[@id="tbodyid"]/div[{item_number}]//a[@class="hrefch"]'

    # Getters
    def get_button_monitors(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_monitors)))

    def get_product(self, item_number):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product.format(item_number=item_number))))

    # Actions
    def action_click_button_monitors(self):
        self.get_button_monitors().click()
        print("Click button monitors")

    def action_click_product(self, item_number):
        self.get_product(item_number).click()
        print("Click product")

   