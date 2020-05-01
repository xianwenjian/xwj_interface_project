"""
    这是登录的api接口
"""


# 导包
import logging

# 定义登录api类
class LoginAPI:
    def __init__(self):
        # 验证码网址
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        # 登录网址
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # 获取验证码的方法
    def get_login_verify_code(self, session):
        logging.info("*********API中:获取验证码的方法*********")
        return session.get(self.verify_url)

    # 登录方法
    def login(self, session, username, password, verify_code):
        logging.info("*********API中:登录方法*********")
        data = {"username": username, "password": password, "verify_code": verify_code}
        return session.post(self.login_url, data=data)
