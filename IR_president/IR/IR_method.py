'''
Created on May 1, 2017

@author: yangr
'''
import json
from pprint import pprint
import math
import re
import sys

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
        self.corpus = Corpus(path).getCorpus()
    
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

        # self.N = self.countDocuments()
        # self.avdl = self.getAvdl()
        pass

    def getCorpus(self):
        return self.corpus

    def printFile(self):
        pprint(self.corpus)





class BM25(IR_method):

    #doc is the list of word in the document

    def __init__(self, path, k1=1.2, b=0.75):
        # super(BM25, self).__init__(path)
        IR_method.__init__(self,path)
        self.k1 = k1
        self.b = b
        self.N = self.countDocuments()
        self.avdl = self.getAvdl()

    def countDocuments(self):
      return len(self.corpus) / 2

    def search(self, q_list, fullRank=False):
        # IR_method.search(self, query, fullRank=fullRank)
        score_dict={}
        for key in self.corpus.keys():
            k = str(key)
            if k.endswith('p'):
              s = self.score(self.corpus[(key)],q_list)
              score_dict[key]=s

        if fullRank:
          return score_dict

        else:
          maxkey = None
          maxtem = -sys.maxint
          for k in score_dict.keys():
            if (score_dict[key]>maxtem):
              maxkey = key
              maxtem = score_dict[key]
          return {maxkey,maxtem}

    def getAvdl(self):
        keys = self.corpus.keys()
        total = 0
        for key in keys:
            k = str(key)
            if k.endswith('p'):
                total += len(self.corpus[key].split())
        return total / self.N

    def get_idf(self, q, base=math.e):
        n = self.get_n(q)
        top = self.N - n + 0.5
        bottom = n + 0.5
        return math.log(top / bottom, base)

    def single_score(self, q, doc):
        idf = self.get_idf(q)
        freq = self.get_frequence(q, doc)
        top = freq * (self.k1 + 1)
        bottom = freq + self.k1 * (1 - self.b + self.b * (len(doc) / self.avdl))
        return idf * (top / bottom)

    # Word occurs in N documents
    def get_n(self, q):
      keys = self.corpus.keys()
      total = 0
      for key in keys:
        k = str(key)
        if k.endswith('p') and q in self.corpus[key]:
          total += 1
      return total

    def get_frequence(self, q, doc):
        return doc.count(q)

    def score(self, doc, q_list):
        total_score = sum(self.single_score(q, doc) for q in q_list)
        return total_score

class SkipBigram(IR_method):
    
    def search(self, query, fullRank=False):
        IR_method.search(self, query, fullRank=fullRank)
