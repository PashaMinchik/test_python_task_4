import time
from selenium.common.exceptions import NoSuchElementException
from Project.locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.action: ActionChains = ActionChains(driver)
        self.home_site = "https://store.steampowered.com/"
        self.actions_click = Locators.actions_click
        self.actions_click_en = Locators.actions_click_en
        self.move_to_games = Locators.move_to_games
        self.check_language_en = Locators.check_language_en
        self.check_language_ru = Locators.check_language_ru

    def get_home_page(self) -> object:
        self.driver.get(self.home_site)

    def click_actions(self) -> object:
        try:
            self.driver.find_element_by_xpath(self.check_language_ru)
            self.action.move_to_element(self.driver.find_element_by_xpath(self.move_to_games)).perform()
            self.driver.find_element_by_xpath(self.actions_click).click()
        except NoSuchElementException:
            try:
                self.driver.find_element_by_xpath(self.check_language_en)
                self.action.move_to_element(self.driver.find_element_by_xpath(self.move_to_games)).perform()
                self.driver.find_element_by_xpath(self.actions_click_en).click()
            except NoSuchElementException:
                pass

