from pymongo import MongoClient
import os
import sys
from pprint import pprint
import json

target_dir = "mallet_docs"

client = MongoClient()
db = client['PROG_WEB']

def extractDocsForMallet():
    cursor = db.articles.find({}, {"body":1})
    for document in cursor:
        with open(target_dir+'/'+str(document.get("_id")) + ".txt", 'w') as f:
            f.write(document.get("body"))

def extractDocsForExamination():
    cursor = db.articles.find()
    with open(os.path.join(os.getcwd(),"all_docs.txt"), 'w') as f:
        for document in cursor:
            f.write("Title: " + document.get("title") + '\n')
            f.write("Type: " + document.get("type") + '\n')
            f.write("Categories: \n")
            f.writelines(["%s\n" % item  for item in document.get("categories")])
            f.write("Body: " + document.get("body") + '\n\n')
            f.write("=================================================================================\n\n")

def main(argv):
    extractDocsForExamination()

if __name__ == "__main__":
    main(sys.argv)
