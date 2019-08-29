
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

    def click_top_sellers(self) -> object:
        self.driver.find_element_by_xpath(self.top_sellers).click()

    def get_max_discount(self) -> object:
        print(self.driver.find_elements_by_xpath(self.game_discount))
        for link in self.driver.find_elements_by_xpath(self.game_discount):
            self.all_trails.append(link.get_attribute("innerText"))

        print(self.all_trails)
        self.max_discount = max(self.all_trails)
        print("Максимальная скидка: " + self.max_discount)

    def get_info_game(self) -> object:
        self.game_info = self.driver.find_element_by_xpath(self.game_final_prise % self.max_discount).get_attribute("innerText")
        print("Информация об игре из списка: " + self.game_info)
        return self.game_info

    def choose_max_discount(self):
        self.driver.find_element_by_xpath(self.click_max_discount % self.max_discount).click()
