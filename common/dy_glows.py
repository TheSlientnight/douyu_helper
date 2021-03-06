import requests
import os
import logging
from common.douyu_request import *

Bags = 0
logging.basicConfig(level=logging.INFO)
Own = 0


def get_glow():
    glow_url = "/japi/prop/backpack/web/v1?rid=12306"
    glow_res = dyreq.request("get", glow_url)
    global Bags
    try:
        assert glow_res.status_code == 200
        assert glow_res.json()['msg'] == "success"
        if glow_res.json()['data']['list']:
            global Own
            Own = glow_res.json()['data']['list'][0]['count']
            logging.info("成功获取荧光棒%s个,给你喜欢的主播进行赠送吧" % Own)
            Bags = 1
        else:
            logging.warning("当前背包中没有任何道具")
    except AssertionError:
        logging.info("领取荧光棒时发生错误")
    return glow_res


def get_own():
    return Own


def glow_donate(num=1, room_id=12306):
    donate_url = "/japi/prop/donate/mainsite/v1"
    DATA = "propId=268&propCount=%s&roomId=%s&bizExt={\"yzxq\":{}}" % (num, room_id)
    if Bags:
        donate_res = dyreq.request(method="post", path=donate_url, data=DATA)
        try:
            assert donate_res.status_code == 200
            assert donate_res.json()['msg'] == "success"
            now_left = int(Own) - int(num)
            logging.info("向房间号%s赠送荧光棒%s个成功,当前剩余%s个" % (room_id, num, now_left))
        except AssertionError:
            if donate_res.json()['msg'] == "用户没有足够的道具":
                logging.warning("向房间号%s赠送荧光棒失败,当前背包中荧光棒数量为:%s,而设定捐赠数量为%s" % (room_id, Own, num))
            else:
                logging.warning(donate_res.json()['msg'])


if __name__ == '__main__':
    get_glow()
