from common.dy_glows import *
from common.login_check import *
from common.mode_choose import *
from common.dy_badge import *
import logging
import math

logging.basicConfig(level=logging.INFO)


def run():
    logging.info("------登录检查开始------")
    login_res = is_login()
    logging.info("------登录检查结束------")
    mode = conf.get_mode()
    if login_res:
        logging.info("------背包检查开始------")
        get_glow()
        try:
            glow_nums = get_own()
            assert glow_nums != 0
            logging.info("------背包检查结束------")
            if mode == 1:
                logging.info("当前选择模式为:自选模式")
                nums = conf.get_conf()[0]
                room_list = conf.get_conf()[1]
                logging.info("------开始捐赠荧光棒------")
                for i in range(len(nums)):
                    glow_donate(nums[i], room_list[i])
                logging.info("------荧光棒捐赠结束------")
                get_need_exp()
            elif mode == 0:
                logging.info("当前选择模式为:平均分配模式")
                room_list = get_room_list()
                every_give = math.ceil(glow_nums / len(b))
                left = glow_nums - every_give
                logging.info("------开始捐赠荧光棒------")
                for room in room_list:
                    if room == room_list[-1]:
                        glow_donate(left, room)
                    else:
                        glow_donate(every_give, room)
                logging.info("------荧光棒捐赠结束------")
                get_need_exp()
            else:
                logging.warning("配置错误,没有这种选项,请修改配置并重新执行")
        except Exception as e:
            logging.warning("背包中没有荧光棒,无法执行赠送,任务即将结束")
            print(e)
    else:
        logging.warning("未登录状态无法进行后续操作,任务已结束")


if __name__ == '__main__':
    run()
