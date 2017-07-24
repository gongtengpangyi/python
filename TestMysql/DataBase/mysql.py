import pymysql
from TestMysql import setting


class Mysql:
    def __init__(self):
        self.__db_info = setting.DATABASE_SETTING
        self.__db = pymysql.connect(self.__db_info.get('ip'), self.__db_info.get('user'),
                                    self.__db_info.get('password'), self.__db_info.get('database'))

    # def connect(self):
    #     self.__db.connect()
    #
    # def close(self):
    #     self.__db.close()

    # 插入数据
    # table 表名
    # params 参数键值对
    def insert(self, table, params):
        cursor = self.__db.cursor()
        sql1 = 'insert into ' + table + '('
        sql2 = ' VALUES ('
        for key in params.keys():
            sql1 = sql1 + key + ', '
            sql2 += '%s, '
        sql = sql1[:-2] + ')' + sql2[:-2] + ');'
        print(sql)
        print(tuple(params.values()))
        cursor.execute(sql, tuple(params.values()))
        self.__db.commit()

    # 删除数据
    # table 表名
    # params 参数键值对
    def delete(self, table, params):
        cursor = self.__db.cursor()
        sql = 'delete from ' + table + Mysql.sql_where(params.keys()) + ';'
        print(sql)
        cursor.execute(sql, tuple(params.values()))
        self.__db.commit()

    # 更新数据
    # table 表名
    # params 参数键值对
    # where_params 条件参数键值对
    def update(self, table, params, where_params):
        cursor = self.__db.cursor()
        sql = 'update ' + table + ' set'
        for key in params.keys():
            sql = sql + ' ' + key + ' = %s and'
        sql = sql[:-3] + Mysql.sql_where(where_params.keys()) + ';'
        print(sql)
        print(tuple(params.values()) + tuple(where_params.values()))
        cursor.execute(sql, tuple(params.values()) + tuple(where_params.values()))
        self.__db.commit()

    # 更新数据
    # table 表名
    # keys 返回参数列表
    # params 参数键值对
    def select(self, table, keys, params):
        cursor = self.__db.cursor()
        sql = 'select'
        for key in keys:
            sql += ' ' + key + ','
        sql = sql[:-1] + ' from ' + table + Mysql.sql_where(params.keys()) + ';'
        print(sql)
        cursor.execute(sql, tuple(params.values()))
        return cursor.fetchall()

    # 组成where语句
    # keys 键列表
    # return 生成的sql语句片段
    @staticmethod
    def sql_where(keys):
        sql = ' where'
        for key in keys:
            sql += ' ' + key + ' = %s and'
        return sql[:-3]
