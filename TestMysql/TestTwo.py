from TestMysql.DataBase.mysql import Mysql


def test():
    print('hello')
    mysql = Mysql()
    # mysql.insert('info_admin', {'account': 'cwj', 'password': 'tbsb'})
    # mysql.delete('info_admin', {'account': 'cwj', 'password': 'tbsb'})
    # mysql.update('info_admin', {'password': 'ssb'}, {'account': 'cwj', 'password': 'tbsb'})
    print(mysql.select('info_admin', ('account', 'password'), {'account': 'cwj', 'password': 'ssb'}))


test()
