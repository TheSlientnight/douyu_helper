import configparser
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, "config")
conf_path = os.path.join(CONFIG_DIR, "mode.ini")


class Config(configparser.ConfigParser):

    def __init__(self):
        super().__init__()
        self.file = conf_path
        self.read(self.file, encoding="utf8")

    def get_mode(self):
        """
        :return:返回配置文件中选择的模式
        """
        mode = self.getint("Modechoose", "giveMode")
        return mode

    def get_conf(self):
        """
        :return:返回自选模式下设定的房间号和赠送的礼物个数
        """
        room_list = self.get("selfMode", "roomId").split(",")
        gift_list = self.get("selfMode", "giftCount").split(",")
        return gift_list, room_list


conf = Config()

if __name__ == '__main__':
    a = Config()
    b = a.get_conf()
