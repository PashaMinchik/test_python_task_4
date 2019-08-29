from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


class BirthTimePage:

    def __init__(self, driver):
        self.driver = driver
        self.age_choose: str = "ageYear"
        self.select = Select
        self.open_page_button: str = "//span[contains (text(),'Открыть страницу')]"

    def choose_birth_time(self):
        try:
            self.select = Select(self.driver.find_element_by_id(self.age_choose))
            self.select.select_by_visible_text("1995")
            self.driver.find_element_by_xpath(self.open_page_button).click()
        except NoSuchElementException:
            try:
                self.driver.find_element_by_xpath(self.open_page_button).click()
            except NoSuchElementException:
                pass
