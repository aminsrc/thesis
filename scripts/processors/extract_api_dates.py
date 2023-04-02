import requests
from bs4 import BeautifulSoup
import re
import os

api_pages_dir = "../data/api_dates_dir"
test_dir = "../data/test"
data_dir = "../data"


with open(os.path.join(data_dir,"api_dates.csv"), 'w') as fout:
    for f in os.listdir(api_pages_dir):
        with open(os.path.join(api_pages_dir,f), 'r') as fin:
            soup = BeautifulSoup(fin, 'lxml')
            rows = soup.find_all('tr')
            for row in rows:
                cols = row.findAll('td')
                if(len(cols) == 4):
                    fout.write(cols[0].a.string.strip())
                    fout.write(',')
                    fout.write(cols[3].string.strip())
                    fout.write('\n')
