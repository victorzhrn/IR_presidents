import unittest
from IR.IR_method import BM25, SkipBigram, Corpus


class MyTestCase(unittest.TestCase):


#     def test_something(self):
#         default_path = '../Data/data.json'
#         bm25 = BM25(default_path)
#         bm25.N = 500000.0
#         self.assertEqual(True, False)
    
    def test_corpus_2(self):
        path = '../../Data/data.json'
        corp = Corpus(path)

#         for i in range(10):
#             print corp.anchors[i]
        print corp.documents[1]  
        print len(corp.documents)
    
#     def test_corpus(self):
#         path = '../../Data/data.json'
#         corp = Corpus(path)
#         for i in corp.documents:
#             print str(i)
#         pass


if __name__ == '__main__':
    unittest.main()
