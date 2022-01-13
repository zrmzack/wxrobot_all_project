import redis
import json

r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


# 解析所有朋友
def get_friends_para(all_info):
    # 唯一id
    wxid = ""
    # 微信账号
    account = ""
    # 微信名字
    nickname = ""
    # 微信备注
    remark = ""
    for i in all_info:
        wxid = i.get('wxid')
        account = i.get('account')
        nickname = i.get('nickname')
        remark = i.get('remark')
        key = wxid
        value = {"account": account, "nickname": nickname, "remark": remark}
        value = json.dumps(value, ensure_ascii=False)
        r.set(key, value)
    print("微信好友数据解析完成")


def get_chatrooms_para(all_info):
    for i in all_info:
        pass


def is_express_info(string):
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
    return count > 10


def get_index(data):
    infos = data.split(" ")
    return len(infos)


def get_all_express_info(data):
    infos = data.split(" ")
    company = infos[0].strip()
    exprss_id = infos[1].strip()
    if len(infos) == 2:
        return company, exprss_id
    else:
        phone = infos[2].strip()

    return company, exprss_id, phone


def get_all_numbers_para(all_info):
    for i in all_info:
        pass
