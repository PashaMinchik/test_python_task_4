from Project.pages.fourth_page_my_game import Game
import os.path
from Project.configure.confpage import ConfPage


class Install(Game):
    def __init__(self, driver: object):
        super().__init__(driver)
        self.steam_install_click: str = "//a[@class='about_install_steam_link']"
        self.file_path: str = r"C:\\Users\\p.minchik\\Downloads\\SteamSetup.exe"
        self.fluent_time: ConfPage = ConfPage(driver)

    def click_install_again(self):
        self.fluent_time.get_element_with_click(self.steam_install_click)

    def check_file_and_close_page(self):
        while True:
            x = os.path.sep = os.path.isfile(self.file_path)
            print("Размер файла: ", os.path.getsize(self.file_path))
            if x:
                print("steam file is in the folder")
                break

