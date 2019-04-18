from PyQt5.QtCore import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtSql import *


class DbDao(QObject):
    # 初始化并连接数据库
    def __init__(self):
        QObject.__init__(self)
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        self.db.setDatabaseName("pyqt5_p")
        self.db.setUserName("root")
        self.db.setPassword("chuy5945")
        ok = self.db.open()
        print('数据库连接:' + str(ok))

    # 判断是否打开
    def getIsOpen(self):
        return self.db.isOpen

    # 查询
    def query(self):
        query = QSqlQuery(self.db)
        query.exec("select * from user")
        while (query.next()):
            print(query.value(0))
            print(query.value(1))
            print(query.value(2))

    # 插入
    def insert(self):
        query = QSqlQuery(self.db)
        query.prepare("insert into chat_room (room_id,room_title,need_password,password,ownner_id)"
                      "values (?,?,?,?,?)")
        query.addBindValue(1004)
        query.addBindValue("聊天室3")
        query.addBindValue(1)
        query.addBindValue(000000)
        query.addBindValue(111)
        result = query.exec_()
        print(result)

        # query = QSqlQuery(self.db)
        #  result=query.exec_("insert into chat_room (room_id,room_title,need_password,password,ownner_id)"
        #                     """values (1001,'聊天室3',1,0000,11)""");
        # print(result)

    # 更新
    def update(self):
        query = QSqlQuery(self.db)
        # query.prepare("update chat_room set room_title ="+"聊天"+" where room_id = "+str(1004))
        result = query.exec_("""update chat_room set room_title ="聊天" where room_id = 1004""")
        # result = query.exec_()
        print(result)

    # 删除
    def delete(self):
        query = QSqlQuery(self.db)
        query.prepare("delete from chat_room where room_id =" + str(1003))
        result = query.exec_()
        print(result)


if __name__ == '__main__':
    db_ = DbDao()
    db_.getIsOpen()
    db_.query()
