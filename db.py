import pymysql
class db:
    def __init__(self):
        self.conn = pymysql.connect("localhost","root","root","tabs")
        self.cursor = self.conn.cursor()
    def nativeQry(self, sql, params):#查询语法
        self.cursor.execute(sql, params)
        arrResult = []
        index = self.cursor.description
        for res in self.cursor.fetchall():
            row = {}
            for i in range(len(index)):
                row[index[i][0]] = res[i]
            arrResult.append(row)

        return arrResult
    def nativeExec(self, sql, params):#执行语法
        self.cursor.execute(sql, params)
    def commit(self):#提交任务
        self.conn.commit()
gDb = db()