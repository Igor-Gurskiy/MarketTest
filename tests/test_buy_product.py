from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utilities.driver import get_driver
import time

def test_buy_product():
    url = "https://www.demoblaze.com/index.html"
    driver = get_driver(url)
    home = HomePage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)
    home.action_click_button_monitors()
    time.sleep(2)
    home.action_click_product(1)
    product.click_button_add_to_cart()
    time.sleep(2)
    product.accept_alert()
    product.action_click_button_cart()
    cart.place_order("Ivan", "Russia", "Moscow", "123456789", "12", "2022")
    print("Test buy product passed")
    driver.quit()