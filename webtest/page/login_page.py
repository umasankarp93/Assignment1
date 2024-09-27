from selenium.webdriver.common.by import By
from webtest.locators.locators import Locators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, Locators.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, Locators.password).send_keys(password)

    def select_language(self):
        self.driver.find_element(By.XPATH, Locators.lang_dd).click()
        self.driver.find_element(By.XPATH, Locators.select_lang).click()

    def click_login(self):
        self.driver.find_element(By.XPATH, Locators.login_button).click()
