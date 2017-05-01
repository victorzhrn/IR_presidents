'''
Created on May 1, 2017

@author: yangr
'''
import json
from pprint import pprint
class IR_method:
    '''
    classdocs
    '''


    def __init__(self, corpus=None, path=None):
        '''
        Constructor
        '''
        if corpus is None and path is None:
            raise Exception('Need at least corpus or path to initilaze!')
        self.corpus = corpus
    
    def readFile(self, path):
        with open(path) as json_data:
            d = json.loads(json_data)
            json_data.close()
        self.corpus = d
    
    def print_corpus(self, data):
        pprint(data)
    
    def search(self, query, fullRank=False):
        pass
    
    def setCorpus(self, corpus):
        self.corpus = corpus
    

class BM25(IR_method):

    def search(self, query, fullRank=False):
        IR_method.search(self, query, fullRank=fullRank)
        
class SkipBigram(IR_method):
    
    def search(self, query, fullRank=False):
        IR_method.search(self, query, fullRank=fullRank)
