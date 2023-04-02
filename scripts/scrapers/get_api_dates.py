import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
import os
import sys
from random import randint
from time import sleep

api_dates_dir = '../data/api_dates_dir'
def getArticleURLs():
    for i in range(134,562):
        try:
            r = requests.get("http://www.programmableweb.com/category/all/apis?page="+str(i))
            print("Getting api listings for page: " + str(i))
            soup = BeautifulSoup(r.content, 'lxml')
            with open(os.path.join(api_dates_dir,str(i)+'.html'), 'w') as f:
                f.write(soup.prettify())
        except:
            e = sys.exc_info()[0]
            print(e)

def main(argv):
    getArticleURLs()

if __name__ == "__main__":
    main(sys.argv)
