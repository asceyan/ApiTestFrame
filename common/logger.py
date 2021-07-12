# -*- coding: utf-8 -*-
# @ Time: 2021/2/8 16:43
# @ Author: YanZhiJia
# @ Email: asce_yan@foxmail.com
# @ File: logger
# @ Description: 指定保存日志的文件路径，日志级别

import logging
import os
import time
from common.config import Config

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOG_PATH = os.path.join(BASE_PATH, 'logs', '')
Error_LOG = os.path.join(LOG_PATH, "error", '')
INFO_LOG = os.path.join(LOG_PATH, "info", '')
is_console = Config().is_console
log_level = Config().log_level


class Logger(object):
    """自定义日志模块"""
    __time_stamp = time.strftime('%Y%m%d%H%M%S.logs')
    __err_name = Error_LOG + __time_stamp
    __info_name = INFO_LOG + __time_stamp
    log_format = '%(asctime)s - %(levelname)s - %(filename)s:[%(lineno)d] - %(threadName)s:[%(thread)d] - Message: %(message)s'

    def __init__(self, name=None):
        # 查看日志文件路径是否存在，不存在则创建
        if os.path.isdir(LOG_PATH):
            if os.path.exists(Error_LOG):
                pass
            else:
                os.mkdir(Error_LOG)
            if os.path.exists(INFO_LOG):
                pass
            else:
                os.mkdir(INFO_LOG)
        else:
            os.mkdir(LOG_PATH)
            os.mkdir(Error_LOG)
            os.mkdir(INFO_LOG)
        self.logger = logging.getLogger(name)

    def get_log(self):
        # 设置日志级别
        self.logger.setLevel(log_level)
        # 定义handler的输出格式
        formatter = logging.Formatter(self.log_format)
        err_handler = logging.FileHandler(self.__err_name, encoding='utf-8')
        err_handler.setLevel('ERROR')
        info_handler = logging.FileHandler(self.__info_name, encoding='utf-8')
        info_handler.setLevel('INFO')
        # 再创建一个handler，用于输出到控制台
        con_handler = logging.StreamHandler()
        con_handler.setLevel('INFO')
        # handler载入格式
        err_handler.setFormatter(formatter)
        info_handler.setFormatter(formatter)
        con_handler.setFormatter(formatter)
        # 判断是否将log输出至控制台
        if eval(is_console):
            # 给logger添加handler
            self.logger.addHandler(err_handler)
            self.logger.addHandler(info_handler)
            self.logger.addHandler(con_handler)
        else:
            self.logger.addHandler(err_handler)
            self.logger.addHandler(info_handler)
        return self.logger


if __name__ == '__main__':
    logger = Logger().get_log()
    logger.info('This is a logs info')
    logger.debug('Debugging')
    logger.warning('Warning exists')
    logger.info('Finish')
    logger.error('error')

