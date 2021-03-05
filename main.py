import requests
import os
import logging


logging.basicConfig(level=logging.INFO)
GLOW_URL = "https://www.douyu.com/japi/prop/backpack/web/v1?rid=12306"
HEADER = {
    "Content-Type": "application/x-www-form-urlencoded",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81",
    "referer": "https://www.douyu.com/topic/s11cb_0?rid=12306",
    "Cookie": os.environ["COOKIES"]
}
DONATE_URL = "https://www.douyu.com/japi/prop/donate/mainsite/v1"


def get_glow():
    glow_res = requests.get(GLOW_URL, headers=HEADER)
    try:
        assert glow_res.status_code == 200
        assert glow_res.json()['msg'] == "success"
        own = glow_res.json()['data']['list'][0]['count']
        logging.info("成功获取荧光棒%d个,给你喜欢的主播进行赠送吧" % own)
    except AssertionError:
        logging.info("领取荧光棒时发生错误")
    return glow_res


def glow_donate(num=1, room_id=12306):
    DATA = "propId=268&propCount=%d&roomId=%d&bizExt={\"yzxq\":{}}" % (num, room_id)
    donate_res = requests.post(url=DONATE_URL, headers=HEADER, data=DATA)
    try:
        assert donate_res.status_code == 200
        assert donate_res.json()['msg'] == "success"
        logging.info("已向房间号%d赠送荧光棒%d个" % (room_id, num))
    except AssertionError:
        if donate_res.json()['msg'] == "用户没有足够的道具":
            own = get_glow().json()['data']['list'][0]['count']
            logging.error("赠送荧光棒失败,当前背包中荧光棒数量为:%d" % own)
        else:
            logging.error(donate_res.json()['msg'])


if __name__ == '__main__':
    get_glow()
    glow_donate(74, 12306)
    glow_donate(1,99999)
