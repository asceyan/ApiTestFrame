# -*- coding: utf-8 -*-
# @ Time: 2020/11/26 10:33
# @ Author: YanZhiJia
# @ Email: asce_yan@foxmail.com
# @ File: com_faker
# @ Description: 构造常用测试数据
from faker import Faker


class FakeData:

    def __init__(self):
        self.fake = Faker(locale='zh_CN')

    def get_name(self):
        """随机姓名"""
        return self.fake.name()

    def get_username(self):
        """随机用户名"""
        return self.fake.user_name()

    def get_password(self):
        """随机用户名"""
        return self.fake.password()

    def get_address(self):
        """随机地址"""
        return self.fake.address()

    def get_idcard(self):
        """随机身份证号"""
        return self.fake.ssn()

    def get_number(self):
        """随机手机号"""
        return self.fake.phone_number()

    def get_email(self):
        """随机邮箱"""
        return self.fake.email()

    def get_ipv4(self):
        """随机ipv4地址"""
        return self.fake.ipv4()

    def get_ipv6(self):
        """随机IP6地址"""
        return self.fake.ipv6()

    def get_domain(self):
        """生成域名"""
        return self.fake.domain_name()

    def get_user_agent(self):
        """随机user_agent信息"""
        return self.fake.user_agent()

    def get_text(self):
        """随机生成一篇文章"""
        return self.fake.text()

    def get_random_int(self, min, max):
        """生成范围内整数"""
        return self.fake.random_int(min, max)

    def get_random_date(self):
        """生成随机日期"""
        return self.fake.date()

    def get_random_time(self):
        """生成随机日期 时间"""
        return self.fake.date_time()

    def get_pyiterable(self):
        """随机生成可迭代对象iterable"""
        return self.fake.pyiterable()

    def get_pydict(self):
        """随机生成字典"""
        return self.fake.pydict()

    def get_pylist(self):
        """随机生成列表"""
        return self.fake.pylist()

    def get_pyset(self):
        """随机生成集合"""
        return self.fake.pyset()


if __name__ == '__main__':
    print(FakeData().get_user_agent())



