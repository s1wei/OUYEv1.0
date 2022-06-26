


let arr = [];
let now = time()
function main() {

    let nickName;

    let dalao = {
        "一只鱼啊啊啊":"05223D04D8C41E04",
        "币圈佐为":"FC5A4C4893FFECBA",
        "北雨导演":"9F6BF9DEA8CD6F5E",
        "赚多点钱":"623AB0D6C631337D",
        "岐山臊子面的岐":"F4A03BC3A2C4173E",
        "牧人":"7A1548D2E73C232B",
        "麒歌CTA2号":"52EE4CEEF2334575",
        "ZC招财进宝":"38097AFE430F4C40",
        "高山流水":"AFF8D9F53C161011",
        "朱荣树":"4BFFCC8C92C9CBED"
    }

    // now_Asset_distribution(dalao.赚多点钱)

    // thread.execAsync(function () {
    //     while (true) {
    //         let selectors= clz("android.widget.EditText");
    //         let result = pasteText(selectors,"运行正常...每10分钟发送一次");
    //         sleep(1000)
    //         let send = text("发送").getOneNodeInfo(300)
    //         if (send) {
    //             send.click()
    //         }
    //         logi("运行正常...")
    //         sleep(600000)
    //     }
    // })
    // now_earnings(dalao.赚多点钱)


    // Trading_masters()
    // sleep(2000000)


    while (true){

        now_action(dalao.一只鱼啊啊啊)

        now_action(dalao.币圈佐为)

        now_action(dalao.北雨导演)

        now_action(dalao.赚多点钱)

        now_action(dalao.岐山臊子面的岐)

        now_action(dalao.麒歌CTA2号)

        now_action(dalao.ZC招财进宝)

        now_action(dalao.高山流水)

        now_action(dalao.牧人)

        now_action(dalao.朱荣树)

    }

}
main()

function Trading_masters() {
    //https://www.okx.com/priapi/v5/ecotrade/public/trade-expert-rate?t=1653826950022&size=8&num=1
    let gsurl = "https://www.okx.com/priapi/v5/ecotrade/public/trade-expert-rate"
    let p = {
        "size": "8",
    }
    let web_pkg = http.httpGet(gsurl,p,20 * 1000,{"content-type":"application/json;charset=UTF-8"})
    if (web_pkg) {
        let web_pkg_arr = JSON.parse(web_pkg).data;
        if (web_pkg_arr) {
            
            logd(JSON.parse(JSON.stringify(web_pkg_arr))[0].ranks)
            let web_pkg_arrr = JSON.parse(JSON.stringify(web_pkg_arr))[0].ranks;
            for (let i = 0; i<web_pkg_arrr.length;i++){
                let pkg = JSON.stringify(web_pkg_arrr[i])

                let nickName = JSON.parse(pkg).nickName;    //大佬名字
                let riskLevel = JSON.parse(pkg).riskLevel;   //风险等级

            }
        }
    }
}   //交易高手

function popular() {
    //https://www.okx.com/priapi/v5/ecotrade/public/popular-star-rate?t=1653826950023&size=8&num=1
}   //人气之星


function now_action(uniqueName) {


    let czurl = "https://www.okx.com/priapi/v5/ecotrade/public/trade-records"
    let p = {
        // "t":"1653620788708",1653700498518
        // "startModify":"1651075200000",1651161600000
        // "endModify":"1653667199000",1653753599000
        "limit":"5",
        "sortType":"filledTime",
        "page":"1",
        "uniqueName":uniqueName    //大佬的id
    }

    let web_pkg = http.httpGet(czurl,p,20 * 1000,{"content-type":"application/json;charset=UTF-8"})
    if (web_pkg) {
        let web_pkg_arr = JSON.parse(web_pkg).data;
        if (web_pkg_arr) {
            for (let i = 0; i<web_pkg_arr.length;i++){
                let pkg = JSON.stringify(web_pkg_arr[i]);

                nickName = (JSON.parse(pkg).nickName); //名字
                let avgPx = (JSON.parse(pkg).avgPx); //均价
                let quoteName = (JSON.parse(pkg).quoteName); //引用币种名称
                let cTime = (JSON.parse(pkg).cTime);  //交易时间（需要时间戳ms转换）
                let side = (JSON.parse(pkg).side);  //买卖行为
                let ordType = (JSON.parse(pkg).ordType) //平  开
                let posSide = (JSON.parse(pkg).posSide) //多  空  无
                let uly = (JSON.parse(pkg).uly) //交易币种
                let instType = (JSON.parse(pkg).instType) //杠杆
                let lever = (JSON.parse(pkg).lever)    //杠杆倍数

                //logd(dateTrans(cTime))
                // logd(dateTrans(cTime) + " " + nickName + " 以均价 " + avgPx +" "+ quoteName +" "
                //     + side_action(side) + 平开(ordType) + 多空(posSide) + uly + " "+杠杆(instType,lever)  )
                let shuchu = dateTrans(cTime) + "\n" + nickName + " 以均价\n" + avgPx +" "+ quoteName +" "
                    + side_action(side) + 平开(ordType) + 多空(posSide) + uly + " "+杠杆(instType,lever)



                if (name_repeat(cTime, arr)) {
                    break;
                    //logd(shuchu)
                } else {
                    // logd(cTime)
                    // logd(now)
                    arr.push(cTime)
                    logi(shuchu);
                    if (cTime >= now) {
                        // logi("eeee")
                        // logi(shuchu);
                        let selectors= clz("android.widget.EditText");
                        pasteText(selectors,shuchu+"\n**************************\n");

                        pasteText(selectors,now_earnings(uniqueName,nickName));

                        now_Asset_distribution(uniqueName,nickName)

                        now_position(uniqueName,nickName)
                    }
                }
            }


        }
        //console.log(web_pkg_arr);
    }

}               //实时操作监控

function now_earnings(uniqueName,nickName) {
    let zcurl = "https://www.okx.com/priapi/v5/ecotrade/public/total-pnl"
    let p = {
        // "t":"1653620788708"
        "limit":"10",
        "uniqueName":uniqueName    //大佬的id
    }
    let web_pkg = http.httpGet(zcurl,p,20 * 1000,{"content-type":"application/json;charset=UTF-8"})
    let web_pkg_arr = JSON.stringify(JSON.parse(web_pkg).data);
    if (web_pkg_arr) {
        //logd(web_pkg_arr)
        let earnings = (JSON.parse(web_pkg_arr)[JSON.parse(web_pkg_arr).length-1].ratio * 100) +"%";
        return "  *  "+nickName+"  *  "+"\n" +"总收益:"+earnings +"\n--------------------------";
    }


}     //目前截至总收益

function now_Asset_distribution(uniqueName) {
    let zcurl = "https://www.okx.com/priapi/v5/ecotrade/public/asset"
    let p = {
        // "t":"1653620788708"
        "limit":"10",
        "uniqueName":uniqueName    //大佬的id
    }
    let web_pkg = http.httpGet(zcurl,p,20 * 1000,{"content-type":"application/json;charset=UTF-8"})
    if (web_pkg) {
        let web_pkg_arr = JSON.stringify(JSON.parse(web_pkg).data);
        if (web_pkg_arr) {
            // logd(web_pkg_arr)
            let selectors= clz("android.widget.EditText");
            pasteText(selectors,"\n资产分布:\n");
            for (let i = 0; i<JSON.parse(web_pkg_arr).length;i++){
                let currency = JSON.parse(web_pkg_arr)[i].currency;
                let percent = ((JSON.parse(web_pkg_arr)[i].percent) * 100 ).toFixed(4) + "%";
                let shuchu = currency + ": " + percent +"\n"

                let selectors= clz("android.widget.EditText");
                pasteText(selectors,shuchu);

            }
            pasteText(selectors,"=======================\n");
        }
    }
}  //当前资产分布

function now_position(uniqueName) {

    let ccurl = "https://www.okx.com/priapi/v5/ecotrade/public/positions-v2"
    let p = {
        // "t":"1653620788708"
        "limit":"10",
        "uniqueName":uniqueName    //大佬的id
    }

    let web_pkg = http.httpGet(ccurl,p,20 * 1000,{"content-type":"application/json;charset=UTF-8"})
    if (web_pkg) {
        let web_pkg_arr = JSON.stringify(JSON.parse(web_pkg).data);
        if (web_pkg_arr) {

            let selectors= clz("android.widget.EditText");

            pasteText(selectors,当前持仓空多倍(web_pkg_arr)+"\n");

            let posData = JSON.parse(web_pkg_arr)[0].posData;
            // logd(JSON.stringify(posData));
            for (let i = 0; i<posData.length;i++){
                let pkg = JSON.stringify(posData[i])

                let instId = (JSON.parse(pkg).instId); //币名字
                let instType = (JSON.parse(pkg).instType) //杠杆
                let lever = (JSON.parse(pkg).lever)    //杠杆倍数
                let posSide = (JSON.parse(pkg).posSide) //多  空  无
                let uplRatio = (JSON.parse(pkg).uplRatio) * 100 +"%" //收益率
                let avgPx = (JSON.parse(pkg).avgPx) ; //均价
                let liqPx = (JSON.parse(pkg).liqPx) ; //预估强平价
                let posSpace = (JSON.parse(pkg).posSpace) * 100  +"%";  //仓位大小

                let shuchu = "\n" + instId + 多空(posSide) +杠杆(instType,lever) + "\n"
                    +"收益率:"+uplRatio+ "\n" + "开仓均价:"+ avgPx + "\n" + "预估强平价:"+ liqPx + "\n" + "仓位大小:"+posSpace + "\n"
                    +"----------------------------------"

                let selectors= clz("android.widget.EditText");
                let result = pasteText(selectors,shuchu);

            }
            sleep(1000)
            let send = text("发送").getOneNodeInfo(300)
            if (send) {
                send.click()
            }
        }
    }
}              //当前持仓收益


function 当前持仓空多倍(web_pkg_arr) {
    let sc = "当前持仓:"

    let longLever = JSON.parse(web_pkg_arr)[0].longLever
    if (longLever !== null) {
        sc = sc + "多:"+ longLever +"倍|";
    }
    let shortLever = JSON.parse(web_pkg_arr)[0].shortLever
    if (shortLever !== null) {
        sc = sc + "空:"+ shortLever +"倍";
    }
    return sc;
}

function dateTrans(date) {
    let _date = new Date(parseInt(date));
    let y = _date.getFullYear();
    let m = _date.getMonth() + 1;
    m = m < 10 ? ('0' + m) : m;
    let d = _date.getDate();
    d = d < 10 ? ('0' + d) : d;
    let h = _date.getHours();
    h = h < 10 ? ('0' + h) : h;
    let minute = _date.getMinutes();
    let second = _date.getSeconds();
    minute = minute < 10 ? ('0' + minute) : minute; second = second < 10 ? ('0' + second) : second;
    let dates = y + '/' + m + '/' + d + '|' + h + ':' + minute + ':' + second
    return dates;
}

function side_action(side) {
    if (side === "buy") {
        return "买入";
    } else if (side === "sell") {
        return "卖出";
    }
}

function 平开(ordType) {
    if (ordType === "market") {
        return "平";
    } else if (ordType === "limit") {
        return "开"
    }
}

function 多空(posSide) {
    if (posSide === "long") {
        return "多";
    } else if (posSide === "short") {
        return "空";
    } else {
        return "";
    }
}

function 杠杆(instType,lever) {
    if (instType === "SWAP") {
        return "永续" + lever+"X";
    } else if (instType === "SPOT") {
        return "";
    } else {
        return "【未知】";
    }
}

function name_repeat(title, arr) {
    var res = false
    for (let i = 0; i < arr.length; i++) {
        if (title === arr[i]) {
            res = true;
        }
    }
    return res;
}   //判断是否重复


