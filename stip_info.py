from bs4 import BeautifulSoup
import os

def find_type(type, soup):
    all_p = ""
    p = soup.find(type)
    while not p==None:
        if not p.string == None:
            all_p+=p.string
        p= p.find_next(type)
    return all_p

dir = "/Users/ruinanzhang/Desktop/OneDrive/myGit/IR_presidents/Presidents"
dict = {}
all_presidents = []
for file in os.listdir(dir):
    if file.endswith(".txt"):
        path = "Presidents/"+file

        file = open(path)
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        title = (soup.title.string)
        dict[title+"_p"]= find_type("p",soup)
        dict[title+"_a"] = find_type("a",soup)
        print soup.title.string
        # dict[title+"_h"] = find_type("h",soup)

