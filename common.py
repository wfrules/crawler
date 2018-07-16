import os
import sys
import requests
session = requests.session()
gBaseDir = '../tab'

class common:
    def fetch_url(self,url):#爬取网页数据
        return session.get(url).content.decode('gbk')
    def showExcept(self, title):#显示异常公用函数
        print(title)
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
    def save_file(self, directory, filename, content):
        sBaseDir = gBaseDir + '/' + directory;
        filename =  filename.replace('/', '_')
        filename = filename.replace('\\', '_')
        if not os.path.exists(sBaseDir):
            os.makedirs(sBaseDir)
        with open(sBaseDir + '/' + filename, 'w', encoding='utf8') as f:
            f.write(content)
            print('已保存为:' + filename)