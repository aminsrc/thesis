import os
import sys
from collections import Counter

unique_lines = set(open('api_urls.txt').readlines())
unique_list = sorted(unique_lines)

f = open('unique_api_urls.txt','w')
for line in unique_list:
    f.write(line)
f.close()
