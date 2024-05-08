import os
import yaml
import requests

from connector import BaseConnector


class IndeedConnector(BaseConnector):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        script_name = os.path.basename(__file__).removesuffix('.py')
        config_path = os.path.join(os.environ["BASE_DIR"],script_name,"config.yaml")

        self.get_config(config_path)


    def construct_url(self):
        pass



