import os
import sys
fin = open('api_urls.txt','r')
fout = open('api_got_sorted.txt','w')

apis = [api.split(',')[0].replace('/api/','').strip() for api in fin.readlines()]
apis.sort()

for api in apis:
    print(api)
