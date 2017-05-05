'''
Created on May 1, 2017

@author: yangr
'''

import sys
from IR.IR_method import BM25, NGram
# path = ""
# 


def main():
    print "Welcome to IR president encyclopedia!"
#     print os.getcwd()
    default_bm_path = '../Data/data_no_stop.json'
    default_skip_path = '../Data/data_nosym_split.json'
    
    bm25 = BM25(NGram(model_path=default_bm_path,n=1))
    skip = BM25(NGram(model_path=default_skip_path,n=2))
    
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
            is_all = False
            arg_num = 1
            if args[1] == '-a':
                is_all = True
                arg_num = 2
            print bm25.search(args[arg_num:], is_all)
        elif args[0] == 'skipBigram':
            print skip.search(args[1:])
        elif args[0] == 'use':
            bm25 = BM25(read[4:])
            skip = NGram(model_path=read[4:],n=2)
        elif args[0] == 'ba':
            result = bm25.search('John Adams second President He was a lawyer'.lower(), True)
            for r in result:
                print r
        elif args[0] == 'b':
            print bm25.search('John Adams')
        else:
            print  "Not a valid command: " + read
    pass


if __name__ == '__main__':
    main()

