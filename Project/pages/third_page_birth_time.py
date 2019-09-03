from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from Project.configure.parsing import Parse


class BirthTimePage:

    def __init__(self, driver):
        self.driver = driver
        self.age_choose: str = "ageYear"
        self.select = Select
        self.open_page_button_ru: str = "//span[contains (text(),'Открыть страницу')]"
        self.language: str = Parse.get_json_language
        self.open_page_button_en: str = "//span[contains (text(),'View Page')]"

    def choose_birth_time(self):
        try:
            self.select = Select(self.driver.find_element_by_id(self.age_choose))
            self.select.select_by_visible_text("1995")
            if self.language == 'ru':
                self.driver.find_element_by_xpath(self.open_page_button_ru).click()
            elif self.language == 'en':
                self.driver.find_element_by_xpath(self.open_page_button_en).click()
        except NoSuchElementException:
            try:
                if self.language == 'ru':
                    self.driver.find_element_by_xpath(self.open_page_button_ru).click()
                elif self.language == 'en':
                    self.driver.find_element_by_xpath(self.open_page_button_en).click()
            except NoSuchElementException:
                pass
