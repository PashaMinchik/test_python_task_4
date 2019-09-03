import unittest
import pytest
from Project.pages.fifth_page_install import Install
from Project.pages.first_page_steam import HomePage
from Project.pages.fourth_page_my_game import Game
from Project.pages.second_page_games import GamesPage
from Project.pages.third_page_birth_time import BirthTimePage
from Project.utility.driver_singleton import BrowserSingleton


class ConfTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserSingleton.get_driver()
        cls.home_page: HomePage = HomePage(cls.driver)
        cls.games_page: GamesPage = GamesPage(cls.driver)
        cls.birth_time_page: BirthTimePage = BirthTimePage(cls.driver)
        cls.my_game_page: Game = Game(cls.driver)
        cls.download: Install = Install(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
