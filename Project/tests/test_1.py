import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
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

    def test_1(self):
        self.home_page.get_home_page()

    def test_2(self):
        self.home_page.click_actions()

    def test_3(self):
        self.game_page.click_top_sellers()

    def test_4(self):
        self.game_page.get_max_discount()

    def test_5(self):
        self.game_page.get_info_game()

    def test_6(self):
        self.game_page.choose_max_discount()

    def test_7(self):
        self.birth_time_page.choose_birth_time()

    def test_8(self):
        self.game.get_info_game1()
        assert self.game_page, self.game
        self.game.click_install()

    def test_9(self):
        self.download.click_install_again()
        self.download.check_file_and_close_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

