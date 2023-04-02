import matplotlib.pyplot as plt
import numpy as np
import csv

f = open('../data/diagnostics_40.csv', 'r')
csvreader = csv.reader(f,delimiter=',')

for row in csvreader:
    ids = row[0]
    tokens = row[1]
    document_entropy = row[2]
    word_length = row[3]
    coherence = row[4]
    uniform_dist = row[5]
    corpus_dist = row[6]
    eff_num_words = row[7]
    token_doc_diff = row[8]
    rank_1_docs = row[9]
    allocation_ratio = row[10]
    allocation_count = row[11]
    exclusivity = row[12]

plt.plot(ids, tokens)
