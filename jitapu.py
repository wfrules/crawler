# _*_ coding:utf-8 _*_
import requests
import re
import scrapy
import json
from pyquery import PyQuery as pq
from common import common
from selenium import webdriver
from db import gDb
gCommon = common()
gSiteId = 1
gDoMain = "http://www.jitapu.com"

driver = None


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
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)
    arrKeys = ['[0-9]','a' ,'b','c','d','e','f','g','j','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    try:
        for key in arrKeys:
            analyzeAtrists('http://www.jitapu.com/listArtist.aspx?path=' + key)
    finally:
        driver.quit()

def analyzeArtistPage(detailUrl):
    try:
        sListContent = gCommon.fetch_url(detailUrl)
        objDoc = pq(sListContent)
        arrLinks = objDoc("#dlListArtist a")
        for i in range(len(arrLinks)):
            sAuthor = arrLinks.eq(i).text()
            sSql = "INSERT author(aname)SELECT %s FROM author \
                WHERE NOT EXISTS(SELECT id FROM author WHERE \
                aname = %s) limit 1"
            gDb.nativeExec(sSql, (sAuthor, sAuthor))
    except:
        gCommon.showExcept(detailUrl +  " 作者列表异常" + sSql)

def analyzeArtistIndex():#逐个解析索引页
    arrKeys = ['[0-9]','a' ,'b','c','d','e','f','g','j','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for key in arrKeys:
        analyzeArtistPage('http://www.jitapu.com/listArtist.aspx?path=' + key)


if __name__ == "__main__":
    main()