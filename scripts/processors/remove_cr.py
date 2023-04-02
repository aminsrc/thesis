import os
import sys

working_dir = os.getcwd()
target_dir = sys.argv[1]

for filename in os.listdir(working_dir + '/' + target_dir):
    f = open(working_dir + '/' + target_dir + '/' + filename, 'r')
    lines = f.readlines()
    f.close()
    f = open(working_dir + '/' + target_dir + '/' + filename, 'w')
    for line in lines:
        stripped_line = line.strip()
        f.write(stripped_line)
        f.write(' ')
    f.close()
