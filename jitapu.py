# _*_ coding:utf-8 _*_
import requests
import re
import scrapy
import json
from pyquery import PyQuery as pq
from common import common
gCommon = common()

gDoMain = "http://www.jitapu.com"

from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)


def analyzeAtrists(listUrl):#分析作者列表
    try:
        sListContent = gCommon.fetch_url(listUrl)
        objDoc = pq(sListContent)
        arrLinks = objDoc("#dlListArtist a")
        for i in range(len(arrLinks)):
            sLink = gDoMain + "/" + arrLinks.eq(i).attr('href')
            analyzeSongList(sLink)
    except:
        gCommon.showExcept(listUrl + " 作者列表异常")

def analyzeSongList(listUrl):#分析歌曲列表
    try:
        sListContent = gCommon.fetch_url(listUrl)
        objDoc = pq(sListContent)
        arrTrs = objDoc("#dgListSong tr")
        for i in range(len(arrTrs)):
            objTds = arrTrs.eq(i).find('td')
            if objTds[3].text == "TXT":
                sLink = gDoMain + "/" + objTds.eq(0).find('a').attr('href')
                analyzeDetail(sLink)
    except:
        gCommon.showExcept(listUrl + ' 曲谱列表异常')



def analyzeDetail(detailUrl):#分析详情页面 用selenium解决pre渲染的问题
    try:
        driver.get(detailUrl)
        domTxt = driver.find_element_by_id('txt')
        sContent = domTxt.text
        sAuthor = driver.find_element_by_css_selector('#tcbInfo a').text #这里选择的是第一个匹配元素
        sSong = driver.find_element_by_css_selector('#tabControlBar h3').text #这里选择的是第一个匹配元素
        dicTab = {
            'url': detailUrl,
            'song': sSong,
            'author': sAuthor,
            'content': sContent
        }
        gCommon.save_file(dicTab['author'], dicTab['song'] + '.txt', dicTab['content'])
    except:
        gCommon.showExcept(detailUrl + ' 曲谱详情异常')
def main():
    arrKeys = ['[0-9]','a' ,'b','c','d','e','f','g','j','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    try:
        for key in arrKeys:
            analyzeAtrists('http://www.jitapu.com/listArtist.aspx?path=' + key)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()