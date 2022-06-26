
from time import sleep
from tkinter import E
import OUYE
import rebot_one
import rebot_config
import threading


def thread_now_action(机器人QQ,群号):
    while 1:
        for i in range(0,len(rebot_config.list2)):

            # print("当前："+ rebot_config.list2[i])

            # def now_action_time():
            nr = OUYE.now_action(rebot_config.list2[i])
            if str(nr) != "None":
                内容 = nr
                print(内容)
                rebot_one.Rebot_SendMsg(机器人QQ,群号,内容)

                # else :
                #     内容 = nr
                #     print(内容)
                #     rebot_one.Rebot_SendMsg(机器人QQ,群号,内容)

            # t3 = threading.Thread(target=now_action_time)
            # t3.start()
            # sleep(0.5)
