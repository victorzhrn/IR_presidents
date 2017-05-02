'''
Created on May 1, 2017

@author: yangr
'''

import sys, os
from IR.IR_method import BM25, SkipBigram
# path = ""
# 


def main():
    print "Welcome to IR president encyclopedia!"
    print os.getcwd()
    default_path = '../Data/data.json'
    
    bm25 = BM25(default_path)
    skip = SkipBigram(default_path)
    
    
    while True:
        read = str(sys.stdin.readline())
        args = read.split()
        if args[0] == 'quit':
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
        else:
#             CRED = '\33[31m'
#             CEND = '\33[0m'
            print  "Not a valid command: " + read.strip()
    pass


if __name__ == '__main__':
    main()