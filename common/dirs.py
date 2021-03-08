#!/usr/bin/python
# encoding:utf-8
import os
import time

# 根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 设置地址
CONFIG_DIR = os.path.join(BASE_DIR, "config")
# 日志地址
LOGS_DIR = os.path.join(BASE_DIR, "log")


def file_log(filepath):
    dir = LOGS_DIR
    if not os.path.exists(dir):
        os.makedirs(dir)
    return os.path.join(dir, "{}.log".format(time.strftime('%Y-%m-%d')))


if __name__ == '__main__':
    print(LOGS_DIR)
