fin = open('../mallet/output/api_desc/50-topics/output-doc-topics', 'r')
lines = fin.readlines()
fout = open('../data/api_net_50_format_removed', 'w')
network = []
for line in lines:
    items = line.split('\t')
    #print(items)
    if len(items) == 5:
        first_topic = items[2]
        if first_topic == '2' or first_topic =='20':
            continue
        network.append(first_topic)
    elif len(items) > 5:
        first_topic = items[2]
        second_topic = items[4]
        if first_topic == '2' or first_topic =='20' or second_topic == '2' or second_topic == '20':
            continue
        if int(first_topic) < int(second_topic):
            network.append((first_topic, second_topic))
        else:
            network.append((second_topic, first_topic))

counts = {}
for list_item in network:
    counts[list_item] = counts.get(list_item, 0) + 1
fout.write('Source,Target,Weight,Type\n')
for key, value in counts.items():
    if len(key) > 1:
        fout.write(key[0] + ',' + key[1] + ',' + str(value) + ','+'Undirected' '\n')

#print(count)
