from datetime import datetime
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

def getAPIsDict():
    apis = {}
    data_dir = "../data"
    with open(os.path.join(data_dir, 'api_dates.csv'), 'r') as fin:
        lines = fin.readlines()
        for line in lines:
            api_to_date = line.strip().split(',')
            api_name = api_to_date[0].replace(' ', '_')
            api_date = api_to_date[1]
            apis[api_name] = api_date

    with open('../mallet/output/api_desc/40-topics/output-doc-topics', 'r') as doc_topics:
        lines = doc_topics.readlines()
        for line in lines:
            items = line.split('\t')
            api_name_string = items[1].split('/')
            api_name_doc_topics = api_name_string[len(api_name_string)-1].split('.')[0]

            if(api_name_doc_topics in apis):
                current_value = [apis[api_name_doc_topics]]
                if len(items) >= 5:
                    top_topic_id = int(items[2]) + 1
                    top_topic_dist = float(items[3])
                    current_value.append(str(top_topic_id))
                    current_value.append(str(top_topic_dist))
                    apis[api_name_doc_topics] = current_value
    return apis

def getDatesDict():
    dates = {}
    for year in range(2004,2017):
        for month in range(1,13):
            dates[datetime(year,month,1)] = [0,0]
    return dates

def getDocsPerDateForTopicDict(topic):
    apis = getAPIsDict()
    dates = getDatesDict()
    for apis_key, apis_value in apis.items():
        apis_date = apis_value[0].split('.')

        if(len(apis_date) == 3):
            apis_top_doc = apis_value[1]
            apis_dist = apis_value[2]
            apis_date_datetime = datetime(int(apis_date[2]),int(apis_date[0]),1)

            if apis_top_doc == topic or topic == "all_topics":
                current_dates_doc_count = dates[apis_date_datetime][0]
                current_dates_dist_count = dates[apis_date_datetime][1]
                new_dates_doc_count = int(current_dates_doc_count) + 1
                new_dates_dist_count = float(current_dates_dist_count) + float(apis_dist)
                new_dates_value = [str(new_dates_doc_count),str(new_dates_dist_count)]
                dates[apis_date_datetime] = new_dates_value
    return dates

def getAggrgate(dicts):
    aggregate_dict = getDatesDict()
    for k,v in aggregate_dict.items():
        doc_count = int(v[0])
        dist_count = float(v[1])
        for dictionary in dicts:
            doc_count += int(dictionary[k][0])
            dist_count += float(dictionary[k][1])
        aggregate_dict[k] = [str(doc_count), str(dist_count)]

    return aggregate_dict

def getAllDocsPerDateDict():
    return getDocsPerDateForTopicDict("all_topics")

def getSumDocCount(dictionary):
    count = 0
    for k,v in dictionary.items():
        count += int(v[0])
    return str(count)

def getCumulativeDict(dictionary):
    new_dictionary = dictionary
    dates_list = []
    for year in range(2004,2017):
        for month in range(1,13):
            dates_list.append(datetime(year,month,1))

    for i in range(1,len(dates_list)):
        new_doc_count = int(new_dictionary[dates_list[i]][0]) + int(new_dictionary[dates_list[i-1]][0])
        new_dist_count = float(new_dictionary[dates_list[i]][1]) + float(new_dictionary[dates_list[i-1]][1])
        new_dictionary[dates_list[i]] = [str(new_doc_count),str(new_dist_count)]

    return new_dictionary

def getXandYAxis(cumulative_all_topics,cumulative_topic_dates):
    dates_list_datetime = []
    x_axis = []
    y_axis = []
    for year in range(2006,2017):
        for month in range(1,13):
            date = datetime(year,month,1)

            topic_doc_count = cumulative_topic_dates[datetime(year,month,1)][0]
            total_doc_count = cumulative_all_topics[datetime(year,month,1)][0]
            if (total_doc_count != '0'):
                perc_docs_total = int(topic_doc_count)/int(total_doc_count)
                y_axis.append(str(perc_docs_total))
                x_axis.append(date)

                #y_axis.append(total_doc_count)

    return x_axis,y_axis

def getListOfCumulativeDicts():
    cumulative_topic_dates_dicts = []
    for i in range(1,40):
        if (i != 9):
            topic_dates_dict = getDocsPerDateForTopicDict(str(i))
            cumulative_topic_dates_dicts.append(getCumulativeDict(topic_dates_dict))
    return cumulative_topic_dates_dicts

def plotTopic(all_topics_dict, cumulative_dict, topic, colour):
    x_axis, y_axis = getXandYAxis(all_topics_dict,cumulative_dict)
    plt.figure(1)
    plt.plot(x_axis,y_axis,color=plt.cm.RdYlBu(colour),label=topic)
    plt.legend(loc='best')

def main(argv):
    all_topics_dict = getAllDocsPerDateDict()
    cumulative_all_topics_dict = getCumulativeDict(all_topics_dict)
    cumulative_topic_dates_dicts = getListOfCumulativeDicts()
    colours = []
    for i in np.linspace(0,1,26):
        colours.append(i)

    platforms = [1,11,23,35]
    health = [12,28]
    big_data = [10,19,20,22]
    aggregate_platforms = [cumulative_topic_dates_dicts[i] for i in platforms]
    aggregate_health = [cumulative_topic_dates_dicts[i] for i in health]
    aggregate_big_data = [cumulative_topic_dates_dicts[i] for i in big_data]

    aggregate_platforms_dict = getAggrgate(aggregate_platforms)
    aggregate_health_dict = getAggrgate(aggregate_health)
    aggregate_big_data_dict = getAggrgate(aggregate_big_data)

    plotTopic(all_topics_dict, aggregate_platforms_dict, "Platforms", colours[0])
    plotTopic(all_topics_dict, aggregate_big_data_dict, "Big Data", colours[10])
    plotTopic(all_topics_dict, aggregate_health_dict, "Health", colours[20])

    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[0], "Real Estate", colours[0])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[1], "Social", colours[0])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[2], "Shipping", colours[2])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[3], "Github", colours[3])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[4], "Mobile", colours[4])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[5], "Cloud", colours[5])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[9], "Music", colours[6])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[10], "Car Registration", colours[7])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[11], "Financial", colours[8])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[12], "Health", colours[5])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[13], "Marketing", colours[10])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[14], "Weather", colours[11])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[16], "Location", colours[12])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[17], "E-Commerce", colours[13])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[18], "Chat", colours[14])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[19], "Sports Stats", colours[15])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[20], "Open Data", colours[10])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[22], "Text Analysis", colours[17])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[23], "Payment", colours[18])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[25], "Verified Emails", colours[19])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[26], "Content Uploading", colours[20])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[28], "Protein Sequencing", colours[15])
    #plotTopic(all_topics_dict, cumulative_topic_dates_dicts[35], "Trading", colours[20])

    plt.show()



if __name__ == "__main__":
    main(sys.argv)
