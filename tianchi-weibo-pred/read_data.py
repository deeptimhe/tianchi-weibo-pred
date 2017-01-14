#! /usr/bin/env python
# -*- coding: utf8 -*-

# author:   Tim He
# date:     2017-01-14
# function: read weibo data into list


def read_data(data_path):
    """
    read weibo data.

    Input:  path to data.txt file, e.g.,  '../Weibo_Data/weibo_train_data.txt'
    Output: a list. And each element is a list which containing:
            [uid, mid, date, time, forward_count, comment_count, like_count, content]
    """
    weibo_train_data = open(data_path, 'r')
    data = list()
    for line in weibo_train_data:
        # print line
        data.append(line.split())
    weibo_train_data.close()
    return data

def extract_count(data):
    """
    extract forward_count, comment_count, like_count from data and save as list(float).
    """
    forward_count_data = list()
    comment_count_data = list()
    like_count_data = list()
    for element in data:
        forward_count_data.append(float(element[4]))
        comment_count_data.append(float(element[5]))
        like_count_data.append(float(element[6]))
    return forward_count_data, comment_count_data, like_count_data



if __name__ == '__main__':
    TRAIN_DATA = read_data('../Weibo_Data/weibo_train_data.txt')
    FORWARD, COMMENT, LIKE = extract_count(TRAIN_DATA)
    print sum(FORWARD) / len(FORWARD)
    print sum(COMMENT) / len(COMMENT)
    print sum(LIKE) / len(LIKE)
