import os
import configparser


class ApiRequestBuilder:
    def __init__(self):
        self.config = configparser.ConfigParser()
        module_dir = os.path.dirname(__file__)
        config_file_path = os.path.join(module_dir, 'api_config.properties')
        self.config.read(config_file_path)  # Read the configuration file first

        # Access configuration values after reading the file
        self.base_url = self.config['API']['base_url']
        self.header = {
            'accept': self.config['API']['accept'],
            'Content-Type': self.config['API']['content_type']
        }

    def get_default_headers(self):
        return self.header

    def get_base_url(self):
        return self.base_url

    def get_roop_image_url(self):
        return f"{self.base_url}{self.config['API']['roop_image']}"

    def get_png_info_url(self):
        return f"{self.base_url}{self.config['API']['png_info']}"

    def get_txt_to_image_url(self):
        return f"{self.base_url}{self.config['API']['txt_to_image']}"
