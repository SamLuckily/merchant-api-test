# -*- coding: utf-8 -*-
import json
from datetime import datetime

from api.BaseApi import BaseApi
from utils.aes_ecb_utils import AESCipher


class TgApi(BaseApi):
    """
    TgApi接口
    """

    def __init__(self):
        # 将 secret_key 定义为类的属性
        self.secret_key = "RYMlMnFa+P60wT3Z8LVHdg=="

    def user_register(self, player_id, player_name, currency):
        """注册用户"""
        req_data = {
            "playerID": player_id,
            "playerName": player_name,
            "currency": currency
        }
        # 转换为 JSON 字符串
        data_string = json.dumps(req_data)
        # 加密
        encrypt_data = AESCipher.aes_encrypt(self.secret_key, data_string)
        # 加密后入参
        data = {
            "data": f"{encrypt_data}"
        }
        path = "openapi/v3/game/create/player"
        return self.send("POST", path, json=data)

    def score_higher(self, payID, playerID, coin, currency):
        """游戏玩家上分"""
        req_data = {
            "payID": payID,
            "playerID": playerID,
            "coin": coin,
            "currency": currency
        }
        # 转换为 JSON 字符串
        data_string = json.dumps(req_data)
        # 加密
        encrypt_data = AESCipher.aes_encrypt(self.secret_key, data_string)
        # 加密后入参
        data = {
            "data": f"{encrypt_data}"
        }
        path = "openapi/v3/game/transfer/in"
        return self.send("POST", path, json=data)

    def score_divided(self, payID, playerID, coin, outall, currency):
        """游戏玩家下分"""
        req_data = {
            "payID": payID,
            "playerID": playerID,
            "coin": coin,
            "outall": outall,
            "currency": currency
        }
        # 转换为 JSON 字符串
        data_string = json.dumps(req_data)
        # 加密
        encrypt_data = AESCipher.aes_encrypt(self.secret_key, data_string)
        # 加密后入参
        data = {
            "data": f"{encrypt_data}"
        }
        path = "openapi/v3/game/transfer/out"
        return self.send("POST", path, json=data)

    def get_game_address(self, playerID, gameUUID, gameLang):
        """获取游戏地址"""
        req_data = {
            "playerID": playerID,
            "gameUUID": gameUUID,
            "gameLang": gameLang
        }
        # 转换为 JSON 字符串
        data_string = json.dumps(req_data)
        # 加密
        encrypt_data = AESCipher.aes_encrypt(self.secret_key, data_string)
        # 加密后入参
        data = {
            "data": f"{encrypt_data}"
        }
        path = "openapi/v3/game/create/url"
        return self.send("POST", path, json=data)

    def query_betting_records(self, page, size, playerID, gameLang, gameUUID, startDate, endDate):
        """查询下注记录明细"""
        # 将 datetime 对象转换为字符串
        if isinstance(startDate, datetime):
            startDate = startDate.strftime('%Y-%m-%d %H:%M:%S')  # 格式化为指定字符串
        if isinstance(endDate, datetime):
            endDate = endDate.strftime('%Y-%m-%d %H:%M:%S')  # 格式化为指定字符串
        req_data = {
            "page": page,
            "size": size,
            "playerID": playerID,
            "gameLang": gameLang,
            "gameUUID": gameUUID,
            "startDate": startDate,
            "endDate": endDate
        }
        # 转换为 JSON 字符串
        data_string = json.dumps(req_data)
        # 加密
        encrypt_data = AESCipher.aes_encrypt(self.secret_key, data_string)
        # 加密后入参
        data = {
            "data": f"{encrypt_data}"
        }
        path = "openapi/v3/game/player/detail/list"
        return self.send("POST", path, json=data)

    def check_player_balance(self, playerID):
        """查询玩家余额"""
        req_data = {
            "playerID": playerID
        }
        # 转换为 JSON 字符串
        data_string = json.dumps(req_data)
        # 加密
        encrypt_data = AESCipher.aes_encrypt(self.secret_key, data_string)
        # 加密后入参
        data = {
            "data": f"{encrypt_data}"
        }
        path = "openapi/v3/game/player/balance"
        return self.send("POST", path, json=data)
