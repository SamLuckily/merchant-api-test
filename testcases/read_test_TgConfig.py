# -*- coding: utf-8 -*-
from config.TgConfig import TgConfig

tg_config = TgConfig()


def test_base_url():
    """
    验证@property装饰器
    :return:
    """
    print(tg_config.base_url)
    print(tg_config.appid)
    print(tg_config.secret)
    print(tg_config.secret_key)
