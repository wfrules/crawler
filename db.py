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
    def getSongIdByName(self, authorId, songName):
        arrRet = self.nativeQry("select id from song where author_id=%s and sname=%s", (authorId, songName))
        if len(arrRet) == 0:
            self.nativeExec("insert song(sname,author_id)values(%s, %s)", (songName, authorId))
            iSongId = self.cursor.lastrowid
        else:
            iSongId = arrRet[0]['id']
        return iSongId
gDb = db()