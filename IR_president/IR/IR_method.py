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
    def __init__(self, corpus):
        '''
        Constructor
        '''
        if corpus is None:
            raise Exception('Need at least corpus or path to initilaze!')
        self.corpus = corpus
    
    def print_data(self, data):
        pprint(data)
    
    def search(self, query, fullRank=False):
        pass
    
    def setCorpus(self, corpus):
        self.corpus = corpus
    
class BM25(IR_method):
    # doc is the list of word in the document
    def __init__(self, path, k1=1.2, b=0.75):
        # super(BM25, self).__init__(path)
        IR_method.__init__(self, path)
        self.k1 = k1
        self.b = b

    def search(self, q_list, fullRank=False):
        result = []
        for title in self.corpus.get_titles():
            score = self.score(self.corpus.get_doc(title), q_list)
            result += [(title, score)]
        result = sorted(result, key=lambda val: val[1], reverse=True)
        if fullRank:
            return result
        else:
            return result[0]

    def get_idf(self, n, N, base):
        top = N - n + 0.5
        bottom = n + 0.5
        return math.log(top / bottom, base)

    def single_score(self, idf, freq, avdl, doc, n, N, base=10):
        top = freq * (self.k1 + 1.0)
        bottom = freq + self.k1 * (1.0 - self.b + self.b * (float(len(doc)) / avdl))
        return idf * (top / bottom)
    
    def test_scoring(self, idf, freq, avdl_doc_rate, n, N, base=10):
        top = freq * (self.k1 + 1.0)
        bottom = freq + self.k1 * (1.0 - self.b + self.b * avdl_doc_rate)
        return idf * (top / bottom)

    def score(self, doc, q_list, base=10):
        total_score = 0
        for qi in q_list:
            n = self.corpus.get_n(qi)
            N = self.corpus.get_N()
            idf = self.get_idf(n, N, base)
            avdl = self.corpus.avdl
            freq = self.corpus.get_freq(qi, doc)
            total_score += self.single_score(idf, freq, avdl, doc, n, N, base)
        return total_score


class SkipBigram(IR_method):
    
    def search(self, query, fullRank=False):
        IR_method.search(self, query, fullRank=fullRank)

class Corpus:
    def __init__(self, path):
        with open(path) as f:
            self.corpus = json.load(f)
            f.close()
        corpus = {}
        for key in self.corpus.keys():
            k = str(key)
            '''
            Anchor tags are appended with the file text
            '''
            content = (self.corpus[key]).encode('utf-8').split()
            title = k[:-2]
            try:
                corpus[title].append(content)
            except KeyError:
                corpus[title] = content
        self.corpus = corpus        
        self.N = self.count_documents()
        self.avdl = self.get_avdl()
        
    def count_documents(self):
        return len(self.corpus)
    
    def get_titles(self):
        return self.corpus.keys()
    
    def get_doc(self, title):
        return self.corpus[title]
    
    def get_avdl(self):
        keys = self.corpus.keys()
        total = 0.0
        for key in keys:
            total += len(self.corpus[key])
        return total / self.N
    
    def get_n(self, qi):
        count = 0
        for key in self.corpus.keys():
            if qi in self.corpus[key]:
                count += 1
        return count
    
    def get_N(self):
        return self.N
    
    def get_freq(self, qi, doc):
        return doc.count(qi)
    
    def get_doc_avdl(self, doc):
        return float(len(doc)) / self.avdl
