# encoding:utf-8
import configparser
from common.dirs import *
import os

conf_path = os.path.join(CONFIG_DIR, "config.ini")


class Config(configparser.ConfigParser):

    def __init__(self):
        super().__init__()
        self.file = conf_path
        self.read(self.file, encoding="utf8")

    def get_conf(self, section, *options) -> dict:
        op_list = []
        if options:
            for option in options:
                res = self.get(section, option)
                op_list.append(res)
            options_list = dict(zip(options, op_list))
        else:
            options_list = dict(self.items(section))
        return options_list

    def get_conf_list(self, section, option):
        return Config.get_conf(self, section, option)[option].split(",")


conf = Config()

if __name__ == '__main__':
    a = Config()
    b = a.get_conf("Modechoose")['givemode']
    print(b)
