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
    return sorted(f for f in os.listdir(f_dir))

def parse_one_file(f_name):
    f_path = f_dir + '/' + f_name
    file = open(f_path)
    soup = BeautifulSoup(file, 'html.parser')
    file.close()
    title = soup.title.string
    a_tag = soup.find_all('a')
    link_list = []
    for a in a_tag:
        if a.get('href') is not None:
            href = a.get('href')
            title = a.get('title')
            link_list.append((href, title))
    print link_list[0]
    print link_list[0][0]
    print link_list[0][1]
    print len(a_tag)

def main():
    f_list = find_file_list()
    print f_list
    print parse_one_file(f_list[0])kK


if __name__ == '__main__':
    main()


