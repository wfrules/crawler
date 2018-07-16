import pymysql
class db:
    def __init__(self, host, user, password, database):
        self.conn = pymysql.connect(host, user, password, database)
        self.cursor = self.conn.cursor()
    def nativeQry(self, sql):
        self.cursor.execute(sql)
        arrResults = self.cursor.fetchall()
        return arrResults
