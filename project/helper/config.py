import configparser
import os

class Config():
    __instance = None

    def __new__(cls):
        if Config.__instance is None:
            cfg_file = os.path.dirname(os.path.abspath(__file__))+'/../cfg.ini'
            config = configparser.ConfigParser()
            config.read(cfg_file)
            Config.__instance = config
        return Config.__instance

