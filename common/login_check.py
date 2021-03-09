# encoding:utf-8
from common.douyu_request import dyreq
from common.logger import logger

Is_login = 0
login_url = "/lapi/member/api/getInfo"


def is_login():
    """
    :return:返回登陆结果,用于主程序判断
    """
    global Is_login
    login = dyreq.request("get", login_url).json()['msg']['info']
    if login:
        Is_login = 1
        user_name = login['nn']
        logger.info("Cookie有效,登陆成功")
        logger.info("用户名称:{}".format(user_name))
    else:
        logger.warning("登陆失败,请检查Cookie有效性")
    return Is_login


if __name__ == '__main__':
    is_login()
