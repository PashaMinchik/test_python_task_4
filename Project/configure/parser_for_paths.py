import json
import os


class ParsePaths:

    def __init__(self):
        self.json_paths = os.path.sep = os.path.join(os.path.dirname(__file__), '..', 'etc', 'paths')
        self.path_to_downloaded_file = str
        self.path_to_downloaded_directory = str

    def get_json_paths(self):
        with open(self.json_paths, 'r') as json_data:
            parsed_data_for_paths = json.load(json_data)
        return parsed_data_for_paths

    def parsed_path_file(self):
        self.path_to_downloaded_file = ParsePaths.get_json_paths(self)['path_to_downloaded_file']
        return self.path_to_downloaded_file

    def parsed_path_download_directory(self):
        self.path_to_downloaded_directory = ParsePaths.get_json_paths(self)['path_to_download_directory']
        return self.path_to_downloaded_directory
