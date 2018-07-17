# _*_ coding:utf-8 _*_
import pymysql
import requests
import re
from pyquery import PyQuery as pq
from jitapu import analyzeArtistIndex
from common import common
gCommon = common()
from db import gDb


def main():
    try:
        analyzeArtistIndex()
        gDb.commit()
    finally:
        print("执行完毕")


if __name__ == "__main__":
    main()

