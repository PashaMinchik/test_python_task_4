from Project.configure.conftest import ConfTest
import time


class TestSteam(ConfTest):

    def test_1(self):
        self.home_page.get_home_page()
        self.home_page.click_action()

        self.games_page.click_top_sellers()
        self.games_page.get_max_discount()
        game_1: str = self.games_page.get_info_game()
        self.games_page.choose_max_discount()

        self.birth_time_page.choose_birth_time()

        game_2: str = self.my_game_page.get_info_game1()
        assert game_2 == game_1  # Проверка равенста параметром(базовая цена, цена со скидкой, размер скидки) \
                                                        # игры с 4 и 5 шага тест кейса
        self.my_game_page.click_install()

        self.download.click_install_again()
        self.download.check_file_and_close_page()


