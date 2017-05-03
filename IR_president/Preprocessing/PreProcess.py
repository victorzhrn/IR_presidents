'''
    Create by xuez May 2nd 2017
    This script is for data pre processing
'''

from bs4 import BeautifulSoup
import os
import json
import re

# global variables
f_dir = "../../Presidents"


def find_file_list():
    return sorted(f for f in os.listdir(f_dir))


def need_to_ignore(href):
    href = href.encode('ascii', 'ignore')

    # if href.startswith('#cite') or href.startswith("/wiki/File:") or \
    #     href.startswith("/wiki/Wikipedia") or href.startswith("#mw") or \
    #     href.startswith("http") or href.startswith("/wiki/Special") or \
    #     href.startswith("/wiki/International_Standard_Book_Number") or \
    #     href.startswith("//") or href.startswith("/wiki/Category") or \
    #     href.startswith("/w/"):
    #     return True
    if re.match(r'.wiki.*[:]', href) or href.startswith("#cite") or \
            href.startswith("#CITE") or href.startswith("#See_also") or \
            href.startswith("#Notes") or href.startswith("#References") or \
            href.startswith("#External_links") or \
            href.startswith("http") or href.startswith("#mw") or \
            href.startswith("//") or href.startswith("/w/") or \
            href.startswith("/wiki/International_Standard_Book_Number"):
        return True
    else:
        return False


def parse_one_file(f_name):
    f_path = f_dir + '/' + f_name
    file = open(f_path)
    soup = BeautifulSoup(file, 'html.parser')
    file.close()
    a_tag = soup.find_all('a')
    external_link_list = []
    internal_link_list = []
    for a in a_tag:
        if a.get('href') is not None:
            href = a.get('href')
            title = a.get('title')
            if not need_to_ignore(href):
                if href.startswith("/wiki"):
                    if title is not None:
                        external_link_list.append((href.encode('ascii', 'ignore'), title.encode('ascii', 'ignore')))
                elif href.startswith("#"):
                    internal_link_list.append(href.encode('ascii', 'ignore'))
    link_dict = {}
    link_dict[f_name[:-4] + "external"] = external_link_list
    link_dict[f_name[:-4] + "internal"] = internal_link_list[1:]
    # uncomment this part for deploy
    # with open(f_name[:-4] + '_links.json', 'w') as fp:
    #     json.dump(link_dict, fp)
    # with open(f_name[:-4] + '_external.json', 'w') as fp:
    #     json.dump(external_link_list, fp)
    # with open(f_name[:-4] + '_internal.json', 'w') as fp:
    #     json.dump(internal_link_list, fp)

    return external_link_list, internal_link_list

def get_internal_link_info(link):




def main():
    f_list = find_file_list()
    # print f_list
    # for file in f_list:
    #     external_link, internal_link = parse_one_file(file)
    #     print file
    #     print "ext", len(external_link)
    #     print "int", len(internal_link)
    e_links, i_links = parse_one_file(f_list[0])
    print len(e_links)
    print i_links



if __name__ == '__main__':
    main()


