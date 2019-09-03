from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager
from Project.configure.parsing import Parse


class BrowserFactory:

    @staticmethod
    def create_browser():
        browser_name = Parse().get_json_browser_name()
        language = Parse().get_json_language()
        if browser_name == "firefox" or browser_name == "Firefox" or browser_name == "ff":
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
        elif browser_name == "chrome" or browser_name == "Chrome":
            options = webdriver.ChromeOptions()
            preferences = {"download.default_directory": r"C:\\Users\\p.minchik\\Downloads",
                           "directory_upgrade": True,
                           "safebrowsing.enabled": True,
                           "intl.accept_languages": language}
            options.add_experimental_option("prefs", preferences)
            BrowserFactory.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        return BrowserFactory.driver