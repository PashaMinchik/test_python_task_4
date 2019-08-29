import unittest
from Project.pages.third_page_birth_time import BirthTimePage
from Project.pages.first_page_steam import HomePage
from Project.pages.fourth_page_my_game import Game
from Project.pages.fifth_page_install import Install
from Project.pages.second_page_games import GamesPage
from Project.configure.browser_config import BrowserFactory


class TestSteam(unittest.TestCase):



    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = BrowserFactory.start_browser("chrome")
        cls.home_page: HomePage = HomePage(cls.driver)
        cls.game_page: GamesPage = GamesPage(cls.driver)
        cls.birth_time_page: BirthTimePage = BirthTimePage(cls.driver)
        cls.game: Game = Game(cls.driver)
        cls.download: Install = Install(cls.driver)
        cls.game_2 = str
        cls.game_1 = str

    def test_1(self):
        self.home_page.get_home_page()
        self.home_page.click_actions()

        self.game_page.click_top_sellers()
        self.game_page.get_max_discount()
        self.game_1 = self.game_page.get_info_game()
        self.game_page.choose_max_discount()

        self.birth_time_page.choose_birth_time()

        self.game_2 = self.game.get_info_game1()
        assert self.game_1 == self.game_2             # Проверка равенста параметром(базовая цена, цена со скидкой, размер скидки) \
                                                        # игры с 4 и 5 шага тест кейса
        self.game.click_install()

        self.download.click_install_again()
        self.download.check_file_and_close_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

