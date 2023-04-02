import os
import sys
from collections import Counter

unique_lines = set(open('api_got.txt').readlines())
unique_list = sorted(unique_lines)

for line in unique_list:
    if 'API URL:' in line:
        print(line)
