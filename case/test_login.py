# -*- coding: utf-8 -*-
import os
import pytest
import allure
from common.api_base import APIBase
from common.com_assert import Assert
from common.parse_data import ReadYaml
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DATA_PATH = os.path.join(BASE_PATH, 'data')
yaml_path = os.path.join(DATA_PATH, 'login_data.yml')
# 读取测试数据
login_data = ReadYaml.read_yaml(yaml_path).get('login_data')


@allure.feature('TestLogin')
class TestLogin:
    def setup_class(self):
        self.CA = Assert()
        self.base_api = APIBase()

    @allure.story('登录接口测试用例')
    @allure.title("{title}")
    @pytest.mark.parametrize("data_input, data_expect, title", login_data)
    def test_login(self, get_url, data_input, data_expect, title):
        # 发送请求
        r = self.base_api.login_api(get_url,
                                    data_input['username'],
                                    data_input['password'])
        status_code = r.get('status_code')
        response = r.get('response_body')
        self.CA.assert_code(status_code, 200)
        self.CA.assertEqual(response['code'], data_expect['code'])
        if response['code'] == '0':
            self.CA.assertIn(data_expect['data'], response['data']['msg'])
        else:
            self.CA.assertIn(data_expect['data'], response['data'])



