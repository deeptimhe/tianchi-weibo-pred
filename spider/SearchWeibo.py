#! /usr/bin/env python
# coding: utf-8

# author: Tim-He

import urllib
import urllib2
from bs4 import BeautifulSoup
import json
import re

cookie = None

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'cookie': cookie
}

class SearchWeibo(object):
    """
    Search weibo by keyword.
    """
    def __init__(self, keyword):
        # self.keyword = self.GBK2UTF(keyword)
        self.keyword = keyword
        self.keyword_encoded = self.keyword_encode()
        self.url_begin = 'http://s.weibo.com/weibo/'
        self.page = self.visit()
        self.wb_name_patt = re.compile(r'W_texta.W_fb\\" nick-name=\\"(\\u....){1,20}\\"')
        self.wb_time_patt = re.compile(r'\w{6}=\\"_blank\\" title=\\"[\d| |-]{13}:\d\d\\"')
        self.wb_content_patt = re.compile(r'p class=\\"[\w|_]{11}\\" [\w|-]{9}=\\"[\w|_]{17}\\" [\w|-]{9}=(.*?)\\t\\t(.*?)\\n\\t\\t<\\/p>')
        self.wb_comment_patt = re.compile(r'span class=\\"line S_line1\\">\\u8bc4\\u8bba(.*?)<em>(.*?)<\\/em><\\/span>')
        self.wb_forward_patt = re.compile(r'span class=\\"line S_line1\\">\\u8f6c\\u53d1(.*?)<em>(.*?)<\\/em><\\/span>')
        self.wb_collect_patt = re.compile(r'span class=\\"line S_line1\\">\\u6536\\u85cf(.*?)<em>(.*?)<\\/em><\\/span>')
        self.wb_like_patt = None

    # def GBK2UTF(self, keyword):
    #     self.keyword = keyword.decode('GBK', 'ignore').encode("utf-8")
    #     # print self.keyword

    def keyword_encode(self): # right
        once = urllib.urlencode({"kw":self.keyword})[3:]
        twice = urllib.urlencode({"kw":once})[3:]
        return twice

    def get_url(self):
        return self.url_begin + self.keyword_encoded + '&' + '&Refer=g'

    def findname_reg(self):
        assert self.page != None, "Please read page first"
        names = []
        for name in re.finditer(self.wb_name_patt, self.page):
            names.append(name.group()[27:-1])
            # print name.group()[27:-1]
        return names

    def findtime_reg(self):
        assert self.page != None, "Please read page first"
        times = []
        for time in re.finditer(self.wb_time_patt, self.page):
            times.append(time.group()[26:-1])
            # print time.group()[26:-1]
        return times

    def findcontent_reg(self):
        assert self.page != None, "Please read page first"
        contents = []
        for content in re.finditer(self.wb_content_patt, self.page):
            contents.append(content.group(2))
            # print content.group(2)
        return contents

    def findcollect_reg(self):
        assert self.page != None, "Please read page first"
        collects = []
        for collect in re.finditer(self.wb_collect_patt, self.page):
            if collect.group(2):
                collects.append(collect.group(2))
                # print collect.group(2)
            else:
                collects.append('0')
                # print '0'
        return collects

    def findforward_reg(self):
        assert self.page != None, "Please read page first"
        forwards = []
        for forward in re.finditer(self.wb_forward_patt, self.page):
            if forward.group(2):
                forwards.append(forward.group(2))
                # print forward.group(2)
            else:
                forwards.append('0')
                # print '0'
        return forwards

    def findcomment_reg(self):
        assert self.page != None, "Please read page first"
        comments = []
        for comment in re.finditer(self.wb_comment_patt, self.page):
            if comment.group(2):
                comments.append(comment.group(2))
                # print comment.group(2)
            else:
                comments.append('0')
                # print '0'
        return comments

    def visit(self, isfile=True):
        if isfile:
            page_txt = open('page.txt', 'r')
            page = page_txt.read()
            page_txt.close()
            self.page = page
        else:
            req = urllib2.Request(self.get_url(), headers=headers)
            page = urllib2.urlopen(req).read()
            page_txt = open('page.txt', 'wb')
            page_txt.write(page)
            page_txt.close()
            self.page = page
        return page


def main():
    pass


if __name__ == '__main__':
    main()