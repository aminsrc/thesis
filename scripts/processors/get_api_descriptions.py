import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
import os
import sys
from random import randint
from time import sleep


client = MongoClient()
db = client['PROG_WEB']
api_pages_dir = 'api_pages_dir'

def getDocumentDict(soup, api_name):
    body = 'NA'
    url = soup.find_all('div', class_="api_description")
    if len(url) > 0:
        body = url[0].text.strip()
    else:
        print('soup did not find anything for: '+api_name)
    return dict([('name', api_name),
                ('body', body)])


for f in os.listdir(api_pages_dir):
    api_name = f.split('.')[0]
    with open(os.path.join(api_pages_dir,f),'r') as fin:
        soup = BeautifulSoup(fin, 'lxml')
        document = getDocumentDict(soup, api_name)
        result = db.apis.insert_one(document)
