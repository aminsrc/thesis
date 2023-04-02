import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
import os
import sys
from random import randint
from time import sleep

def getArticleURLs():
    f = open('mashup_urls.txt', 'a')
    for i in range(252):
        r = requests.get("http://www.programmableweb.com/category/all/mashups?page="+str(i))
        print("Getting Mashup URLS from page " + str(i))
        soup = BeautifulSoup(r.content, "lxml")
        links = soup.find_all(href=re.compile("^/mashup/"))
        for link in links:
            f.write(link.get("href") + ',' + link.text)
            f.write('\n')
    f.close()

def main(argv):
    getArticleURLs()

if __name__ == "__main__":
    main(sys.argv)
