# -*- coding: utf-8 -*-
# @ Time: 2021/2/8 16:22
# @ Author: YanZhiJia
# @ Email: asce_yan@foxmail.com
# @ File: com_assert
# @ Description: 封装断言方法
from common.logger import Logger
logger = Logger('Assert').get_log()


class Assert(object):
    def assertEqual(self, first, second):
        try:
            assert first == second
            return True
        except AssertionError as e:
            logger.error(f"AssertionError, expected result:[{first}=={second}]，"
                         f"actual result:[{first} != {second}]")
            raise e

    def assertNotEqual(self, first, second):
        try:
            assert first != second
            return True
        except AssertionError as e:
            logger.error(f"AssertionError, expected result:[{first} != {second}], "
                         f"actual result:[first={first},second={second}]")
            raise (e)

    def assertTrue(self, expr):
        try:
            assert expr is True
            return True
        except AssertionError as e:
            logger.error(f"AssertionError, actual result:[{expr} is not true] ")
            raise e

    def assertFalse(self, expr):
        try:
            assert expr is False
            return True
        except AssertionError as e:
            logger.error(f"AssertionError, actual result:[{expr} is not false] ")
            raise e

    def assertIn(self, first, second):
        try:
            assert str(first) in str(second)
            return True
        except AssertionError as e:
            logger.error(f"AssertionError, expected result:[{first} is in {second}], "
                         f"actual result:[first={first},second={second}]")
            raise e

    def assertNotIn(self, first, second):
        try:
            assert str(first) not in str(second)
            return True
        except AssertionError as e:
            logger.error(f"AssertionError, expected result:[{first} is not in {second}], "
                         f"actual result:[first={first},second={second}]")
            raise e

    def assertIsNone(self, expr=None):
        try:
            assert expr is None
            return True
        except AssertionError as e:
            logger.error(f"AssertionError, expected result:[{expr} is None], "
                         f"actual result:[expr={expr}]")
            raise e

    def assertIsNotNone(self, expr=None):
        try:
            assert expr is not None
            return True
        except AssertionError as e:
            logger.error(f"AssertionError, expected result:[{expr} is not None], "
                         f"actual result:[expr={expr}]")
            raise e

    def assert_code(self, status_code, expect):
        """
        判断response.status_code是否如预期
        :param expect:
        :param status_code:
        :return:
        """
        # 判断expect 是否为string类型；如果是，转换expect为int类型
        if isinstance(expect, str):
            expect = int(expect)
        try:
            return self.assertEqual(status_code, expect)
        except Exception as e:
            logger.error(f"AssertionError, expected result:[{expect}], "
                         f"actual result:[status_code={status_code}]")
            raise e

    @staticmethod
    def assert_dict_content(expect: dict, actual: dict):
        """当接口返回数据比较多时，使用字典expect接收返回参数，然后直接对比字典的value"""
        result = None
        for key in expect.keys():
            if (key in actual) and (expect[key] == actual[key]):
                result = True
            else:
                result = False
        return result

