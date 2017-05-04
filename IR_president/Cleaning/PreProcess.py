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
target_dir = "../../Data/"


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
    return soup

def extract_links(soup, f_name):
    a_tag = soup.find_all('a')
    external_link_list = []
    internal_link_list = []
    external_link_titles = []
    for a in a_tag:
        if a.get('href') is not None:
            href = a.get('href')
            title = a.get('title')
            if not need_to_ignore(href):
                if href.startswith("/wiki"):
                    if title is not None:
                        external_link_list.append((href.encode('ascii', 'ignore'), title.encode('ascii', 'ignore')))
                        external_link_titles.append(title.encode('ascii', 'ignore'))
                elif href.startswith("#"):
                    internal_link_list.append(href.encode('ascii', 'ignore')[1:].replace('_', ' '))
    link_dict = {}
    link_dict[f_name[:-4] + "external"] = external_link_list
    internal_link_list = internal_link_list[1:]
    link_dict[f_name[:-4] + "internal"] = internal_link_list
    # uncomment this part for deploy
#     with open(f_name[:-4] + '_links.json', 'w') as fp:
#         json.dump(link_dict, fp)
#     with open(f_name[:-4] + '_external.json', 'w') as fp:
#         json.dump(external_link_list, fp)
#     with open(f_name[:-4] + '_internal.json', 'w') as fp:
#         json.dump(internal_link_list, fp)

    return external_link_list, external_link_titles, internal_link_list

def get_content(soup, file):
    key = file[:-4]
    contents = soup.find(id='mw-content-text').find_all('p')
    paragraph_dict = {}
    paragraph_list = []
    for content in contents:
        paragraph = ""
        for string in content.stripped_strings:
            paragraph += string.encode('ascii', 'ignore').replace('\"', ' ') + ' '
        paragraph = re.sub('[\[[][\ ][0-9]+[\ ]]', ' ', paragraph)
        paragraph_list.append(paragraph)
    paragraph_dict[key] = paragraph_list
#     with open(key + '_paragraph.json', 'w') as fp:
#         json.dump(paragraph_dict, fp)

    return paragraph_list



def main():
    f_list = find_file_list()
    for file in f_list:
        president_dict = {}
        soup = parse_one_file(file)
        e_links, e_titles, i_links = extract_links(soup, file)
        p_list = get_content(soup, file)
        president_dict['name'] = file[:-4]
        president_dict['internal_links'] = i_links
        president_dict['paragraphes'] = p_list
        with open(target_dir + file[:-4] + '.json', 'w') as fp:
            json.dump(president_dict, fp)





if __name__ == '__main__':
    main()


