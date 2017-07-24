import pymysql


def test():
    mysql = Mysql()
    # mysql.insert_admin('cwj', 'ssb')
    mysql.select_admin("' or '1'='1")

    # mysql.select_admin_sql_insert("'" + "' or '1'='1" + "'")


# 这是一个基本的测试类，测试pymysql执行基本的增加和查询的效果，作为demo而不作为最后的实际运行代码
class Mysql:
    # 初始化，连接数据库
    def __init__(self):
        self.__db = pymysql.connect("localhost", "root", "wjfrz", "shop")

    # 向admin_info表插入数据
    def insert_admin(self, account, password):
        cursor = self.__db.cursor()
        sql = 'insert into info_admin(account, password) VALUES (%s, %s)'
        cursor.execute(sql, (account, password))
        self.__db.commit()

    # 用字符串sql进行查询
    def select_admin(self, account):
        cursor = self.__db.cursor()
        sql = 'select * from info_admin where account = %s '
        cursor.execute(sql, account)
        # self.__db.commit()
        results = cursor.fetchall()
        for row in results:
            print(row)

    # 用cursor的execute函数执行查询
    def select_admin_sql_insert(self, account):
        cursor = self.__db.cursor()
        sql = 'select * from info_admin where account = %s '
        print(sql % account)
        cursor.execute(sql % account)
        # self.__db.commit()
        results = cursor.fetchall()
        for row in results:
            print(row)

test()
