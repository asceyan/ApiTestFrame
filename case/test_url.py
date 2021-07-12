# -*- coding: utf-8 -*-
import allure
from common.api_base import APIBase
from common.com_assert import Assert


@allure.feature('TestURL')
class TestURL:
    def setup_class(self):
        self.CA = Assert()
        self.base_api = APIBase()

    @allure.story('获取url接口测试用例')
    @allure.title("参数id=1，获取淘宝url")
    def test_get_url_01(self, get_url):
        # 发送请求
        r = self.base_api.get_url_api(get_url, uid=1)
        status_code = r.get('status_code')
        response = r.get('response_body').get('requestDetail').get('url')
        self.CA.assert_code(status_code, 200)
        self.CA.assertEqual('http://www.taobao.com', response)

    @allure.story('获取url接口测试用例')
    @allure.title("参数id=2，获取百度url")
    def test_get_url_02(self, get_url):
        # 发送请求
        r = self.base_api.get_url_api(get_url, uid=2)
        status_code = r.get('status_code')
        response = r.get('response_body').get('requestDetail').get('url')
        self.CA.assert_code(status_code, 200)
        self.CA.assertEqual('http://www.baidu.com', response)

    @allure.story('获取url接口测试用例')
    @allure.title("参数id=3，获取bing的url")
    def test_get_url_03(self, get_url):
        # 发送请求
        r = self.base_api.get_url_api(get_url, uid=3)
        status_code = r.get('status_code')
        response = r.get('response_body').get('requestDetail').get('url')
        self.CA.assert_code(status_code, 200)
        self.CA.assertEqual('http://bing.com', response)






