import unittest
from IR.IR_method import BM25, SkipBigram, Corpus


class MyTestCase(unittest.TestCase):


#     def test_something(self):
#         default_path = '../Data/data.json'
#         bm25 = BM25(default_path)
#         bm25.N = 500000.0
#         self.assertEqual(True, False)
    
#     def test_corpus(self):
#         path = '../../Data/data.json'
#         corp = Corpus(path)
# 
# #         for i in range(10):
# #             print corp.anchors[i]
#         print corp.documents[1]  
#         print len(corp.documents)
    
    def test_bm25(self):
#         path = '../../Data/data.json'
#         corp = Corpus(path)
        bm25 = BM25("Test")
        n_p = 40000
        n_l = 300
        N = 500000
        p_idf = bm25.get_idf(n_p, N, 10)
        l_idf = bm25.get_idf(n_l, N, 10) 
        president = bm25.test_scoring(p_idf, 15, 0.9, n_p, N, 10)
        lincoln = bm25.test_scoring(l_idf, 25, 0.9, n_l, N, 10)
        
        self.assertAlmostEqual(round(president + lincoln, 2) , 8.96)
    


if __name__ == '__main__':
    unittest.main()
