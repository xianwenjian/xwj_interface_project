"""
    登录的接口测试 使用unittest框架
"""

# 导包
import unittest
from requests import Session
from api.login_api import LoginAPI
from parameterized import parameterized
import logging
from utils import assert_common

# 创建测试类
class TestLogin(unittest.TestCase):
    # 方法级别的初始化fixture
    def setUp(self):
        # 创建session对象
        self.session = Session()

    # 类级别的初始化fixture
    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginAPI()

    # 方法级别的销毁fixture
    def tearDown(self):
        # 关闭session对象
        self.session.close()

    # 登录成功
    @parameterized.expand({("15627672674", "123456", "8888")})
    def test_login_success(self, username, password, verify_code):
        logging.info("======进入登陆成功测试用例======")
        # 获取验证码
        response_verify = self.login_api.get_login_verify_code(self.session)
        # 登录
        response_login = self.login_api.login(self.session, username, password, verify_code)
        # 断言
        assert_common(self, response_verify, response_login, "image", 200, 1, "登陆成功")

    # 用户名不存在
    @parameterized.expand({("15627670091", "123456", "8888")})
    def test_login_username_is_not_exist(self, username, password, verify_code):
        logging.info("======进入用户名不存在测试用例======")
        # 获取验证码
        response_verify = self.login_api.get_login_verify_code(self.session)
        # 登录
        response_login = self.login_api.login(self.session, username, password, verify_code)
        # 断言
        assert_common(self, response_verify, response_login, "image", 200, -1, "账号不存在")

    # 密码错误
    @parameterized.expand({("15627672674", "error00", "8888")})
    def test_login_verify_code_is_error(self, username, password, verify_code):
        logging.info("======进入密码错误测试用例======")
        # 获取验证码
        response_verify = self.login_api.get_login_verify_code(self.session)
        # 登录
        response_login = self.login_api.login(self.session, username, password, verify_code)
        # 断言
        assert_common(self,response_verify,response_login, "image",200, -2, "密码错误")

