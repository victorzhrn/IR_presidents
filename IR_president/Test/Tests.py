import unittest
from IR.IR_method import BM25, SkipBigram

class MyTestCase(unittest.TestCase):


    def test_something(self):
        default_path = '../Data/data.json'
        bm25 = BM25(default_path)
        bm25.N = 500000.0
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
