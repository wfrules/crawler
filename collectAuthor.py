# _*_ coding:utf-8 _*_
import pymysql
import requests
import re
from pyquery import PyQuery as pq
from jitapu import analyzeArtistIndex
from jitapu import getTxtDetail
from common import common
gCommon = common()
from db import gDb


def main():
    try:
        gCommon.fetch_url("http://www.jitapu.com/listSong201504.aspx?id=7688&ArtistName=张学友")
        # getTxtDetail("http://www.jitapu.com/CreatHtml.aspx?id=10505&creat=False&class=1&Url=903/txt20063515093518.htm     ")
        # analyzeArtistIndex()
    finally:
        print("执行完毕")


if __name__ == "__main__":
    main()

