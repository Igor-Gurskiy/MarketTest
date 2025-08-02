from base.base_class import Base
from utilities.driver import get_driver

def test_autorization():
    url = "https://www.demoblaze.com/index.html"
    driver = get_driver(url)
    base = Base(driver)
    username = 'tuttam'
    password = '123'
    base.login(username, password)
    base.assert_text(f'Welcome {username}', base.get_greetings().text)
    print("Test autorization passed")
    driver.quit()