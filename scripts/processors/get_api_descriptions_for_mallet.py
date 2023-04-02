import requests
from bs4 import BeautifulSoup
import re
import os
import sys
from random import randint
from time import sleep

api_pages_dir = '../data/api_pages_dir'
api_descriptions_mallet_dir = '../mallet/api_descriptions'

def getDescription(soup, api_name):
    description = 'NA'
    url = soup.find_all('div', class_="api_description")
    if len(url) > 0:
        description = url[0].text.strip()
    else:
        print('soup did not find anything for: '+api_name)
    return description


for f in os.listdir(api_pages_dir):
    api_name = f.split('.')[0]
    with open(os.path.join(api_pages_dir,f),'r') as fin:
        soup = BeautifulSoup(fin, 'lxml')
        description = getDescription(soup, api_name)
        with open(os.path.join(api_descriptions_mallet_dir,api_name+'.txt'),'w') as fout:
            fout.write(description)
