# encoding:utf-8
import requests
from common.dirs import LOGS_DIR
from common.logger import logger

log_file = os.path.join(LOGS_DIR, "daily.log")


def log_reader():
    with open(log_file, 'r', encoding="UTF-8") as lg:
        logs = lg.readlines()
        logs_str = ''.join(logs)
    return logs_str


def send_message(send_key) -> None:
    logger.info("------执行server酱推送------")
    url = "https://sctapi.ftqq.com/{}.send".format(send_key)
    data = {
        "title": u"DouYu-Helper执行结果",
        "desp": log_reader()
    }
    if data['desp']:
        try:
            send_log = requests.post(url, data=data)
            logger.info("------推送成功------")
        except Exception as e:
            logger.error(e)
    else:
        data = {
            "title": u"DouYu-Helper执行结果",
            "desp": "执行出现问题,日志为空"
        }
        send_log = requests.post(url)
    return send_log.status_code


if __name__ == '__main__':
    send_message()
