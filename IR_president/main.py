'''
Created on May 1, 2017

@author: yangr
'''

import sys, os

# path = ""
# 
# with open(path) as f:
#     corpus = json.load(f)

def main():
    print "Welcome to IR president encyclopedia!"
    print os.getcwd()
    default_path = '../Data/data.json'
    
    while True:
        line = sys.stdin.readline()
        line = str(line).split()
        if line[0] == 'quit':
            sys.exit(0)
        elif line[0] == 'help':
            print 'help'
            pass
        else:
            print str(line).strip()
    pass


if __name__ == '__main__':
    main()