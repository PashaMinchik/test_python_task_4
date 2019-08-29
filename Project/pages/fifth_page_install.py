from Project.locators.locators import Locators
from Project.pages.fourth_page_my_game import Game
import os.path


class Install(Game):
    def __init__(self, driver: object):
        super().__init__(driver)
        self.stem_install_click = Locators.stem_install_click
        self.file_path = str

    def click_install_again(self):
        self.driver.find_element_by_xpath(self.stem_install_click).click()

    def check_file_and_close_page(self):
        self.file_path = r"C:\Users\p.minchik\Downloads\SteamSetup.exe"
        while True:
            x = os.path.isfile(self.file_path)
            if x:
                print("file there")
                break

