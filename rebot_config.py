

import UI

import configparser

import os

# 获取当前路径

curr_dir = os.path.dirname(os.path.realpath(__file__))

# 合成完整路径

config_path = curr_dir + os.sep + "config.ini"

config = configparser.ConfigParser()

# print(config_path)
config.read(config_path, encoding="GB2312")

 
机器人QQ = config.get('database', '机器人QQ')
QQ群号 = config.get('database', 'QQ群号')

UniqueName_arr = config.get('database', 'UniqueName_arr')  
list1 = UniqueName_arr.split('\n')
list2 = list(list1)

# memo = config.get('database', 'memo')                  
http_ = config.get('database', 'http_')
https_ = config.get('database', 'https_')
listen_add = config.get('database', 'listen_add')
Token_ = config.get('database', 'Token_')
Callback_add = config.get('database', 'Callback_add')
Callback_port = config.get('database', 'Callback_port')


# # -getint(section,option)得到section中的option的值，返回为int类型
# print('getint:' ,' ' ,config.getint('database', 'id'))
# print('getfloat:' ,' ' , config.getfloat('database', 'weight'))
# print('getboolean:' ,'  ', config.getboolean('database', 'isChoice'))

def 初始化():
    import OUYE
    # print("5秒后运行")
    # sleep(5)
    print("开始初始化人气之星和交易高手")
    OUYE.Trading_masters(20)
    # sleep(1000)        
    OUYE.popular_star(20)
    # 初始化一次人气之星和交易高手
    # config.set("database", "listen_add", listen_add)  # 修改指定section 的option
    # config.set("database", "memo", memo)  # 修改指定section 的option
    str1 = '\n'.join(OUYE.uName_arr)
    # str2 = '\n'.join(OUYE.Name_arr)
    UI.UniqueName.setPlainText(str1)
    # UI.memo.setPlainText(str2)
    print("初始化人气之星和交易高手完毕")


def initialize():
    import threading
    t0 = threading.Thread(target=初始化)
    t0.start()
        
def save_():

    机器人QQ = UI.Rebot_QQ_Num.text()
    QQ群号 = UI.Group_QQ_Num.text()
    UniqueName_arr = UI.UniqueName.toPlainText()   # 多行输入框
    # memo = UI.memo.toPlainText()                   # 多行输入框：备注
    http_ = UI.http_.text()
    https_ = UI.https_.text()
    listen_add = UI.listen_add.text()
    Token_ = UI.Token_.text()
    Callback_add = UI.Callback_add.text()
    Callback_port = UI.Callback_port.text()

    config.set("database", "机器人QQ", 机器人QQ)  
    config.set("database", "QQ群号", QQ群号) 
    config.set("database", "UniqueName_arr", UniqueName_arr)  
    # config.set("database", "memo", memo)  
    config.set("database", "http_", http_)  
    config.set("database", "https_", https_)  
    config.set("database", "listen_add", listen_add)  
    config.set("database", "Token_", Token_)  
    config.set("database", "Callback_add", Callback_add)  
    config.set("database", "Callback_port", Callback_port)  

    config.write(open(config_path, 'w'))



    # Debug_info = UI.Debug_info.text()







