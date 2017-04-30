from bs4 import BeautifulSoup
path = "/Users/yangr/Documents/AI/NLP/Data/Adams.txt"
file = open(path)
content = file.read()
soup = BeautifulSoup(content, 'html.parser')

#soup.title.string
#soup.getText()
