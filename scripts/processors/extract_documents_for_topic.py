with open('../mallet/output/api_desc/40-topics/output-doc-topics', 'r') as fin:
    with open('../data/topic-docs-1-and-13','w') as fout:
        lines = fin.readlines()
        fout.write("api_name,top_topic_id,top_topic_dist\n")
        for line in lines:
            items = line.split('\t')
            api_name_string = items[1].split('/')
            api_name = api_name_string[len(api_name_string)-1].split('.')[0]

            if len(items) >= 5:
                top_topic_id = int(items[2]) + 1
                top_topic_dist = float(items[3])
                if top_topic_id == 1 or top_topic_id == 13:
                    fout.write(api_name + ',' + str(top_topic_id) + ',' + str(top_topic_dist) + '\n')
