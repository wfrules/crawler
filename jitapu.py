#

import requests
import re
import scrapy
import json
import os
from pyquery import PyQuery as pq

session = requests.session()
gDoMain = "http://www.jitapu.com"
gBaseDir = '../tab'
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://www.cheerby.com")


def fetch_url(url):
    return session.get(url).content.decode('gbk')

def save_file(directory, filename, content):
    sBaseDir = gBaseDir + '/' + directory;
    if not os.path.exists(sBaseDir):
        os.makedirs(sBaseDir)
    with open(sBaseDir + '/' + filename, 'w', encoding='utf8') as f:
        f.write(content)
        print('已保存为:' + filename)

def analyzeDetail(detailUrl):#分析详情页面
    sDetailContent = fetch_url(detailUrl)
    objDoc = pq(sDetailContent)
    domTcbInfo  = objDoc('#tcbInfo')
    arrLinks = domTcbInfo("a")
    sAuthor = arrLinks[0].text
    sSong = objDoc('#tabControlBar h3').text()
    domTxt = objDoc('#txt')
    domPre = objDoc('pre')
    sContent = domPre.text()
    dicTab = {
        'url': detailUrl,
        'song': sSong,
        'author': sAuthor,
        'content': sContent
    }
    save_file(dicTab['author'], dicTab['song'] + '.txt', dicTab['content'])

def main():
    url = 'http://www.jitapu.com/tabPages/7361/txt20165601065606.htm'   #列表页
    analyzeDetail(url)

if __name__ == "__main__":
    main()