# -*- coding: utf-8 -*-
# @ Time: 2021/3/9 14:46
# @ Author: YanZhiJia
# @ Email: asce_yan@foxmail.com
# @ File: run_allure
# @ Description: 项目执行文件
import os
import time
import pytest

from common.report import Report

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
REPORT_PATH = os.path.join(BASE_PATH, 'report')


report = Report()


class Run:
    def __init__(self):
        self.allure_result = os.path.join(REPORT_PATH, 'allure_result')
        self.allure_report = os.path.join(REPORT_PATH, 'allure_report')

    def run_case(self):
        # 执行测试
        args = ['-s', "--alluredir", f"{self.allure_result}"]
        pytest.main(args)
        # 生成测试报告
        cmd = f"{report.allure} generate {self.allure_result} -o {self.allure_report} --clean"
        print(os.popen(cmd).read())


if __name__ == '__main__':
    run = Run()
    run.run_case()