# -*- coding: utf-8 -*-
import json

import jsonpath as jsonpath
import requests as requests
from utils.aes_ecb_utils import AESCipher
from utils.jsonpath_utils import JsonPathUtils
from utils.random_pro_utils import RandomData


class TestApi:

    def setup_class(self):
        # 将secret_key 定义为类的属性
        self.secret_key = "r4JEOfsc2CxibxOjNFqBpg=="
        """获取token"""
        headers = {"Content-Type": "application/json"}
        data = {
            "appid": "gawd0ow1zes3",
            "secret": "f45638c7b5c145cb87030296cf3b5ac1"
        }
        url = "https://api.tgfun.com/openapi/v3/game/token"
        r = requests.request("POST", url, headers=headers, json=data)
        self.data = jsonpath.jsonpath(r.json(), "$.data")[0]
        # 解密
        decrypt_data = AESCipher.aes_decrypt(self.secret_key, self.data)
        # 将 JSON 数据转换为 Python 字典
        res_result = json.loads(decrypt_data)
        # 提取access_token
        self.access_token = res_result.get("access_token")
        # 玩家id
        self.player_id = RandomData.generate_player_id()
        # 玩家昵称
        self.player_name = RandomData.generate_player_name()
        # 游戏UUID
        self.gameUUID = "f731e5c36a234eee85ed9efe19a41193"
        # 上分
        self.coin = "1000000.65"
        # 下分
        self.coin_lower = "0.65"
        # 币种
        self.currency = "JPY"
        # 游戏玩家登录游戏时的语言
        self.gameLang = "pt"
        # 域名
        self.url = "https://api.tgfun.com/"

    def test_register(self):
        """玩家注册账号"""
        headers = {"Content-Type": "application/json", "Authorization": f"{self.access_token}"}
        req_data = {
            "playerID": self.player_id,
            "playerName": self.player_name,
            "currency": self.currency
        }
        # 转换为 JSON 字符串
        data_string = json.dumps(req_data)
        # 加密
        encrypt_data = AESCipher.aes_encrypt(self.secret_key, data_string)
        # 加密后入参
        data = {
            "data": f"{encrypt_data}"
        }
        url = self.url + f"openapi/v3/game/create/player"
        r = requests.request("POST", url, headers=headers, json=data)
        assert r.json()["code"] == "000000"
        print(r.text)

    def test_gamers_score_higher(self):
        """游戏玩家上分"""
        headers = {"Content-Type": "application/json", "Authorization": f"{self.access_token}"}
        req_data = {
            "payID": "79d6ac30803b4da19b080dccf6de9cd9",
            "playerID": self.player_id,
            "coin": self.coin,
            "currency": self.currency
        }
        # 转换为 JSON 字符串
        data_string = json.dumps(req_data)
        # 加密
        encrypt_data = AESCipher.aes_encrypt(self.secret_key, data_string)
        # 加密后入参
        data = {
            "data": f"{encrypt_data}"
        }
        url = self.url + f"openapi/v3/game/transfer/in"
        r = requests.request("POST", url, headers=headers, json=data)
        print(r.text)

    def test_game_score_divided(self):
        """"游戏玩家下分"""
        headers = {"Content-Type": "application/json", "Authorization": f"{self.access_token}"}
        req_data = {
            "payID": "79d6ac30803b4da19b080dccf6de9cd9",
            "playerID": self.player_id,
            "coin": self.coin_lower,
            "outall": "false",
            "currency": self.currency
        }
        # 转换为 JSON 字符串
        data_string = json.dumps(req_data)
        # 加密
        encrypt_data = AESCipher.aes_encrypt(self.secret_key, data_string)
        # 加密后入参
        data = {
            "data": f"{encrypt_data}"
        }
        url = self.url + f"openapi/v3/game/transfer/out"
        r = requests.request("POST", url, headers=headers, json=data)
        print(r.text)

    def test_get_game_address(self):
        """获取游戏地址"""
        headers = {"Content-Type": "application/json", "Authorization": f"{self.access_token}"}
        req_data = {
            "playerID": self.player_id,
            "gameUUID": self.gameUUID,
            "gameLang": self.gameLang
        }
        # 转换为 JSON 字符串
        data_string = json.dumps(req_data)
        # 加密
        encrypt_data = AESCipher.aes_encrypt(self.secret_key, data_string)
        # 加密后入参
        data = {
            "data": f"{encrypt_data}"
        }
        url = self.url + f"openapi/v3/game/create/url"
        r = requests.request("POST", url, headers=headers, json=data)
        # 使用 json() 方法解析响应数据,会将响应体转换为 Python 字典,确保接口返回的是有效的 JSON 格式
        response_json = r.json()
        # 使用 get() 方法访问 data 字段
        res_encrypt_data = response_json.get("data")
        # 解密
        decrypt_data = AESCipher.aes_decrypt(self.secret_key, res_encrypt_data)
        print(decrypt_data)
        # 将 JSON 字符串转换为字典
        # data_dict = json.loads(decrypt_data)
        # url = data_dict.get("url")
        # print(url)

    def test_player_betting_game_records(self):
        """获取游戏玩家下注游戏记录明细"""
        headers = {"Content-Type": "application/json", "Authorization": f"{self.access_token}"}
        req_data = {
            "page": 1,
            "size": 10,
            "playerID": self.player_id,
            "gameLang": self.gameLang,
            "gameUUID": self.gameUUID,
            "startDate": "2024-11-06 00:00:00",
            "endDate": "2024-12-31 23:59:59"
        }
        # 转换为 JSON 字符串
        data_string = json.dumps(req_data)
        # 加密
        encrypt_data = AESCipher.aes_encrypt(self.secret_key, data_string)
        # 加密后入参
        data = {
            "data": f"{encrypt_data}"
        }
        url = self.url + f"openapi/v3/game/player/detail/list"
        r = requests.request("POST", url, headers=headers, json=data)
        # 使用 json() 方法解析响应数据,会将响应体转换为 Python 字典,确保接口返回的是有效的 JSON 格式
        response_json = r.json()
        # 使用 get() 方法访问 data 字段
        res_encrypt_data = response_json.get("data")
        # 解密
        decrypt_data = AESCipher.aes_decrypt(self.secret_key, res_encrypt_data)
        print(decrypt_data)

    def test_get_player_balance(self):
        """获取游戏玩家的实时余额"""
        headers = {"Content-Type": "application/json", "Authorization": f"{self.access_token}"}
        req_data = {
            "playerID": self.player_id
        }
        # 转换为 JSON 字符串
        data_string = json.dumps(req_data)
        # 加密
        encrypt_data = AESCipher.aes_encrypt(self.secret_key, data_string)
        # 加密后入参
        data = {
            "data": f"{encrypt_data}"
        }
        url = self.url + f"openapi/v3/game/player/balance"
        r = requests.request("POST", url, headers=headers, json=data)
        # code = jsonpath.jsonpath(r.json(), "$.code")[0]
        # assert code == "000000"
        print(r.text)
