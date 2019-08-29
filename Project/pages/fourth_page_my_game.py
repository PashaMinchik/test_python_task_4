from Project.locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException


class Game:
    def __init__(self, driver: object) -> object:
        self.x = str
        self.game_info1 = str
        self.driver = driver
        self.game1_prise = Locators.game1_prise
        self.game1_discount = Locators.game1_discount
        self.game1_base_discount = Locators.game1_base_discount
        self.click_install_button = Locators.click_install_button

    def get_info_game1(self) -> object:
        self.game_info1 = self.driver.find_element_by_xpath(self.game1_discount).get_attribute("innerText")
        try:
            self.x = self.driver.find_element_by_xpath(self.game1_base_discount).get_attribute("innerText")
            self.game_info1.replace(self.x, "")
            print(self.game_info1)
        except NoSuchElementException:
            pass
        print(self.game_info1)

    def click_install(self) -> object:
        self.driver.find_element_by_xpath(self.click_install_button).click()
