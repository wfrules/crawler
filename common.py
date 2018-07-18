import os
import sys
import requests
from selenium import webdriver

import string
from urllib.parse import quote


session = requests.session()
gBaseDir = '../tab'


class common:
    __chromeDriver = None

    def __del__(self):
        print("析构")
        # if self.__chromeDriver != None:
        #     print('释放chrome')
        #     # self.__chromeDriver.quit()
    @property
    def chrome(self):#获取google headless driver
        if self.__chromeDriver == None:
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            self.__chromeDriver = webdriver.Chrome(chrome_options=option)
        return self.__chromeDriver

    def freeChrome(self):#释放chromedriver
        if self.__chromeDriver != None:
            print("释放chrome")
            self.__chromeDriver.quit()

    def fetch_url(self,url):#爬取网页数据
        sEncodedUrl = quote(url, safe=string.printable)
        return session.get(sEncodedUrl).content.decode('gbk')

    def showExcept(self, title):#显示异常公用函数
        print(title)
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])

    def save_file(self, directory, filename, content):
        sBaseDir = gBaseDir + '/' + directory
        filename =  filename.replace('/', '_')
        filename = filename.replace('\\', '_')
        if not os.path.exists(sBaseDir):
            os.makedirs(sBaseDir)
        with open(sBaseDir + '/' + filename, 'w', encoding='utf8') as f:
            f.write(content)
            print('已保存为:' + filename)


gCommon = common()
