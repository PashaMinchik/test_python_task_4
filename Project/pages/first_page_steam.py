from selenium.webdriver.common.action_chains import ActionChains

from Project.configure.confpage import ConfPage
from Project.configure.parsing import Parse


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.action: ActionChains = ActionChains(driver)
        self.home_site: str = Parse().get_json_url()
        self.actions_click_ru: str = "//a[contains (text(),'Экшен')][@class='popup_menu_item']"
        self.move_to_games_ru: str = "//a[@class='pulldown_desktop'][contains (text(),'Игры')]"
        self.language: str = Parse().get_json_language()
        self.actions_click_en: str = "//a[contains (text(),'Action')][@class='popup_menu_item']"
        self.move_to_games_en: str = "//a[@class='pulldown_desktop'][contains (text(),'Games')]"
        self.fluent_time: ConfPage = ConfPage(driver)

    def get_home_page(self):
        self.driver.get(self.home_site)

    def click_action(self):
        if self.language == "ru":
            self.action.move_to_element(self.driver.find_element_by_xpath(self.move_to_games_ru)).perform()
            #self.fluent_time.get_element(self.actions_click_ru)
            #self.fluent_time.fluent_wait(self.actions_click_ru).click()
            self.driver.find_element_by_xpath(self.actions_click_ru).click()
        elif self.language == "en":
            self.action.move_to_element(self.driver.find_element_by_xpath(self.move_to_games_en)).perform()
            self.driver.find_element_by_xpath(self.actions_click_en).click()
