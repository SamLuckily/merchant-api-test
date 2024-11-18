# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import random
import string

from utils.database_utils import Database


class RandomData:
    """
    生成随机数据工具
    """

    @classmethod
    def generate_player_id(cls):
        """生成6位随机数"""
        return f"{random.randint(100000, 999999)}"

    @classmethod
    def generate_player_name(cls):
        """生成随机字符，包括随机的小写和大写字母8位字符"""
        random_suffix = ''.join(random.choices(string.ascii_letters, k=8))  # 生成5个随机大小写字母
        return f"{random_suffix}"  # 组合成新的 playerName
