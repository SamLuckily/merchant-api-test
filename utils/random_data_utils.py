# -*- coding: utf-8 -*-
import random
import string

from utils.database_utils import Database


class RandomData:
    """
    生成随机数据工具
    """

    @classmethod
    def check_player_id_exists(cls, player_id):
        """检查 player_id 是否存在于数据库中"""
        sql = f"SELECT COUNT(*) FROM box_player WHERE PlayerID = '{player_id}';"  # 替换为实际的查询
        result = Database.query_db(sql)
        return result and result[0][0] > 0  # 返回 True 如果存在，返回 False 否则

    @classmethod
    def check_player_name_exists(cls, player_name):
        """检查 player_name 是否存在于数据库中"""
        sql = f"SELECT COUNT(*) FROM box_player WHERE PlayerName = '{player_name}';"  # 替换为实际的查询
        result = Database.query_db(sql)
        return result and result[0][0] > 0  # 返回 True 如果存在，返回 False 否则

    @classmethod
    def generate_unique_player_id(cls):
        """生成唯一的 player_id"""
        while True:
            player_id = cls.generate_player_id()
            if not cls.check_player_id_exists(player_id):
                return player_id  # 返回唯一的 player_id

    @classmethod
    def generate_unique_player_name(cls):
        """生成唯一的 player_name"""
        while True:
            player_name = cls.generate_player_name()
            if not cls.check_player_name_exists(player_name):
                return player_name  # 返回唯一的 player_name

    sql = "SELECT * FROM box_player LIMIT 1;"
    result = Database.query_db(sql)

    @classmethod
    def generate_player_id(cls):
        """生成6位随机数"""
        return f"{random.randint(100000, 999999)}"

    @classmethod
    def generate_player_name(cls):
        """生成随机字符，包括随机的小写和大写字母8位字符"""
        random_suffix = ''.join(random.choices(string.ascii_letters, k=8))  # 生成5个随机大小写字母
        return f"{random_suffix}"  # 组合成新的 playerName
