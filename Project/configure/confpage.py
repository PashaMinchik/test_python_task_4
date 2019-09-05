from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver
from Project.configure.parsing import Parse


class ConfPage:
    wait: webdriver

    def __init__(self, driver):
        self.driver = driver
        self.timeout = Parse().get_json_timeout()

    def get_element(self, xpath):
        WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable(By.XPATH, xpath))
