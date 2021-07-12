# -*- coding: utf-8 -*-
# @ Time: 2021/2/8 16:22
# @ Author: YanZhiJia
# @ Email: asce_yan@foxmail.com
# @ File: http_request.py
# @ Description: 封装requests请求方法

import os
import random
import requests
import urllib3
from common.faker_data import FakeData
from common.logger import Logger
from requests_toolbelt import MultipartEncoder

logger = Logger('Request').get_log()
# 忽略InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Request:
    def __init__(self):
        self.s = requests.Session()
        # 模拟真机发送请求
        headers = {"User-Agent": FakeData().get_user_agent()}
        self.s.headers.update(headers)

    def get_requests(self, url='', data=None, headers=None, verify=False):
        """封装http get请求"""
        try:
            if data is None:
                r = self.s.get(url=url, headers=headers, verify=verify)
                logger.info(f'Request sent successfully, method:[get], url:[{url}], headers:{headers}, data:None')
            else:
                r = self.s.get(url=url, params=data, headers=headers, verify=verify)
                logger.info(f'Request sent successfully, method:[get], url:[{url}], headers:{headers}, data:{data}')

        except requests.RequestException as e:
            logger.error(f'RequestException:{e}, url:[{url}]')
            raise e

        response = dict()
        response['status_code'] = r.status_code
        try:
            response['response_body'] = r.json()
        except Exception as e:
            print(e)
            response['response_body'] = r.text
        response['elapsed_time'] = r.elapsed.total_seconds()
        logger.info(f"Interface response successful, response message:{response}")
        return response

    def post_request(self, url='', data=None, json=None, headers=None, verify=False):
        """封装http post请求"""
        try:
            if json is not None:
                r = self.s.post(url, json=json, headers=headers, verify=verify)
                logger.info(f'Request sent successfully, method:[post], url:[{url}], headers:{headers}, json:{json}')
            elif data is not None:
                r = self.s.post(url, data=data, headers=headers, verify=verify)
                logger.info(f'Request sent successfully, method:[post], url:[{url}], headers:{headers}, data:{data}')
            else:
                r = self.s.post(url=url, headers=headers)
                logger.info(f'Request sent successfully, method:[post], url:[url], headers:{headers}, data:None')

        except requests.RequestException as e:
            logger.error(f'RequestException:{e}, url:[{url}]')
            raise e
        response = dict()
        response['status_code'] = r.status_code
        try:
            response['response_body'] = r.json()
        except Exception as e:
            print(e)
            response['response_body'] = r.text
        response['elapsed_time'] = r.elapsed.total_seconds()
        logger.info(f"Interface response successful, response message:{response}")
        return response

    def post_request_multipart(self, url='', data=None, headers=None,
                               file_parm=None, file=None, f_type=None, verify=False):
        """
        提交Multipart/form-data 格式的Post请求
        实例：m = MultipartEncoder(fields={'a':'1','b':'2','file_parm' :('filename',open('filename','rb'),'image/png')})
        r = requests.post(url,data=m,headers={'Content-Type':m.content_type})
        :param url: URL地址
        :param data: 接口参数
        :param headers: 接口头部参数
        :param file_parm: 上传文件接口的参数名
        :param file: 上传文件名称
        :param f_type: 上传文件类型
        :return: response
        """
        try:
            if data is None:
                r = self.post_request(url, headers=headers)
                logger.info(f'Request sent successfully！, method:post, url:{url}, headers:{headers}, data:None')
            else:
                data[file_parm] = os.path.basename(file), open(file, 'rb'), f_type
                m = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )
                headers['Content-Type'] = m.content_type
                r = self.s.post(url=url, data=m, headers=headers, verify=verify)
                logger.info(f'Request sent successfully, method:post, url:{url}, headers:{headers}, data:{m}')

        except requests.RequestException as e:
            logger.error(f'RequestException:{e}, url:[{url}]')
            raise e

        response = dict()
        response['status_code'] = r.status_code
        try:
            response['response_body'] = r.json()
        except Exception as e:
            print(e)
            response['response_body'] = r.text
        response['elapsed_time'] = r.elapsed.total_seconds()
        logger.info(f"Interface response successful！, response message:{response}")
        return response

    def put_request(self, url, data=None, headers=None, verify=False):
        try:
            if not data:
                r = self.s.put(url=url, headers=headers, verify=verify)
                logger.info(f'Request sent successfully, method:[put], url:[{url}], headers:{headers}, data:None')
            else:

                r = self.s.put(url, data=data, headers=headers, verify=verify)
                logger.info(f'Request sent successfully, method:[put], url:[{url}], headers:{headers}, data:{data}')
        except requests.RequestException as e:
            logger.error(f'RequestException:{e}, url:[{url}]')
            raise e
        response = dict()
        response['status_code'] = r.status_code
        try:
            response['response_body'] = r.json()
        except Exception as e:
            response['response_body'] = r.text
            print(e)
        response['elapsed_time'] = r.elapsed.total_seconds()
        logger.info(f"Interface response successful, response message:{response}")
        return response

    def del_requests(self, url, data=None, headers=None, verify=False):
        try:
            if not data:
                r = self.s.delete(url=url, headers=headers, verify=verify)
                logger.info(f'Request sent successfully, method:[delete], url:[{url}], headers:{headers}, data:None')
            else:

                r = self.s.delete(url, data=data, headers=headers, verify=verify)
                logger.info(f'Request sent successfully, method:[delete], url:[{url}], headers:{headers}, data:{data}')
        except requests.RequestException as e:
            logger.error(f'RequestException:{e}, url:[{url}]')
            raise e
        response = dict()
        response['status_code'] = r.status_code
        try:
            response['response_body'] = r.json()
        except Exception as e:
            response['response_body'] = r.text
            print(e)
        response['elapsed_time'] = r.elapsed.total_seconds()
        logger.info(f"Interface response successful, response message:{response}")
        return response

