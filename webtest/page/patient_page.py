from selenium.webdriver.common.by import By
from webtest.locators.locators import Locators
from selenium.webdriver import ActionChains

class PatientPage:
    def __init__(self, driver):
        self.driver = driver

    def click_patient(self):
        self.driver.find_element(By.XPATH, Locators.patient_button).click()

    def click_new_search(self):
        patient_new_search = self.driver.find_element(By.XPATH, Locators.patient_new_search)
        ActionChains(self.driver).move_to_element(patient_new_search).click().perform()

    def add_patient_details(self, first_name, last_name):
        self.driver.find_element(By.XPATH, Locators.fst_name).send_keys(first_name)
        self.driver.find_element(By.XPATH, Locators.lst_name).send_keys(last_name)

    def select_dob(self):
        self.driver.find_element(By.XPATH, Locators.DOB_field).click()
        self.driver.find_element(By.XPATH, Locators.DOB_today).click()

    def select_gender(self):
        self.driver.find_element(By.XPATH, Locators.gender_dropdown).click()
        self.driver.find_element(By.XPATH, Locators.gender_selection).click()

    def create_new_patient(self):
        self.driver.find_element(By.XPATH, Locators.create_button).click()
