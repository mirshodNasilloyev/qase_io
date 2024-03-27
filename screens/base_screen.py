from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as wdw


class BaseScreen:

    def __init__(self, driver):
        self.driver = driver

    def click(self, elem):
        wdw(self.driver, timeout=20).until(ec.visibility_of_element_located((By.XPATH, elem))).click()

    def enter_data(self, elem, data):
        wdw(self.driver, timeout=20).until(ec.visibility_of_element_located((By.XPATH, elem))).send_keys(data)

    def clear_input_field(self, elem):
        wdw(self.driver, timeout=20).until(ec.visibility_of_element_located((By.XPATH, elem))).clear()

    def is_element_exist(self, elem):
        if wdw(self.driver, timeout=20).until(ec.visibility_of_element_located((By.XPATH, elem))).is_displayed():
            return True
        else:
            return False

