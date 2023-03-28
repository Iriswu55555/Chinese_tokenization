import jieba
import csv
import re
from collections import Counter
from pprint import pprint

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))
import pandas
#coding='utf-8'impo#coding='utf-8'

#停用詞表
def stopwordslist():
    stopwords = [line.strip() for line in open('stopword.txt',encoding='utf-8').readlines()] #停用詞表讀取
    return stopwords
stopwords = stopwordslist()
jieba.set_dictionary('dict_zh_tw.txt')
jieba.load_userdict('userdict.txt')  #userdict 為自訂字典

#檔案存取
a = open('outline.csv','r',encoding='utf-8').read().split('\n')
RS = []
fd =open("token.csv","w")
writer = csv.writer(fd)

for i in range(len(a)):
    result = []
    seg_list = jieba.lcut(a[i], cut_all=False)
    for w in seg_list:
        if w not in stopwords:
            result.append(w)
    RS.append(result)
    writer.writerow(RS)
print(RS)

fd.close()










