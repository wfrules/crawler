# _*_ coding:utf-8 _*_
import requests
import re
import scrapy
import json
from pyquery import PyQuery as pq
from common import common
from selenium import webdriver
driver = None
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)


from db import gDb
from consts import gConsts
gCommon = common()
gSiteId = 1
gDoMain = "http://www.jitapu.com"




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

def analyzeArtistPage(detailUrl):
    try:
        sListContent = gCommon.fetch_url(detailUrl)
        objDoc = pq(sListContent)
        arrLinks = objDoc("#dlListArtist a")
        for i in range(len(arrLinks)):
            sAuthor = arrLinks.eq(i).text()
            sLink = gDoMain + "/" + arrLinks.eq(i).attr('href')
            sSql = "select * from author where aname=%s"
            arrRet = gDb.nativeQry(sSql, (sAuthor))
            if len(arrRet) == 0:
                gDb.nativeExec("insert author(aname)values(%s)", (sAuthor))
                iAuthorId = gDb.cursor.lastrowid
            else:
                iAuthorId = arrRet[0]['id']
                gDb.nativeExec("delete from author_link where author_id=%s and site_id=%s", (iAuthorId, gSiteId))
            sSql = "insert author_link(author_id,site_id,url)values(%s,%s,%s)"
            gDb.nativeExec(sSql, (iAuthorId, gSiteId, sLink))
            crawlTabList(sLink, iAuthorId)
    except:
        gCommon.showExcept(detailUrl +  " 作者列表异常" + sSql)

def analyzeArtistIndex():#逐个解析索引页
    arrKeys = ['[0-9]','a' ,'b','c','d','e','f','g','j','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for key in arrKeys:
        analyzeArtistPage('http://www.jitapu.com/listArtist.aspx?path=' + key)

def crawlTabList(authorUrl, authorId):#分析歌曲列表
    try:
        sListContent = gCommon.fetch_url(authorUrl)
        objDoc = pq(sListContent)
        arrTrs = objDoc("#dgListSong tr")
        for i in range(1, len(arrTrs)):
            arrTds = arrTrs.eq(i).find('td')
            sSong = arrTds.eq(0).find('a').text()
            iSongId = gDb.getSongIdByName(authorId, sSong)
            sLink = gDoMain + "/" + arrTds.eq(0).find('a').attr('href')

            sContent = ''
            if len(arrTrs) >= 4:
                sType = arrTds.eq(3).text().lower()
                if sType == "txt":
                    sContent = getTxtDetail(sLink)
            else:
                sType = 'unknown'
            iType = gConsts.tabTypes[sType]
            gDb.nativeExec("insert tab(song_id,url,site_id,ttype,content)values(%s,%s,%s,%s,%s)", (iSongId, sLink, gSiteId, iType, sContent))
        gDb.commit()
    except:
        gCommon.showExcept(authorUrl + ' 曲谱列表异常')

def getTxtDetail(detailUrl):#分析详情页面 用selenium解决pre渲染的问题
    try:
        driver.get(detailUrl)
        domTxt = driver.find_element_by_id('txt')
        sContent = domTxt.text
        return sContent
    except:
        gCommon.showExcept(detailUrl + ' 曲谱详情异常')

if __name__ == "__main__":
    main()