#

import requests
import re
import scrapy
import json
import os

session = requests.session()
gDoMain = "http://www.gepuwang.net"

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://www.cheerby.com")


def fetch_url(url):
    return session.get(url).content.decode('gbk')


def getPageNum(content):#获取总页码
    result = re.findall('(?<=共 <strong>)\d*(?=</strong>页)', content)[0]  #特殊字符之间包含的表达式
    iPageNum = int(result)
    return iPageNum

def analyzeList(listContent): #分析列表数据
    listResult = re.findall('(?<=<h3><a href=")/hexianpu/\d*.html(?=" target="_blank">)', listContent)
    for slink in listResult:
        analyzeDetail(gDoMain + slink)

def analyzeDetail(detailUrl):#分析详情页面
    sDetailContent = fetch_url(detailUrl)
    print(detailUrl)

def main():
    url = 'http://www.gepuwang.net/hexianpu/list_62_1.html'   #列表页
    content = fetch_url(url)
    iPageNum = getPageNum(content) #页数
    iPageNum = 1
    for i in range(iPageNum):
        sUrl = 'http://www.gepuwang.net/hexianpu/list_62_' + str(i+1) +'.html'
        sContent = fetch_url(sUrl)
        analyzeList(sContent)

if __name__ == "__main__":
    main()