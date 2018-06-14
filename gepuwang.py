#

import requests
import re
import json
import os

session = requests.session()

def fetch_url(url):
    return session.get(url).content.decode('gbk')


def getPageNum(content):#获取总页码
    result = re.findall('(?<=共 <strong>)\d*(?=</strong>页)', content)[0]  #特殊字符之间包含的表达式
    iPageNum = int(result)
    return iPageNum

def main():
    url = 'http://www.gepuwang.net/hexianpu/list_62_1.html'   #列表页
    content = fetch_url(url)
    iPageNum = getPageNum(content)
    iPageNum = 1
    for i in range(iPageNum):
        url = 'http://www.gepuwang.net/hexianpu/list_62_' + str(i+1) +'.html'
        print(url)

if __name__ == "__main__":
    main()