# -*- coding: utf-8 -*-
import pandas as pd
import re
import jieba
import jieba.analyse
from collections import Counter
import sys
import time
import jieba.posseg as pseg
import keywords_new
reload(sys)
sys.setdefaultencoding('utf-8')


f = open("YOUR_USER_ID", "r")
f1 = open("category.txt", "w")
f2 = open("express.txt", "w")
f3 = open("word.txt", "w")
f4 = open("name.txt", "w")
list1 = []
record = {}  # 记录命中信息
express = {}
name_set = {}
while True:
    line = f.readline().strip().decode('utf-8')
    if line:
        item = line.split(' ', 1)[1]
        ex_all = re.findall(u"\\[.*?\\]", item)
        if ex_all:
            for ex_item in ex_all:
                express[ex_item] = express.get(ex_item, 0) + 1
        for kw, keywords in keywords_new.keyword_dict.iteritems():  # kw是大类
            flag = 0  # 大类命中的标志
            for key, keyword in keywords.iteritems():  # key 是小类
            	if flag == 1:
            		break
                for word in keyword:  # 小类关键词
                    match_flag = 1  # 列表中关键词全部命中的标志
                    for small_word in word:  # 关键词列表
#                    	print small_word
                        match = re.search(re.compile(small_word, re.I), item)
                        if not match:
                            match_flag = 0
                            break
                    if match_flag == 1:  #命中了一个小类
                        record[kw] = record.get(kw, 0) + 1 # 单次记录
                        flag = 1
                        break
        item = re.sub(u"\\[.*?\\]", '', item)
        list = jieba.cut(item, cut_all = False)
        for ll in list:
            list1.append(ll)  # 分词
        seg_list = pseg.cut(item)
        for word, flag in seg_list:
            if flag == 'nr':
                name_set[word] = name_set.get(word, 0) + 1
    else:
        break

count = Counter(list1)
for item in sorted(dict(count).iteritems(), key=lambda d:d[1], reverse = True):
    if len(item[0]) >= 2 and item[1] >= 3:
        print >> f3, item[0],item[1]

for key, keywords in sorted(record.iteritems(), key=lambda d:d[1], reverse = True):
    print >> f1, u'命中了', key, record[key], u'次'

for key, keywords in sorted(express.iteritems(), key=lambda d:d[1], reverse = True):
    print >> f2, u'使用了', key, u'表情', express[key], u'次'

for key, keywords in sorted(name_set.iteritems(), key=lambda d:d[1], reverse = True):
    print >>f4, u'使用了名字', key, name_set[key], u'次'
