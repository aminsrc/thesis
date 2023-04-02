import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
import os
import sys
from random import randint
from time import sleep

def getArticleURLs():
    f = open('api_urls.txt', 'a')
    for i in range(556):
        r = requests.get("http://www.programmableweb.com/category/all/apis?page="+str(i))
        print("Getting API URLS from page " + str(i))
        soup = BeautifulSoup(r.content, "lxml")
        links = soup.find_all(href=re.compile("^/api/"))
        for link in links:
            f.write(link.get("href") + ',' + link.text)
            f.write('\n')
        random_time = randint(1,3)
        print("Sleeping for " + str(random_time))
        sleep(random_time)
    f.close()

def main(argv):
    getArticleURLs()

if __name__ == "__main__":
    main(sys.argv)
