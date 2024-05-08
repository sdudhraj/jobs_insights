import yaml

class BaseConnector:
    def get_config(self, config_path):
        with open(config_path, 'r') as fopen:
            prime_service = yaml.safe_load(fopen)


    def construct_url(self):
        pass
