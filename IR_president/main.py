'''
Created on May 1, 2017

@author: yangr
'''

import sys
from IR.IR_method import BM25, NGram

def print_call(doc):
    print doc
#     for val in doc:
#         print val

def parse(doc, n):
        split = []
        doc_len = len(doc)
        if n == 1:
            return doc
        elif n > doc_len:
            raise Exception('Not enough words! Type help to see available command')
        else:
            for i in range(doc_len - n + 1):
                split += [doc[i: i + n]]
            return split + parse(doc, n - 1)
def main():
    print "Welcome to IR president encyclopedia!"
    print "Type 'help' to see available command"
#     print os.getcwd()
    default_bm_path = '../Data/data_no_stop.json'
    default_skip_path = '../Data/data_nosym_split.json'
    
    bm25 = BM25(NGram(model_path=default_bm_path, n=1))
    skip = BM25(NGram(model_path=default_skip_path, n=2))
    
    while True:
        read = raw_input(">")
        args = read.split()
        
        if len(args) == 0:
            print "Not valid"
        elif args[0] == 'quit' or args[0] == 'q':
            print "Bye!"
            sys.exit(0)
        elif args[0] == 'help':
            print 'bm25: bm  <-a> <query>'
            print 'skipBigram: sk <-a> <query>'
            pass
        elif args[0] == 'bm':
            is_all = False
            arg_num = 1
            if args[1] == '-a':
                is_all = True
                arg_num = 2
            print_call(bm25.search(args[arg_num:], is_all))
        elif args[0] == 'sk':
            is_all = False
            arg_num = 1
            if args[1] == '-a':
                is_all = True
                arg_num = 2
            query = parse(args[arg_num:], 2) + args[arg_num:]
            print_call(skip.search(query, is_all))
        elif args[0] == 'use':
            bm25 = BM25(read[4:])
            skip = NGram(model_path=read[4:], n=2)
        else:
            print  "Not a valid command: " + read

if __name__ == '__main__':
    main()

