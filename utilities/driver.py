from selenium import webdriver
from selenium.webdriver import ChromeOptions

def get_driver(url):
    service = webdriver.ChromeService(
        executable_path="C:\\Users\\R2-D2\\Desktop\\megacvetTest\\chromedriver.exe"
    )
    options = ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
        },
        )
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    driver.maximize_window()
    return driver
