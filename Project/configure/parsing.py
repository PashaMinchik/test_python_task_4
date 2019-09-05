import json
import os


class Parse:

    def __init__(self):
        self.json_configuration = os.path.sep = os.path.join(os.path.dirname(__file__), '..', 'etc', 'configuration')
        self.browser_name = str
        self.browser_names = str
        self.language = str
        self.url = str
        self.timeout = str

    def get_json_configuration(self):
        with open(self.json_configuration, 'r') as json_data:
            parsed_data = json.load(json_data)
        return parsed_data

    def get_json_browser_name(self):
        self.browser_name = Parse.get_json_configuration(self)['browser_name']
        return self.browser_name

    def get_json_language(self):
        self.language = Parse.get_json_configuration(self)['language']
        return self.language

    def get_json_url(self):
        self.url = Parse.get_json_configuration(self)['url']
        return self.url

    def get_json_timeout(self):
        self.timeout = Parse.get_json_configuration(self)['timeout']
        return self.timeout
