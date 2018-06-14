#

import requests
import re
import json
import os

session = requests.session()

def fetch_url(url):
    return session.get(url).content.decode('gbk')


def getPageNum(content):
    result = re.findall('^页<strong>\d', content)
    print(result)

def main():
    url = 'http://www.gepuwang.net/hexianpu/list_62_1.html'   #列表页
    content = fetch_url(url)
    getPageNum(content)

if __name__ == "__main__":
    main()