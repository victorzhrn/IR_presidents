'''
Created on May 1, 2017

@author: yangr
'''

import sys, os
from IR.IR_method import BM25, SkipBigram, Corpus
# path = ""
# 


def main():
    print "Welcome to IR president encyclopedia!"
#     print os.getcwd()
    default_path = '../Data/data.json'
    corp = Corpus(default_path)
    bm25 = BM25(corp)
    skip = SkipBigram(corp)
    
    while True:
        read = raw_input(">")
        args = read.split()
        
        if args[0] == 'quit' or args[0]=='q':
            print "Bye!"
            sys.exit(0)
        elif args[0] == 'help':
            print 'help'
            pass
        elif args[0] == 'bm25':
            print bm25.search(args[1:])
        elif args[0] == 'skipBigram':
            print skip.search(args[1:])
        elif args[0] == 'use':
            bm25 = BM25(read[4:])
            skip = SkipBigram(read[4:])
        elif args[0] == 'ba':
            result = bm25.search('John Adams second President He was a lawyer', True)
            for r in result:
                print r
        elif args[0] == 'b':
            print bm25.search('John Adams')
        else:
            print  "Not a valid command: " + read
    pass


if __name__ == '__main__':
    main()

