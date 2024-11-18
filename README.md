# TGFUN商户上线接入API
这是一个用于接口自动化测试的框架，使用python+requests+pytest+yaml+allure框架搭建，旨在提高 API 测试的效率和可靠性。

## 目录
- [背景](#背景)
- [功能](#功能)
- [安装](#安装)
- [使用](#使用)
## 背景
随着公司项目的不断增大，客户数量的增多，回归的任务量越来越大，需要对接口进行定时回归测试来保证接口的稳定性。
## 功能
- 支持多种 API 测试方式（GET、POST、PUT、DELETE 等）。
- 支持 JSON 和 XML 格式的数据。
- 集成了常用的库（如 `requests` 或 `pytest`）。
- 可以生成测试报告。
- 具备环境管理功能（如测试环境、开发环境等）。
## 安装
## 克隆项目
git clone https://github.com/hypercarbon/gamebox-merchant-api.git
## 进入项目目录
cd gamebox-merchant-api
## 安装依赖
pip install -r requirements.txt
## 使用
运行所有测试：Terminal下输入pytest即可
## 指定运行某个测试文件
pytest .\test_v2_api.py