import yaml
import os


def genConfig():
    with open(os.getcwd() + '/configuration/config.yaml') as file:
        return yaml.load(file, Loader=yaml.FullLoader)

Config = genConfig()