from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver


class ConfPage:
    wait: webdriver

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, xpath):
        wait = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(By.XPATH(xpath)))
        wait.click()
        return wait
