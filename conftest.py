# -*- coding: utf-8 -*-
# @ Time: 2021/2/20 16:05
# @ Author: YanZhiJia
# @ Email: asce_yan@foxmail.com
# @ File: conftest
# @ Description:
import pytest
import os
from common.config import Config
from common.parse_data import ReadYaml
# 获取不同环境的url
test_url = Config().test_url
dev_url = Config().dev_url
prod_url = Config().prod_url
BASE_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(BASE_PATH, 'data')


def pytest_addoption(parser):
    # 自定义命令行，用于接收host地址
    parser.addoption(
        '--host', action='store', default='127.0.0.1', help='input your host address'
    )
    # 自定义命令行，用于接收当前环境特征
    parser.addoption(
        '--env', action='store', default='test', choices=['dev', 'prod', 'test'],
        help="Select the test case run environment: ['dev', 'prod', 'test']"
    )


@pytest.fixture(scope='session')
def get_host(request):
    return request.config.getoption('--host')


@pytest.fixture(scope='session')
def get_env(request):
    return request.config.getoption('--env')


@pytest.fixture(scope='session')
def get_url(request):
    """获取不同环境对应的服务地址"""
    env = request.getfixturevalue('get_env')
    if env == 'test':
        return test_url
    elif env == 'dev':
        return dev_url
    elif env == 'prod':
        return prod_url


@pytest.fixture(scope='session')
def get_load_data(request):
    # 接收测试用例文件的名称
    file_name = request.param
    env = request.getfixturevalue('get_env')
    # 根据传入的环境变量参数，计算出应该用那个环境下的数据文件
    env_folder = os.path.join(DATA_PATH, env)
    data_file_name = file_name.replace('.py', '.yml')
    data_file = os.path.join(env_folder, data_file_name)
    # 读取并处理yml文件格式
    return ReadYaml.read_yaml(yamlpath=data_file)