# -*- coding: utf-8 -*-
# @ Time: 2021/2/20 14:09
# @ Author: YanZhiJia
# @ Email: asce_yan@foxmail.com
# @ File: config
# @ Description: 管理项目配置文件
import os
from configparser import ConfigParser
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
CONFIG_FILE = os.path.join(CONFIG_PATH, 'config.ini')


class Config(object):
    # Title
    __TITLE_LOGGER = 'Logger'
    __TITLE_SERVER = 'ServerURL'
    # Value
    __VALUE_LEVEL = 'Level'
    __VALUE_ISCONSOLE = 'isConsole'
    __VALUE_TEST_URL = 'TEST_URL'
    __VALUE_DEV_URL = 'DEV_URL'
    __VALUE_PROD_URL = 'PROD_URL'

    def __init__(self):
        self.config = ConfigParser()
        if not os.path.exists(CONFIG_FILE):
            raise FileNotFoundError("请确保配置文件存在！")
        try:
            self.config.read(CONFIG_FILE, encoding='utf-8')
        except:
            raise Exception(f'读取{CONFIG_FILE}文件出错')
        self.log_level = self.get_conf(self.__TITLE_LOGGER, self.__VALUE_LEVEL)
        self.is_console = self.get_conf(self.__TITLE_LOGGER, self.__VALUE_ISCONSOLE)
        self.test_url = self.get_conf(self.__TITLE_SERVER, self.__VALUE_TEST_URL)
        self.dev_url = self.get_conf(self.__TITLE_SERVER, self.__VALUE_DEV_URL)
        self.prod_url = self.get_conf(self.__TITLE_SERVER, self.__VALUE_PROD_URL)

    def get_conf(self, title, value):
        return self.config.get(title, value)
