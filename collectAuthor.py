# _*_ coding:utf-8 _*_
import pymysql
import requests
import re
import scrapy
import json
from pyquery import PyQuery as pq
from common import common
gCommon = common()
from db import db
gDb = db("localhost","root","root","tabs")
arrRet = gDb.nativeQry("select id,sname,url from site")
print(arrRet)

arrRet = gDb.nativeQry("select * from song")
print(arrRet)


from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)

def main():
    try:
        print('wf')
    finally:
        driver.quit()

if __name__ == "__main__":
    main()