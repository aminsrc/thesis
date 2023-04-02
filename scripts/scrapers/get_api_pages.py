import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
import os
import sys
from random import randint
from time import sleep

api_pages_dir = 'api_pages_dir'
f = open('unique_api_urls.txt', 'r')
for line in f:
    url_list = line.split(',')
    api_url = url_list[0].strip()
    api_name = url_list[1].strip()
    api_file_name = api_name.replace(' ', '_') + '.html'
    print('trying with: ' + api_url)
    try:
        r = requests.get("http://www.programmableweb.com"+api_url)
        soup = BeautifulSoup(r.content, 'lxml')
        with open(os.path.join(api_pages_dir,api_file_name), 'w') as f:
            f.write(soup.prettify())
    except:
        e = sys.exc_info()[0]
        print(e)
        print('API URL: ' + api_url)
