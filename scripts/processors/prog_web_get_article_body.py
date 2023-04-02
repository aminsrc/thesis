import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
import os
import sys
from random import randint
from time import sleep
import json
import logging


logging.basicConfig(filename='get_articles.log',level=logging.INFO)
client = MongoClient()
db = client['PROG_WEB']


def getDocumentDict(url, body, categories):
    article_metadata = url.split('/')
    print(article_metadata)
    article_title= article_metadata[2]
    if(len(article_metadata) == 7):
        article_type = article_metadata[3]
    else:
        article_type = "NA"
    article_date_year = article_metadata[len(article_metadata)-3]
    article_date_month = article_metadata[len(article_metadata)-2]
    article_date_day = article_metadata[len(article_metadata)-1]
    article = dict([('title', article_title),
                    ('type', article_type),
                    ('categories', categories),
                    ('date_year', article_date_year),
                    ('date_month', article_date_month),
                    ('date_day', article_date_day),
                    ('body', body)])
    return article

def getArticleBody(paragraphs):
    body = ""
    for paragraph in paragraphs:
        body += paragraph.text.strip()
        body += " "
    return body

def getArticlesBodies():
    f = open('processed_article_urls.txt', 'r')
    for line in f:
        stripped_line = line.strip()
        r = requests.get("http://www.programmableweb.com"+stripped_line)
        soup = BeautifulSoup(r.content, "lxml")
        body = getArticleBody(soup.find_all('p'))
        categories = [category.text for category in soup.find_all('a', class_=(re.compile('eyebrow\d')))]
        article_document = getDocumentDict(stripped_line, body, categories)
        result = db.articles.insert_one(article_document)
        log_msg = "Article: " + stripped_line + " inserted with id: " + str(result.inserted_id)
        logging.info(log_msg)
        print(log_msg)
        random_time = randint(1,10)
        print("Sleeping for " + str(random_time) + " seconds.")
        sleep(random_time)
    f.close()

def main(argv):
    getArticlesBodies()

if __name__ == "__main__":
    main(sys.argv)
