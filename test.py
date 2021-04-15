cookies = {
    "dy_did": "b0589ec44a2c4306be885d2400021601",
    "acf_did": "b0589ec44a2c4306be885d2400021601",
    "Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7": "1614143819,1615360238",
    "PHPSESSID": "0vr61jfcadgp7pcfkii1lq3m44",
    "acf_auth": "1df4lTvJxBCi31n8tc99%2BzqpgtpD%2FKf7RT%2Bmwm6zdJMCfIeWCqMGZyzZV2p0kfTWoRvzPUssXP4pd8CIQ0LDA5fXNBTsdW1M0GiurzWfX4IDufbd4K9FTa2rKyOV",
    "dy_auth": "1ceefP8rhiqcn2uwk0jETTdWEZOiFM%2FzNO71iyrch6ol5ETDhlsjDBXJLhfaSERtAIlP%2FafPjiXCqLQ%2FXDVYnyE8gEOM58kJD7xiwMbEz2ijC%2FrblV8xVtDvl%2BMs",
    "wan_auth37wan": "5d68f65be16dUvMfFeriJ1pq2muQ83ZxSRdP4F7SPVMqDZzGBP%2F2HU417bkLtBT3jzWAsYudegSW6wgHGl5OZiJhzNCVasmZs3kW%2F901jSQd4zTM",
    "acf_uid": "9096489",
    "acf_username": "auto_0ZpUDqZB1y",
    "acf_nickname": "%E5%B0%B1%E5%8F%AB%E9%BB%98%E5%A4%9C%E5%90%A7",
    "acf_own_room": "1",
    "acf_groupid": "1",
    "acf_phonestatus": "1",
    "acf_avatar": "https%3A%2F%2Fapic.douyucdn.cn%2Fupload%2Favatar%2F009%2F09%2F64%2F89_avatar_",
    "acf_ct": "0",
    "acf_ltkid": "33163986",
    "acf_biz": "1",
    "acf_stk": "cd048d3aee7d5fe1",
    "Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7": "1615360518"
}
cookie2 = "acf_auth=c4c3BV0tKu%2BvN8zC%2Fr0u%2FnDAjwnsN8p%2FSg%2F5JRK6HGc8jGqNufxM2Guo5eTibJOnLvRh1O7uMIljljqbelUdT6gm%2F3tUejsphkOhBVsAKxbC2MxItEp6jEQ;dy_auth=0a93VkWISam8mCKingJHcbw7AuibTXvf1sp0nUK0VXS%2BupJOnnlXd79w6%2Fh1NLnXEXIBTu4Z0CQqYT1sCja5qv5Z0amokMzwaSh6vhPEAJocNtHVsCnYb9Q"
cookie3 = {}


def setcookie(cookies):
    cookie = ''
    for name, value in cookies.items():
        cookie += '{0}={1};'.format(name, value)
    return cookie


def setcookie2(cookie):
    for line in cookie.split(';'):
        # 其设置为1就会把字符串拆分成2份
        name, value = line.strip().split('=', 1)
        cookie3[name] = value
    return cookie3
import requests

if __name__ == '__main__':
    a = setcookie(cookies)
    b = setcookie2(cookie2)
    print(a)
