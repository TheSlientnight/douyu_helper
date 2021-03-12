# encoding:utf-8
from requests.sessions import session
from common.get_secrets import get_secrets


# 重写请求方法,便于直接获取结果
class DYHTTPRequests:

    def __init__(self):
        self.cookie = get_secrets('COOKIES')
        self.session = session()
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81",
            "referer": "https://www.douyu.com",
            "Cookie": self.cookie
        }

    def request(self, method, path, **kwargs):
        url = "https://www.douyu.com" + path
        method.upper()
        return self.session.request(method, url=url, headers=self.header, **kwargs)

    def __del__(self):
        self.session.close()


dyreq = DYHTTPRequests()
if __name__ == '__main__':
    print(dyreq.request("get", "/lapi/member/api/getInfo").json())
    glow_url = "/japi/prop/backpack/web/v1?rid=12306"
    print(dyreq.request("get", glow_url).json())
