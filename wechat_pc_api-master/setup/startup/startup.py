# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wechat
import time

from corona.get_corona import get_csv
from db.redis_core import get_answer, calculate
from hongbao.get_hongbao import set_elm_key, set_mt_key
from kuaidi.get_kd import get_express_data
from utils.parase_data import get_friends_para, is_express_info, get_index, get_all_express_info
from weather.get_weather_data import init
from weather.position import get_position
from wechat import WeChatManager, MessageType

wechat_manager = WeChatManager(libs_path='../../libs')
position = get_position()


# 这里测试函数回调
@wechat.CONNECT_CALLBACK(in_class=False)
def on_connect(client_id):
    print('[on_connect] client_id: {0}'.format(client_id))


# if msg.type == 'Attachment':
#     msg.get_file(msg.file_name)
#     msg.chat.send(msg.file_name + '文件接收完成')
#     x, y = calculate(msg.file_name)
#     msg.chat.send('数据解析完成')
#     string = str('最有可能出现问题机房:  ') + str(y) + '  发生概率是:  ' + str(x)
#     msg.chat.send(string)

@wechat.RECV_CALLBACK(in_class=False)
def on_recv(client_id, message_type, message_data):
    print(message_data, message_type)
    # 解析用户
    if (message_type == MessageType.MT_DATA_FRIENDS_MSG):
        get_friends_para(message_data)

    #  回复单聊信息
    if message_type == MessageType.MT_RECV_TEXT_MSG and message_data.get("room_wxid") == "" and message_data.get(
            "from_wxid") != "wxid_34gi7tto8w0w12":
        wxid = message_data.get("from_wxid")
        info = message_data.get("msg")
        wechat_manager.send_text(1, wxid, info)

    #  回复群聊信息
    if message_type == MessageType.MT_RECV_TEXT_MSG and message_data.get("room_wxid") != "" and message_data.get(
            "from_wxid") != "wxid_34gi7tto8w0w12" and message_data.get("msg")[:6] == "@我是机器人":
        wxid = message_data.get("room_wxid")
        info = message_data.get("msg")[7:]
        relay = False
        if relay == False:
            if ("今天天气" or "明天天气") in info:
                all, tianqi, kqzl, jrtq, oneday = init('北京')
                send_message = "北京" + tianqi + '\n' + kqzl + '\n' + jrtq + '\n' + oneday
                wechat_manager.send_text(client_id, wxid, send_message)
                relay = True
            elif ("天气") in info:
                for i in position:
                    if i in info:
                        all, tianqi, kqzl, jrtq, oneday = init(i)
                        send_message = str(i) + tianqi + '\n' + kqzl + '\n' + jrtq + '\n' + oneday
                        wechat_manager.send_text(client_id, wxid, send_message)
                        relay = True
            if ("疫情") in info:
                cor = get_csv()
                string = ''
                for i in set(cor):
                    string += str(i) + ' '
                wechat_manager.send_text(client_id, wxid, ('目前疫情区域：' + string))
                # wechat_manager.send_file(client_id, wxid, "疫情.csv")
                relay = True
            if ("饿了么红包") in info:
                url = set_elm_key()
                wechat_manager.send_text(client_id, wxid, url)
                relay = True
            if ("美团红包") in info:
                url = set_mt_key()
                wechat_manager.send_text(client_id, wxid, url)
                relay = True
            if is_express_info(info):
                # print(msg.text)
                if get_index(info) == 3:
                    company, exprss_id, phone = get_all_express_info(info)
                    # print(phone)
                    # print(company)
                    # print(exprss_id)
                    info = get_express_data(str(company), str(exprss_id), str(phone))
                    # print(info)
                    wechat_manager.send_text(client_id, wxid, info)
                    relay = True

                if get_index(info) == 2:
                    company, exprss_id = get_all_express_info(info)
                    info = get_express_data(company, exprss_id, "")
                    wechat_manager.send_text(client_id, wxid, info)
                    relay = True
        if relay == False and get_answer(info) == None:
            a = '换个问题问吧'
            wechat_manager.send_text(client_id, wxid, a)
        else:
            a = get_answer(info)
            wechat_manager.send_text(client_id, wxid, a)


@wechat.CLOSE_CALLBACK(in_class=False)
def on_close(client_id):
    print('[on_close] client_id: {0}'.format(client_id))


# 这里测试类回调， 函数回调与类回调可以混合使用
class LoginTipBot(wechat.CallbackHandler):

    @wechat.RECV_CALLBACK(in_class=True)
    def on_message(self, client_id, message_type, message_data):
        if message_type == MessageType.MT_USER_LOGIN:
            time.sleep(2)
            wechat_manager.get_friends(client_id)
        if (message_type == MessageType.MT_RECV_FILE_MSG) and message_data.get("room_wxid") == "":
            filename = message_data.get("file")
            wxid = message_data.get("from_wxid")
            time.sleep(3)
            x, y = calculate(filename)
            print("文件解析完成")
            wechat_manager.send_text(client_id, wxid, str('最有可能出现问题机房:  ') + str(y) + '  发生概率是:  ' + str(x))
            print("Jieshu")


if __name__ == "__main__":
    bot = LoginTipBot()

    # 添加回调实例对象
    wechat_manager.add_callback_handler(bot)
    wechat_manager.manager_wechat(smart=True)

    # 阻塞主线程
    while True:
        time.sleep(0.5)
