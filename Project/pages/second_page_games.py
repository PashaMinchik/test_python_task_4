from Project.configure.confpage import ConfPage


class GamesPage:

    def __init__(self, driver):
        self.driver = driver
        self.top_sellers: str = "//div[@id='tab_select_TopSellers']"
        self.game_discount: str = "//div[@id='TopSellersRows']//div[@class='discount_pct' and contains(text(),'%')]"
        self.game_final_prise: str = "//div[@id='TopSellersRows']//div[@class='discount_pct' and contains(text(),'%s')]/.."
        self.all_trails = []
        self.game_info = str
        self.max_discount = []
        self.click_max_discount: str = "//div[@id='TopSellersRows']//div[@class='discount_pct' and contains(text(),'%s')]"
        self.fluent_time: ConfPage = ConfPage(driver)

    def click_top_sellers(self):
        self.fluent_time.get_element_with_click(self.top_sellers)

    def get_max_discount(self):
        for link in self.driver.find_elements_by_xpath(self.game_discount):
            self.all_trails.append(link.get_attribute("innerText"))

        print("Список игр со скидками: ", self.all_trails)
        self.max_discount = max(self.all_trails)
        print("Максимальная скидка: " + self.max_discount)

    def get_info_game(self) -> str:
        self.game_info = self.driver.find_element_by_xpath(self.game_final_prise % self.max_discount).get_attribute("innerText")
        print("Информация об игре из списка: " + self.game_info)
        return self.game_info

    def choose_max_discount(self):
        self.fluent_time.get_element_with_click(self.click_max_discount % self.max_discount)
