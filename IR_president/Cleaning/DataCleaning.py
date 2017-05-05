'''
Created on May 1, 2017

@author: yangr
'''



from bs4 import BeautifulSoup
import os
import json, re



def find_type(type, soup):
    all_p = ""
    p = soup.find(type)
    while not p==None:
        if not p.string == None:
            all_p+=p.string
        p= p.find_next(type)
    return all_p

def clean(filePath, writePath):
    os.chdir("\Users\yangr\Documents\AI\IR_presidents")
    dir = "Presidents/"
    parsedDir = "/Data/"
    dict = {}
    all_presidents = []
    for file in os.listdir(dir):
        if file.endswith(".txt"):
            path = dir+file
            file = open(path)
            content = file.read()
            soup = BeautifulSoup(content, 'html.parser')
            title = (soup.title.string)
            dict[title+"_p"]= find_type("p",soup)
            dict[title+"_a"] = find_type("a",soup)
            
    with open(parsedDir+ 'data.json', 'w') as fp:
        json.dump(dict, fp)
    
    
import codecs
fi = json.load(codecs.open('data.json', 'r', 'utf-8-sig'))


data = {}
for key in fi.keys():
    content = " ".join(fi[key]['anchors'])
    content2 = " ".join(fi[key]['p'])
    total = content + ' ' + content2
    strip = re.sub(r'[^\w]', ' ', total)
    
    
stop_list = {}
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
for key in data.keys():
    p = data[key]
    word_list = [i for i in p.lower().split() if i not in stop]
    stop_list[key] = word_list
    
with open('data_no_stop.json', 'w') as fp:
    json.dump(data, fp)


    
    