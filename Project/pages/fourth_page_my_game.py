from selenium.common.exceptions import NoSuchElementException
from Project.configure.confpage import ConfPage


class Game:
    def __init__(self, driver: object):
        self.x = str
        self.game_info1 = str
        self.all_trails = []
        self.driver = driver
        self.game1_prise: str = "//div[@class='discount_final_price']"
        self.game1_discount: str = "(//div[contains(@class,'discount_pct')])[1]/.."
        self.games_discount: str = "//div[@class='discount_block game_purchase_discount']//div[contains(@class,'discount_pct')]"
        self.game1_base_discount: str = "//div[@class='bundle_base_discount']"
        self.click_install_button: str = "//a[@class='header_installsteam_btn_content']"
        self.fluent_time: ConfPage = ConfPage(driver)

    def get_info_game1(self):
        self.game_info1 = self.driver.find_element_by_xpath(self.game1_discount).get_attribute("innerText")
        try:
            self.x = self.driver.find_element_by_xpath(self.game1_base_discount).get_attribute("innerText")
            self.game_info1.replace(self.x, "")
        except NoSuchElementException:
            pass
        print("Информация об выбранной игре: " + self.game_info1)
        return self.game_info1

    def click_install(self):
        self.fluent_time.get_element_with_click(self.click_install_button)
