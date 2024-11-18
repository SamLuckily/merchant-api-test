# -*- coding: utf-8 -*-
import pytest
from api.TgfunApi import TgApi
from testcases.conftest import get_data
from utils.aes_ecb_utils import AESCipher
from utils.random_data_utils import RandomData
import allure


@allure.feature("TgFun商户接入Api")
class TestApi:

    def setup_class(self):
        self.tg_api = TgApi()
        # 玩家id
        self.player_id = RandomData.generate_unique_player_id()
        # 玩家昵称
        self.player_name = RandomData.generate_unique_player_name()
        # V3密钥
        self.secret_key = "6CANzZfmtR7jvbGCtA35yw=="

    @allure.story("TgFun商户注册测试用例")
    @allure.title("商户注册")
    @allure.severity('normal')
    @allure.description("商户注册")
    @pytest.mark.parametrize("data", get_data()['user_register'])
    def test_register(self, data):
        """商户注册账号"""
        # # 玩家id
        # self.player_id = RandomData.generate_unique_player_id()
        # # 玩家昵称
        # self.player_name = RandomData.generate_unique_player_name()
        # 注册用户
        r = self.tg_api.user_register(self.player_id, self.player_name, data["currency"])
        # 断言
        assert r.get("code") == "000000"

    @allure.story("TgFun游戏玩家上分测试用例")
    @allure.title("游戏玩家上分")
    @allure.severity('normal')
    @allure.description("游戏玩家上分")
    @pytest.mark.parametrize("data", get_data()['score_higher'])
    def test_score_higher(self, data):
        """游戏玩家上分"""
        r = self.tg_api.score_higher(data["payID"], self.player_id, data["coin"], data["currency"])
        # 断言
        assert r.get("code") == "000000"

    @allure.story("TgFun游戏玩家下分测试用例")
    @allure.title("游戏玩家下分")
    @allure.severity('normal')
    @allure.description("游戏玩家下分")
    @pytest.mark.parametrize("data", get_data()['score_divided'])
    def test_score_divided(self, data):
        """游戏玩家下分"""
        r = self.tg_api.score_divided(data["payID"], self.player_id, data["coin"], data["outall"], data["currency"])
        # 断言
        assert r.get("code") == "000000"

    @allure.story("TgFun获取游戏地址测试用例")
    @allure.title("获取游戏地址")
    @allure.severity('normal')
    @allure.description("获取游戏地址")
    @pytest.mark.parametrize("data", get_data()['get_game_address'])
    def test_get_game_address(self, data):
        """获取游戏地址"""
        r = self.tg_api.get_game_address(self.player_id, data["gameUUID"], data["gameLang"])
        # 断言
        assert r.get("code") == "000000"
        # 使用 json() 方法解析响应数据,会将响应体转换为 Python 字典,确保接口返回的是有效的 JSON 格式
        response_json = r
        # 使用 get() 方法访问 data 字段
        res_encrypt_data = response_json.get("data")
        # 解密
        decrypt_data = AESCipher.aes_decrypt(self.secret_key, res_encrypt_data)
        print(decrypt_data)

    @allure.story("TgFun查询下注记录测试用例")
    @allure.title("查询下注记录")
    @allure.severity('normal')
    @allure.description("查询下注记录")
    @pytest.mark.parametrize("data", get_data()['query_betting_records'])
    def test_query_betting_records(self, data):
        """查询下注记录"""
        r = self.tg_api.query_betting_records(data["page"], data["size"], self.player_id, data["gameLang"],
                                              data["gameUUID"],
                                              data["startDate"], data["endDate"])
        # 断言
        assert r.get("code") == "000000"
        # 使用 json() 方法解析响应数据,会将响应体转换为 Python 字典,确保接口返回的是有效的 JSON 格式
        response_json = r
        # 使用 get() 方法访问 data 字段
        res_encrypt_data = response_json.get("data")
        # 解密
        decrypt_data = AESCipher.aes_decrypt(self.secret_key, res_encrypt_data)
        print(decrypt_data)

    @allure.story("TgFun查询玩家余额测试用例")
    @allure.title("查询玩家余额")
    @allure.severity('normal')
    @allure.description("查询玩家余额")
    def test_check_player_balance(self):
        """查询玩家余额"""
        r = self.tg_api.check_player_balance(self.player_id)
        # 断言
        assert r.get("code") == "000000"
