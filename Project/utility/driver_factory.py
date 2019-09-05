from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Project.configure.parsing import Parse
from Project.configure.parser_browser_names import ParseNames


class BrowserFactory:

    @staticmethod
    def create_browser():

        browser_name = Parse().get_json_browser_name()
        browser_names_google = ParseNames().parsed_browser_names_google()
        browser_names_mozilla = ParseNames().parsed_browser_names_mozilla()
        language = Parse().get_json_language()

        if browser_name in browser_names_mozilla:
            options = webdriver.FirefoxOptions()
            options.set_preference("intl.accept_languages", language)
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.manager.showWhenStarting", False)
            options.set_preference("browser.download.dir", r"C:\\Users\\p.minchik\\Downloads")
            options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                   "application/msword, application/csv, application/ris, text/csv, image/png, "
                                   "application/pdf, text/html, text/plain, application/zip, application/x-zip, "
                                   "application/x-zip-compressed, application/download, application/octet-stream")

            BrowserFactory.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
            BrowserFactory.driver.maximize_window()
        elif browser_name in browser_names_google:
            options = webdriver.ChromeOptions()
            preferences = {"download.default_directory": r"C:\\Users\\p.minchik\\Downloads",
                           "directory_upgrade": True,
                           "safebrowsing.enabled": True,
                           "intl.accept_languages": language}
            options.add_argument("--start-maximized")
            options.add_experimental_option("prefs", preferences)
            BrowserFactory.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        return BrowserFactory.driver
