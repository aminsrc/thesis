import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
import os
import sys
from random import randint
from time import sleep

mashup_dates_dir = '../data/mashup_dates_dir'
def getMashupDates():
    for i in range(1,252):
        try:
            r = requests.get("http://www.programmableweb.com/category/all/mashups?page="+str(i))
            print("Getting api listings for page: " + str(i))
            soup = BeautifulSoup(r.content, 'lxml')
            with open(os.path.join(mashup_dates_dir,str(i)+'.html'), 'w') as f:
                f.write(soup.prettify())
        except:
            e = sys.exc_info()[0]
            print(e)

def main(argv):
    getMashupDates()

if __name__ == "__main__":
    main(sys.argv)
