import logging
import time
from logging import handlers


# 初始化日志配置
def init_log_config():
    # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 创建控制台处理器
    sh = logging.StreamHandler()
    # 创建文件处理器

    log_path = "../log/log{}.log".format(time.strftime("%Y%m%d-%H%M%S"))
    fh = logging.handlers.TimedRotatingFileHandler(log_path, when="midnight", interval=1, backupCount=7,
                                                   encoding="UTF-8")
    # 创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] -%(message)s'
    formatter = logging.Formatter(fmt)
    # 把格式化器添加到处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 把处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)
