# -*- coding: utf-8 -*-
import allure
import jsonpath as jsonpath
import requests as requests

from utils.random_data_utils import RandomData


@allure.feature("TgFun商户接入Api")
class TestApi:
    def setup_class(self):
        """获取token"""
        headers = {"Content-Type": "application/json"}
        data = {
            "grant_type": "client_credential",
            "appid": "ga6as02niqmb",
            "secret": "105599370e0a4b718d73938d1ea99336"
        }
        url = "https://api.tgfun.io/openapi/open/game/token/get"
        r = requests.request("GET", url, headers=headers, params=data)
        # print(r.text)
        self.token = jsonpath.jsonpath(r.json(), "$.access_token")[0]
        # 玩家id
        self.player_id = RandomData.generate_unique_player_id()
        # 玩家昵称
        self.player_name = RandomData.generate_unique_player_name()
        # 游戏UUID
        self.gameUUID = "50f2cc12601d49c18f8b8af5964030b5"
        # 上分
        self.coin = "100000.65"
        # 下分
        self.coin_lower = "0.65"
        # 币种
        self.currency = "CNY"
        # 游戏玩家登录游戏时的语言
        self.gameLang = "zh-CN"
        # 域名
        self.url = "https://api.tgfun.io/"

    @allure.story("TgFun注册测试用例")
    @allure.title("商户注册")
    @allure.severity('normal')
    @allure.description("商户注册")
    def test_register(self):
        """玩家注册账号"""
        headers = {"Content-Type": "application/json"}
        data = {
            "playerID": self.player_id,
            "playerName": self.player_name,
            "currency": self.currency
        }
        url = self.url + f"openapi/open/game/create/player?access_token={self.token}"
        r = requests.request("POST", url, headers=headers, json=data)
        print(r.text)

    @allure.story("TgFun游戏玩家上分测试用例")
    @allure.title("游戏玩家上分")
    @allure.severity('normal')
    @allure.description("游戏玩家上分")
    def test_gamers_score_higher(self):
        """游戏玩家上分"""
        headers = {"Content-Type": "application/json"}
        data = {
            "payID": "79d6ac30803b4da19b080dccf6de9cd9",
            "playerID": self.player_id,
            "coin": self.coin,
            "currency": self.currency
        }
        # data = {
        #     "payID": "79d6ac30803b4da19b080dccf6de9cd9",
        #     "playerID": 2855487457584211,
        #     "coin": 10000,
        #     "currency": "USD"
        # }
        url = self.url + f"openapi/open/game/transfer/in?access_token={self.token}"
        r = requests.request("POST", url, headers=headers, json=data)
        print(r.text)

    @allure.story("TgFun游戏玩家下分测试用例")
    @allure.title("游戏玩家下分")
    @allure.severity('normal')
    @allure.description("游戏玩家下分")
    def test_game_score_divided(self):
        """"游戏玩家下分"""
        headers = {"Content-Type": "application/json"}
        data = {
            "payID": "79d6ac30803b4da19b080dccf6de9cd9",
            "playerID": self.player_id,
            "coin": self.coin_lower,
            "outall": "false",
            "currency": self.currency
        }
        url = self.url + f"openapi/open/game/transfer/out?access_token={self.token}"
        r = requests.request("POST", url, headers=headers, json=data)
        print(r.text)

    @allure.story("TgFun获取游戏地址测试用例")
    @allure.title("获取游戏地址")
    @allure.severity('normal')
    @allure.description("获取游戏地址")
    def test_get_game_address(self):
        """获取游戏地址"""
        headers = {"Content-Type": "application/json"}
        data = {
            "playerID": self.player_id,
            "gameUUID": self.gameUUID,
            "gameLang": self.gameLang
        }
        url = self.url + f"openapi/open/game/get/url?access_token={self.token}"
        r = requests.request("POST", url, headers=headers, json=data)
        print(r.text)

    @allure.story("TgFun获取游戏玩家下注游戏记录明细测试用例")
    @allure.title("获取游戏玩家下注游戏记录明细")
    @allure.severity('normal')
    @allure.description("获取游戏玩家下注游戏记录明细")
    def test_player_betting_game_records(self):
        """获取游戏玩家下注游戏记录明细"""
        headers = {"Content-Type": "application/json"}
        data = {
            "page": 1,
            "size": 10,
            "playerID": self.player_id,
            "gameLang": self.gameLang,
            "gameUUID": self.gameUUID,
            "startDate": "2024-11-05 00:00:00",
            "endDate": "2024-12-31 23:59:59"
        }
        url = self.url + f"openapi/open/game/player/detail/list?access_token={self.token}"
        r = requests.request("POST", url, headers=headers, json=data)
        print(r.text)

    @allure.story("TgFun获取游戏玩家的实时余额测试用例")
    @allure.title("获取游戏玩家的实时余额")
    @allure.severity('normal')
    @allure.description("获取游戏玩家的实时余额")
    def test_get_player_balance(self):
        """获取游戏玩家的实时余额"""
        headers = {"Content-Type": "application/json"}
        data = {
            "playerID": self.player_id
        }
        url = self.url + f"openapi/open/game/score/get?access_token={self.token}"
        r = requests.request("POST", url, headers=headers, json=data)
        print(r.text)
