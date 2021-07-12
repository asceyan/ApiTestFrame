import json
import allure
from common.http_request import Request
from common.logger import Logger


logger = Logger('APIBase').get_log()


# 自定义日志装饰器，主要记录方法执行顺序
def mylogger(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'info':
                logger.info(f'Method [{func.__name__}] is running !')
            elif level == 'error':
                logger.error(f'Method [{func.__name__}] runs error !')
            return func(*args, **kwargs)
        return wrapper
    return decorator


class APIBase:
    """
        定义测试接口的基类，封装接口的入参和出参
    """

    def __init__(self):
        self.re = Request()

    @mylogger("info")
    @allure.step('登陆case')
    def login_api(self, host, username='', password=''):
        uri = '/login'
        url = host + uri
        body = {
            "username": username,
            "password": password,
        }
        h = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        r = self.re.post_request(url, data=body, headers=h)
        return r

    @mylogger("info")
    @allure.step('获取url')
    def get_url_api(self, host, uid='1'):
        uri = '/test_url'
        url = host + uri
        body = {
            "id": uid
        }
        r = self.re.get_requests(url, data=body)
        return r


if __name__ == '__main__':
    host = 'http://47.96.25.229:7300/mock/60e29c972b9d72001731a419/mymock'
    api = APIBase()
    r = api.login_api(host, 'admin', '123456')
    print(r)