import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
import os
import sys
from random import randint
from time import sleep

def getArticleURLs():
    f = open('article_urls.txt', 'a')
    for i in range(274,400):
        r = requests.get("http://www.programmableweb.com/category/all/news?page="+str(i))
        print("Getting article URLS from page " + str(i))
        soup = BeautifulSoup(r.content, "lxml")
        links = soup.find_all(href=re.compile("^/news"))
        for link in links:
            f.write(link.get("href"))
            f.write('\n')
        random_time = randint(5,35)
        print("Sleeping for " + str(random_time))
        sleep(random_time)
    f.close()

def main(argv):
    getArticleURLs()

if __name__ == "__main__":
    main(sys.argv)
