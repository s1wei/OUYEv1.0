



# if rebot_start = 1

def main():

    from time import sleep

    import rebot_config  #机器人配置

    import rebot_main       #机器人菜单

    import rebot_now_action #机器人检测欧意

    import threading    #
    

    机器人QQ = rebot_config.机器人QQ
    QQ群号 = rebot_config.QQ群号  
    # 机器人QQ = "166264438"
    # QQ群号 = "764297732" 
    
        
    t1 = threading.Thread(target=rebot_main.rebot_menu,args=(机器人QQ,QQ群号))                #菜单
    t2 = threading.Thread(target=rebot_now_action.thread_now_action,args=(机器人QQ,QQ群号))   #监听
    
    def thread():
        try:
            print("启动菜单线程")
            sleep(2)
            t1.start()
            print("启动菜单线程完毕")

            print("启动监控线程")
            sleep(2)
            t2.start()
            print("启动监控线程完毕")
            # i = 0
            # while 1 :
            #     sleep(600)
            #     i = i + 10
            #     print("已经运行了"+str(i)+"分钟")
        except:
            print("出现错误 重新启动线程")
            thread()
    
    thread()
	
		