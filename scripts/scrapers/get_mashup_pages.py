import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
import os
import sys
from random import randint
from time import sleep

mashup_pages_dir = '../data/mashup_pages_dir'
f = open('../data/mashup_urls.txt', 'r')
for line in f:
    url_list = line.split(',')
    mashup_url = url_list[0].strip()
    mashup_name = url_list[1].strip()
    mashup_file_name = mashup_name.replace(' ', '_') + '.html'
    print('trying with: ' + mashup_url)
    try:
        r = requests.get("http://www.programmableweb.com"+mashup_url)
        soup = BeautifulSoup(r.content, 'lxml')
        with open(os.path.join(mashup_pages_dir,mashup_file_name), 'w') as f:
            f.write(soup.prettify())
    except:
        e = sys.exc_info()[0]
        print(e)
        print('API URL: ' + mashup_url)
