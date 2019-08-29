from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.action: ActionChains = ActionChains(driver)
        self.home_site = "https://store.steampowered.com/"
        self.actions_click: str = "//a[contains (text(),'Экшен')][@class='popup_menu_item']"
        self.move_to_games: str = "//a[@class='pulldown_desktop'][contains (text(),'Игры')]"

    def get_home_page(self):
        self.driver.get(self.home_site)

    def click_actions(self):
        self.action.move_to_element(self.driver.find_element_by_xpath(self.move_to_games)).perform()
        self.driver.find_element_by_xpath(self.actions_click).click()
       #try:
       #    self.driver.find_element_by_xpath(self.check_language_ru)
       #    self.action.move_to_element(self.driver.find_element_by_xpath(self.move_to_games)).perform()
       #    self.driver.find_element_by_xpath(self.actions_click).click()
       #except NoSuchElementException:
       #    try:
       #        self.driver.find_element_by_xpath(self.check_language_en)
       #        self.action.move_to_element(self.driver.find_element_by_xpath(self.move_to_games)).perform()
       #        self.driver.find_element_by_xpath(self.actions_click_en).click()
       #    except NoSuchElementException:
       #        pass

