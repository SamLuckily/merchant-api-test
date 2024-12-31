# -*- coding: utf-8 -*-
import pymysql

from utils.log_utils import logger


class Database:
    """
    链接数据库之增删改查
    """
    database_info = {
        'host': '47.130.39.54',
        'user': 'ylgame',
        'password': 'mhSBhmHBEdpi3hXf',
        'db': 'ylgame',
        'port': 3306,
        'charset': 'utf8mb4'
    }

    @classmethod
    def query_db(cls, sql, database_info=None):
        """
        链接数据库，执行对应的sql语句，获得执行结果
        :param sql: 要执行的sql语句
        :param database_info: 数据库配置信息
        :return:
        """
        # 如果没有提供数据库信息，使用默认信息
        if database_info is None:
            database_info = cls.database_info
        # 连接数据库
        try:
            conn = pymysql.Connect(**database_info)
            logger.info("数据库连接成功")
        except pymysql.MySQLError as e:
            logger.error(f"数据库连接失败：{e}")
            return None
        # 创建游标
        cursor = conn.cursor()
        logger.info(f"创建的游标为 {cursor}")
        logger.info(f"要执行的sql语句为 {sql}")
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 获取查询结果
            datas = cursor.fetchall()
            logger.info(f"执行结果数据为 {datas}")
        except pymysql.MySQLError as e:
            logger.error(f"SQL执行失败：{e}")
            return None
        # 关闭连接
        cursor.close()
        conn.close()
        return datas



