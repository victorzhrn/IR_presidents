'''
Created on May 1, 2017

@author: yangr
'''



from bs4 import BeautifulSoup
import os
import json

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
    
        