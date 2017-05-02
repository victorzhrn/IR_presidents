'''
    Create by xuez May 2nd 2017
    This script is for data pre processing
'''

from bs4 import BeautifulSoup
import os
import json

# global variables
f_dir = "../../Presidents"


def find_file_list():
    file_list = os.listdir(f_dir)
    return file_list

def parse_one_file(f_name):
    f_path = f_dir + '/' + f_name
    file = open(f_path)
    soup = BeautifulSoup(file, 'html.parser')
    file.close()
    title = soup.title.string
    a_tag = soup.find_all('a')
    print "a tag", a_tag
    print "a tag string", a_tag[1].string
    print "a tag len", len(a_tag)
    print "soup content", soup.contents

def main():
    f_list = find_file_list()
    print f_list
    print parse_one_file(f_list[0])


if __name__ == '__main__':
    main()


