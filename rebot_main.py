


import rebot_config

from myqq import send

import json

import urllib

import rebot_one     

import re

import OUYE          #欧意

def size_num(find_):
    find_filter = filter(str.isdigit, find_)
    find_list = list(find_filter)       # ['2', '0', '1', '9', '0', '9', '0', '4', '1', '1', '0', '0']
    find_str = "".join(find_list)       # 转为str    201909041100
    if bool(re.search(r'\d', find_str)) :
        find_int = int(find_str)            # 转为int    201909041100
        return find_int
    else :
        return 0;

def rebot_menu(机器人QQ,群号):

    while 1 :

        get = send.news(rebot_config.Callback_add, int(rebot_config.Callback_port))

        # 运行

        get_msg = get.run()

        get_msg = send.tool.python_to_json(get_msg)

        MQ_type = json.loads(get_msg)["MQ_type"]   # 类型

        if MQ_type == 2 :

            MQ_fromQQ = json.loads(get_msg)["MQ_fromQQ"] # 消息来自QQ

            MQ_msg = urllib.parse.unquote(json.loads(get_msg)["MQ_msg"])        # 消息内容

            if MQ_msg == "菜单":

                内容 = "==欢迎使用[Face]欧耶菜单==\n   交易高手  |  人气之星   \n   我的订阅  |     "

                rebot_one.Rebot_SendMsg(机器人QQ,群号,内容)

            elif ("交易高手" in MQ_msg ):

                if MQ_msg == "交易高手" :

                    内容 = "请在 ‘交易高手’ 后面添加数字\n例如： 交易高手10 表示查询前10名\n数字范围：1~20"

                    rebot_one.Rebot_SendMsg(机器人QQ,群号,内容)

                if size_num(MQ_msg) != 0:

                    if 0<size_num(MQ_msg)<20 :

                        内容 = OUYE.Trading_masters(size_num(MQ_msg))

                        rebot_one.Rebot_SendMsg(机器人QQ,群号,内容)

            elif ("人气之星" in MQ_msg and 0<size_num(MQ_msg)<20 ):

                if MQ_msg == "人气之星" :
                        
                    内容 = "请在 ‘人气之星’ 后面添加数字\n例如： 人气之星10 表示查询前10名\n数字范围：1~20"

                    rebot_one.Rebot_SendMsg(机器人QQ,群号,内容)

                if size_num(MQ_msg) != 0:
    
                    if 0<size_num(MQ_msg)<20 :

                        内容 = OUYE.popular_star(size_num(MQ_msg))

                        rebot_one.Rebot_SendMsg(机器人QQ,群号,内容)

            elif MQ_msg == "我的订阅":

                内容 = ("我的订阅")

                rebot_one.Rebot_SendMsg(机器人QQ,群号,内容)

    





