import time
import unittest
from script.test_login import TestLogin
from tools_lib.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))

# 测试报告文件路径
report_file = "../report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
with open(report_file, "wb") as f:
    # 创建HTMLTestRunner运行器
    runner = HTMLTestRunner(f, title="xwj之TPshop接口自动化测试报告", description="xwj_V1.0")
    # 运行测试套件
    runner.run(suite)