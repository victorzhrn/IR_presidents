'''
Created on May 1, 2017

@author: yangr
'''
import json
from pprint import pprint
import math

class IR_method:
    '''
    classdocs
    '''


    def __init__(self, path=None):
        '''
        Constructor
        '''
        if path is None:
            raise Exception('Need at least corpus or path to initilaze!')
        self.corpus = Corpus(path)
    
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
    
class Corpus:

    def __init__(self, path):
        with open(path) as f:
            self.corpus = json.load(f)

        self.N = self.countDocuments()
        self.avdl = self.getAvdl()
        pass

    def countDocuments(self):
        return len(self.corpus)/2

    def getCorpus(self):
        return self.corpus

    def printFile(self):
        pprint(self.corpus)

    #Word occurs in N documents
    def get_n(self, word):
        pass

    def getFrequence(self, q, doc):
        pass






class BM25(IR_method):

    def __init__(self, path, k1, b):
        super(BM25, self).__init__(path)
        self.k1 = 1.2
        self.b = 0.75

    def search(self, query, fullRank=False):
        # IR_method.search(self, query, fullRank=fullRank)

        pass

    def getAvdl(self):
        keys = self.corpus.keys()
        total = 0
        for key in keys:
            k = str(key)
            if k.endswith('p'):
                total += len(self.corpus[key].split())

        return total / self.N


    def get_IDF(self, q, base=math.e):
        n = self.get_n(q)
        top = self.N - n + 0.5
        bottom = n + 0.5
        return math.log(top / bottom, base)

    def singleScore(self, q, doc):
        idf = self.get_IDF(q)
        freq = self.getFrequence(q, doc)
        # top = freq * self.k +
        pass
        
class SkipBigram(IR_method):
    
    def search(self, query, fullRank=False):
        IR_method.search(self, query, fullRank=fullRank)
