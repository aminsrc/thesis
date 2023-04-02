import requests
from bs4 import BeautifulSoup
import re
import os
import sys
from random import randint
from time import sleep

mashup_pages_dir = '../data/mashup_pages_dir'
mashup_descriptions_mallet_dir = '../mallet/mashup_descriptions'

def getDescription(soup, mashup_name):
    description = 'NA'
    url = soup('div',class_='tabs-header_description')
    if len(url) > 0:
        description = url[0].text.strip()
    else:
        print('soup did not find anything for: '+mashup_name)
    return description

counter = 1

for f in os.listdir(mashup_pages_dir):
    mashup_name = f.split('.')[0]
    print(str(counter) + ': getting mashup description from; ' + mashup_name)
    with open(os.path.join(mashup_pages_dir,f),'r') as fin:
        soup = BeautifulSoup(fin, 'lxml')
        description = getDescription(soup, mashup_name)
        with open(os.path.join(mashup_descriptions_mallet_dir,mashup_name+'.txt'),'w') as fout:
            fout.write(description)
    counter += 1
