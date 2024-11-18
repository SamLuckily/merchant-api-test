# -*- coding: utf-8 -*-
import json
import jsonpath
import requests
from config.TgConfig import TgConfig
from utils.aes_ecb_utils import AESCipher
from utils.log_utils import logger
from utils.read_utils import Utils


class BaseApi:
    def access_token(self):
        """
        获取token
        :return:
        """
        # 将secret_key 定义为类的属性
        secret_key = self.config().secret_key
        headers = {"Content-Type": "application/json"}
        req_data = {
            "appid": self.config().appid,
            "secret": self.config().secret
        }
        url = self.config().base_url + "openapi/v3/game/token"
        r = requests.request("POST", url, headers=headers, json=req_data)
        data = jsonpath.jsonpath(r.json(), "$.data")[0]
        # 解密
        decrypt_data = AESCipher.aes_decrypt(secret_key, data)
        # 将 JSON 数据转换为 Python 字典
        res_result = json.loads(decrypt_data)
        # 提取access_token
        access_token = res_result.get("access_token")
        return access_token

    def config(self) -> TgConfig:
        """
        获取配置
        :return:
        """
        return TgConfig()

    def get_token_by_file(self, key):
        """
        从文件读取配置信息
        :param key:
        :return:
        """
        # 拿到存放token的文件路径
        path = Utils.get_root_path()
        file_path = f'{path}/data/token.yaml'
        new_token = self.access_token()
        # 写入新数据
        token_data = {
            'access_token': new_token
        }
        Utils.add_yaml_data({key: token_data}, file_path)
        return new_token

    def send(self, method, url, **kwargs):
        """
        请求方法
        :return:
        """
        request_url = self.config().base_url + url
        headers = {"Authorization": self.get_token_by_file("contacts")}
        logger.info(f"发起的请求地址为===========>{request_url}")
        r = requests.request(method, request_url, headers=headers, timeout=5, **kwargs)  # 添加接口请求超时处理
        logger.info(f"接口的响应信息为<==========={r.text}")
        # 如果所有的接口都可以进行json序列化的话，就直接return r.json()即可
        return r.json()
