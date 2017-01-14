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
            [uid, mid, date, time, forward_count, comment_count, like_count, content] - train_data
            [uid, mid, data, time, content] - test_data
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

def write_result_data(test_data, forward_count, comment_count, like_count, result_file_path):
    """
    write result data into result file.
    format: uid(tab)mid(tab)forward_count(,)comment_count(,)like_count
    """
    result_file = open(result_file_path, 'w')
    if not isinstance(forward_count, list):
        assert not isinstance(comment_count, list)
        assert not isinstance(like_count, list)
        forward_count = [forward_count] * len(test_data)
        comment_count = [comment_count] * len(test_data)
        like_count = [like_count] * len(test_data)
    for index, element in enumerate(test_data):
        element = element[:2]
        element = element + [forward_count[index]] + [comment_count[index]] + [like_count[index]]
        result_file.write(element[0]+'\t'+element[1]+'\t' \
                            +str(element[2])+',' \
                            +str(element[3])+',' \
                            +str(element[4])+'\n')
    result_file.close()



if __name__ == '__main__':
    TRAIN_DATA = read_data('../Weibo_Data/weibo_train_data.txt')
    FORWARD, COMMENT, LIKE = extract_count(TRAIN_DATA)
    FORWARD_MEAN = sum(FORWARD) / len(FORWARD)
    COMMENT_MEAN = sum(COMMENT) / len(COMMENT)
    LIKE_MEAN = sum(LIKE) / len(LIKE)
    #
    TEST_DATA = read_data('../Weibo_Data/weibo_predict_data.txt')
    write_result_data(TEST_DATA, 0, 0, 0, '../result/weibo_result_data_0.txt')
    # write_result_data(TEST_DATA, FORWARD_MEAN, COMMENT_MEAN, LIKE_MEAN, '../weibo_result_data.txt')
