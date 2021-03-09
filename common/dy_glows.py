# encoding:utf-8
from time import time

from common.douyu_request import dyreq
from common.logger import logger

Bags = 0
Own = 0


def get_glow():
    """
    :return: 领取结果的基本格式
    """
    # 需要先访问一次直播间才会获得道具
    into_data = "v=220120210309&did=0d945ed357b50e80ee2ee63400021501&tt={}&sign=3ca6f479a64b61d22d4c85ee28b535ac&cdn" \
                "=&rate=0&ver=Douyu_221030405&iar=1&ive=0&hevc=0".format(int(time()))
    into_room = dyreq.request("post", "/lapi/live/getH5Play/12313", data=into_data)
    glow_url = "/japi/prop/backpack/web/v1?rid=12306"
    glow_res = dyreq.request("get", glow_url)
    global Bags
    try:
        # 查询获取到的荧光棒
        assert glow_res.status_code == 200
        assert glow_res.json()['msg'] == "success"
        # 防止没有道具导致程序报错
        if glow_res.json()['data']['list']:
            global Own
            Own = glow_res.json()['data']['list'][0]['count']
            logger.info("成功获取荧光棒%s个,给你喜欢的主播进行赠送吧" % Own)
            Bags = 1
        else:
            logger.warning("当前背包中没有任何道具")
    except AssertionError:
        logger.info("领取荧光棒时发生错误")
    return glow_res


def get_own():
    """
    :return:返回全局变量,用于主程序内判断
    """
    return Own


def glow_donate(num=1, room_id=12306):
    """
    :param num: 向该房间赠送荧光棒的数量
    :param room_id: 房间号
    """
    donate_url = "/japi/prop/donate/mainsite/v1"
    DATA = "propId=268&propCount=%s&roomId=%s&bizExt={\"yzxq\":{}}" % (num, room_id)
    # 背包中含有道具才会进行赠送，否则会报错
    if Bags:
        donate_res = dyreq.request(method="post", path=donate_url, data=DATA)
        global Own
        try:
            assert donate_res.status_code == 200
            assert donate_res.json()['msg'] == "success"
            # 计算剩余荧光棒
            now_left = int(Own) - int(num)
            Own = now_left
            logger.info("向房间号%s赠送荧光棒%s个成功,当前剩余%s个" % (room_id, num, now_left))
        except AssertionError:
            if donate_res.json()['msg'] == "用户没有足够的道具":
                logger.warning("向房间号%s赠送荧光棒失败,当前背包中荧光棒数量为:%s,而设定捐赠数量为%s" % (room_id, Own, num))
            else:
                logger.warning(donate_res.json()['msg'])


if __name__ == '__main__':
    get_glow()
