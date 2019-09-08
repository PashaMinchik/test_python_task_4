from selenium import webdriver
from Project.utility.driver_factory import BrowserFactory


class BrowserSingleton:
    driver: webdriver = None

    @staticmethod
    def get_driver():
        if BrowserSingleton.driver is None:
            BrowserSingleton.driver = BrowserFactory.create_browser()
        return BrowserSingleton.driver

