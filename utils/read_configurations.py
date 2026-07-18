import configparser
import os
from configparser import ConfigParser


def read_configuration(category, key):
    config = configparser.ConfigParser()
    # Get the absolute path to the directory containing this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.ini")

    config.read(config_path)
    return config.get(category, key)
