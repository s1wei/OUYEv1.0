


# from encodings import utf_8

# from webbrowser import Elinks

# # 请求
# from email import header

# 导入库
# import myqq

from myqq import send

import rebot_config

# 新建机器人
bot = send.Send(rebot_config.listen_add, rebot_config.Token_)

# API函数名称


'''
# 消息回调设置
get = send.news('127.0.0.1', 5000)
# 运行
get_msg = get.run()

get_msg = send.tool.python_to_json(get_msg)

'''
#机器人使用声明 （通过日志发送）
def Rebot_statement():
    Api_OutPut = "Api_OutPut"
    c1 = {"c1": "插件作者小河灵 QQ：771111550   版本v1.0.0  更新日期:2022.5.10"}
    bot.div(Api_OutPut, c1)
    c2 = {"c1": "本插件仅用于学习交流参考使用，禁止用于违法违规用途"}
    bot.div(Api_OutPut, c2)
    c3 = {"c1": "使用本插件代表使用者同意自行承担使用插件的一切后果"}
    bot.div(Api_OutPut, c3)
# Rebot_statement()


def Rebot_SendMsg(机器人QQ,群号,内容):
    Api_OutPut = "Api_SendMsg"
    P = {"c1": 机器人QQ,"c2":"2","c3":群号,"c4":"","c5":内容}
    bot.div(Api_OutPut,P)

# Rebot_SendMsg(机器人QQ,群号,内容)

def Rebot_SendFriendMsg(机器人QQ,对方QQ,内容):
    Api_OutPut = "Api_SendMsg"
    P = {"c1": 机器人QQ,"c2":"1","c3":"","c4":对方QQ,"c5":内容}
    bot.div(Api_OutPut,P)

# Rebot_SendFriendMsg(机器人QQ,对方QQ,内容)


def Rebot_IfFriend(机器人QQ,对方QQ):
    Api_OutPut = "Api_IfFriend"
    P = {"c1": 机器人QQ,"c2":对方QQ}
    bot.div(Api_OutPut,P)
    #是否QQ好友（双向） 好友返回真 非好友或获取失败返回假

# Rebot_IfFriend(机器人QQ,对方QQ)


    









