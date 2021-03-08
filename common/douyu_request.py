import requests
from requests.sessions import session
import logging
import os


# 重写请求方法,便于直接获取结果
class DYHTTPRequests:

    def __init__(self):
        self.session = session()
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81",
            "referer": "https://www.douyu.com",
            "Cookie": os.environ["COOKIES"]
        }

    def __del__(self):
        self.session.close()

    def request(self, method, path, **kwargs):
        url = "https://www.douyu.com" + path
        method.upper()
        return self.session.request(method, url=url, headers=self.header, **kwargs)


dyreq = DYHTTPRequests()

if __name__ == '__main__':
    print(dyreq.request("get", "/lapi/member/api/getInfo").json())
