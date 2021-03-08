#!/usr/bin/python
# encoding:utf-8
import logging
import logging.handlers
from common.config import conf
from dirs import file_log, LOGS_DIR


class Logger:

    def __new__(cls, file_name='run.log', *args, **kwargs):
        file = file_log(LOGS_DIR)
        log = logging.getLogger()
        log_config = conf.get_conf("log")
        log.setLevel(log_config['logger_level'])
        # 设置日志格式
        log_fmt = logging.Formatter(fmt='%(asctime)s - 【%(levelname)s】: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # 实例化控制台渠道
        log_stream = logging.StreamHandler()
        log_stream.setFormatter(log_fmt)
        log_stream.setLevel(log_config['stream_level'])

        # 实例化输出文件
        log_file = logging.FileHandler(file, encoding="UTF-8")
        log_file.setFormatter(log_fmt)
        log_file.setLevel(log_config['file_level'])

        # 添加至收集器
        log.addHandler(log_stream)
        log.addHandler(log_file)
        return log


logger = Logger()

if __name__ == '__main__':
    logger.info("test")
