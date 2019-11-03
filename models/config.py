import json, os, traceback

class Config:
    """
    This class is responsible for interpreting the config.json file to give the application
    direction
    """
    def __init__(self, config_json_path: str):
        self._config_path = config_json_path
        self._config_dict = {}

    def load_config_file(self):
        """
        This function will load the config params in config.json
        :return: config_dict that has all config params
        """
        try:
            with open(self._config_path, 'r+') as json_file:
                self._config_dict = json.load(json_file)
        except Exception as e:
            print(f"There was an error in load_config_file() - {e}")
            traceback.print_stack()
            os._exit(1)

    def get_config_params(self):
        """
        This function will return the config params
        :return:
        """
        return self._config_dict
