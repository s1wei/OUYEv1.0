from encodings import utf_8

import time

import json

from webbrowser import Elinks

import rebot_config

# 请求
from email import header

import rebot_config

import requests

header = {"content-type":"application/json;charset=UTF-8"}

proxie = {'http':rebot_config.http_,'https':rebot_config.https_}



time_arr = []

uName_arr = []

Name_arr = []

now = int(round(time.time() * 1000))

##  以下是爬虫代码

def name_repeat(title, time_arr):
    res = 1
    for i in range(0,len(time_arr)) :
        if title == time_arr[i] :
            res = 0;
    return res

def uName_arr_repeat(title, uName_arr):
    res = 1
    for i in range(0,len(uName_arr)) :
        if title == uName_arr[i] :
            res = 0;
    return res

# 时间戳转换时间
def dateTrans(cTime):
    timeStamp = float(int(cTime)/1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

def 平开(ordType):
    if ordType == "market":
        return "平";
    elif ordType == "limit":
        return "开"

def side_action(side):
    if side == "buy":
        return "买入";
    elif side == "sell":
        return "卖出"

def 多空(posSide):
    if posSide == "long":
        return "多";
    elif posSide == "short":
        return "空";
    else:
        return "";
    
def 杠杆(instType,lever):
    if instType == "SWAP":
        return "永续" + lever+"X";
    elif instType == "SPOT":
        return "";
    else:
        return "【未知】";

def 风险等级(riskLevel):
    if riskLevel == "low":
        return "低"
    elif riskLevel == "middle":
        return "中"
    elif riskLevel == "high":
        return "高"

# 交易高手
def Trading_masters(size):
    
    url = "https://www.okx.com/priapi/v5/ecotrade/public/trade-expert-rate"

    p = {
        "size": size,
        "num":"1"
        }
    header = {"content-type":"application/json;charset=UTF-8"}

    # print("开始请求")
    
    web_pkg = requests.get(url=url,params=p,timeout=20 * 1000,headers=header,proxies=proxie)

    if web_pkg:
        web_pkg_arr = json.loads(web_pkg.text)["data"]
        
        web_pkg_arr1 = json.dumps(web_pkg_arr)
        
        web_pkg_arr2 = json.loads(web_pkg_arr1)[0]["ranks"]

        time = "交易高手:\n[Time]\n"
        内容 = ""
        for i in range(0,len(web_pkg_arr2)):

            pkg = json.dumps(web_pkg_arr2[i])

            nickName = json.loads(pkg)['nickName']    # 昵称

            uniqueName =json.loads(pkg)['uniqueName'] # 编号

            yieldRate = float(json.loads(pkg)['yieldRate'])*100  # 收益率

            riskLevel = json.loads(pkg)['riskLevel']  # 风险等级

            longLever = json.loads(pkg)['longLever']  # 多倍

            shortLever = json.loads(pkg)['longLever'] # 空倍

            shuchu = "\n-------------------------\n昵称："+nickName +"\n收益率："+str(yieldRate) + "%\n风险等级："+ 风险等级(riskLevel) + "\n多:"+ longLever +"倍|空:"+ shortLever +"倍"

            内容 = 内容 + shuchu

            if uName_arr_repeat(uniqueName, rebot_config.list2):
                uName_arr.append(uniqueName)
                # Name_arr.append(nickName)

        内容 = time + 内容
        
        return 内容

# 人气之星
def popular_star(size):
        
    url = "https://www.okx.com/priapi/v5/ecotrade/public/popular-star-rate"

    p = {
        "size": size,
        "num":"1"
        }
    header = {"content-type":"application/json;charset=UTF-8"}

    web_pkg = requests.get(url=url,params=p,timeout=20 * 1000,headers=header,proxies=proxie)

    if web_pkg:
        web_pkg_arr = json.loads(web_pkg.text)["data"]
        
        web_pkg_arr1 = json.dumps(web_pkg_arr)
        
        web_pkg_arr2 = json.loads(web_pkg_arr1)[0]["ranks"]

        time = "人气之星:\n[Time]\n"
        内容 = ""
        for i in range(0,len(web_pkg_arr2)):

            pkg = json.dumps(web_pkg_arr2[i])

            nickName = json.loads(pkg)['nickName']    # 昵称

            uniqueName =json.loads(pkg)['uniqueName'] # 编号

            yieldRate = str(float(json.loads(pkg)['yieldRate'])*100) + "%"  # 收益率

            riskLevel = json.loads(pkg)['riskLevel']  # 风险等级

            longLever = json.loads(pkg)['longLever']  # 多倍

            shortLever = json.loads(pkg)['longLever'] # 空倍

            shuchu = "\n-------------------------\n昵称："+nickName +"\n收益率："+str(yieldRate) + "%\n风险等级："+ 风险等级(riskLevel) + "\n多:"+ longLever +"倍|空:"+ shortLever +"倍"

            内容 = 内容 + shuchu

            if uName_arr_repeat(uniqueName, rebot_config.list2):
                uName_arr.append(uniqueName)
                # Name_arr.append(nickName)

        内容 = time + 内容
        
        return 内容

# 现在动态
def now_action(uniqueName):
    
    url ="https://www.okx.com/priapi/v5/ecotrade/public/trade-records"

    p = {        
        "limit":"5",
        "sortType":"filledTime",
        "page":"1",
        "uniqueName":uniqueName    
        }
    
    web_pkg = requests.get(url=url,params=p,timeout=20 * 1000,headers=header,proxies=proxie)


    if web_pkg:
        web_pkg_arr = json.loads(web_pkg.text)["data"]
        for i in range(0,len(web_pkg_arr)):
            pkg = json.dumps(web_pkg_arr[i])
            
            nickName = json.loads(pkg)['nickName']    # 昵称
            avgPx = json.loads(pkg)['avgPx']          # 均价
            quoteName = json.loads(pkg)['quoteName']  # 引用币种名称
            cTime = json.loads(pkg)['cTime'];         # 交易时间（需要时间戳ms转换）
            side = json.loads(pkg)['side']            # 买卖行为
            ordType = json.loads(pkg)['ordType']      # 平  开
            posSide = json.loads(pkg)['posSide']      # 多  空  无
            uly = json.loads(pkg)['uly']              # 交易币种
            instType = json.loads(pkg)['instType']    # 杠杆
            lever = json.loads(pkg)['lever']          # 杠杆倍数  
            

            if 多空(posSide) =="多" or 多空(posSide) == "空" :
            
                shuchu = dateTrans(cTime) + "\n" + nickName + " 以均价\n" + avgPx +" "+ quoteName +" "+ side_action(side) + 平开(ordType) + 多空(posSide) + uly + " "+杠杆(instType,lever)

                if name_repeat(cTime, time_arr) :
                    time_arr.append(cTime)
                    # print(shuchu)
                    if int(cTime) >= now :
                        return shuchu
                    else :
                        return;
            

