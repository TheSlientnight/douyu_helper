# encoding:utf-8
from common.douyu_request import dyreq
from common.logger import logger
from lxml import etree
import re


def get_badge():
    """
    :return: 获取具有粉丝牌的房间号、当前经验、升级所需经验、升级还需要的经验
    """
    badges_url = "/member/cp/getFansBadgeList"
    badges = dyreq.request("get", badges_url)
    html = etree.HTML(badges.text, etree.HTMLParser())
    num = len(html.xpath('//*[@id="wrap"]/div/div[2]/div[2]/div[3]/table/tbody/tr'))
    re_now = r'(?<= )\d.*\d(?=\/\d)'
    re_up = r'(?<=\/)\d.*\d'
    badge_dict = {}
    exp_list = []
    for path in range(num):
        path += 1
        room_id = html.xpath('//*[@id="wrap"]/div/div[2]/div[2]/div[3]/table/tbody/tr[%s]/@data-fans-room' % path)[
            0]
        anchor = html.xpath('//*[@id="wrap"]/div/div[2]/div[2]/div[3]/table/tbody/tr[%s]/td[2]/a/text()' % path)[0]
        exp = html.xpath('//*[@id="wrap"]/div/div[2]/div[2]/div[3]/table/tbody/tr[%s]/td[3]/text()' % path)[0]
        exp_now = float(re.findall(re_now, exp)[0])
        up_grade = float(re.findall(re_up, exp)[0])
        exp_need = round((up_grade - exp_now), 1)
        exp_list.append(exp_need)
        badge_dict[room_id] = anchor
    return badge_dict, exp_list


def get_room_list():
    """
    :return:通过数组方式返回房间号
    """
    room_list = []
    for room in get_badge()[0]:
        room_list.append(room)
    return room_list


def get_need_exp():
    """
    :return:通过数组方式返回升级所需经验
    """
    for i in range(len(get_badge()[1])):
        logger.info("房间号%s升级还需%s点经验" % (get_room_list()[i], get_badge()[1][i]))


if __name__ == '__main__':
    a = get_room_list()
    get_need_exp()
