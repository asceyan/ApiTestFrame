# ApiTestFrame框架介绍

### 简介

本框架为接口测试自动化框架，基于Python3+requests+pytest+allure组成

### 目录结构

| 项目结构    | 说明                                         |
| :---------- | :------------------------------------------- |
| case        | 用例层，存放测试用例                         |
| common      | 公共层，负责底层封装                         |
| config      | 配置层，存放配置文件，如项目地址、邮件地址等 |
| data        | 存放测试数据                                 |
| lib         | 存放第三方库，如allure库                     |
| log         | 存放项目日志                                 |
| report      | 存放allure报告                               |
| conftest.py | 负责编写用例fixture                          |
| pytest.ini  | pytest 的配置文件                            |
| run.py      | 执行测试文件                                 |

### 快速上手

- 从远程仓库拉取代码

`git clone https://github.com/asceyan/ApiTestFrame.git`

- 安装依赖包

```pip3 install -r requirements.txt -i https://pypi.douban.com/simple```

#### 编写用例

查看case目录下用例示例

- `test_url.py`普通用例编写示例

- `test_login.py`实现测试用例参数化示例

#### 运行用例

- 执行项目根目录下的run.py文件，执行全部测试用例

- 执行结束后，在report\allure_report目录下查看测试报告

- 在命令行中使用指令`pytest -s --env test --alluredir ./report/allure_result --clean`

  - 参数说明：
    - --env：自定义参数，可一键修改测试环境地址
    - --alluredir： 设置生成allure数据的路径

#### 报告展示

查看report/allure_report目录下`index.html`文件


