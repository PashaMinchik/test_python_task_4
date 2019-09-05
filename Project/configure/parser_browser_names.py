import json
import os


class ParseNames:

    def __init__(self):
        self.json_browser_names = os.path.sep = os.path.join(os.path.dirname(__file__), '..', 'etc', 'browser_names')
        self.browser_names_google = str
        self.browser_names_mozilla = str

    def get_json_browser_names(self):
        with open(self.json_browser_names, 'r') as json_data:
            parsed_data_for_name_browser = json.load(json_data)
        return parsed_data_for_name_browser

    def parsed_browser_names_google(self):
        self.browser_names_google = ParseNames.get_json_browser_names(self)['google']
        return self.browser_names_google

    def parsed_browser_names_mozilla(self):
        self.browser_names_mozilla = ParseNames.get_json_browser_names(self)['mozilla']
        return self.browser_names_mozilla
