"""
    自定义工具类
"""


# 登录的共同的断言方法
def assert_common(self, response_verify, response_login, image, status_code, status, msg):
    self.assertIn(image, response_verify.headers.get("Content-Type"))
    response_json = response_login.json()
    self.assertEqual(status_code, response_login.status_code)
    self.assertEqual(status, response_json.get("status"))
    self.assertIn(msg, response_json.get("msg"))
