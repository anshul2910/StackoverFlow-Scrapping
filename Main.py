from bs4 import BeautifulSoup
# import selenium
import requests
import re

url = 'https://stackoverflow.com/search?tab=Relevance&pagesize=50&q=ubuntu'
r = requests.get(url)
html_doc = r.text 
soup = BeautifulSoup(html_doc, 'lxml')

links = []
for link in soup.find_all('a'):
    links.append((link.get('href')))


question_links = [k for k in links if k and 'questions' in k]
pattern = re.compile('/questions/\d')
question_links = filter(pattern.search, question_links)
question_links = list(question_links)

# print(len(question_links))

final =[]
for i in range(50):
    final.append("https://stackoverflow.com"+question_links[i])


print(len(final))

# print(final, end ="\n")

#writing links to text file of first page.
with open('Question_Links.txt', 'w') as f:
    for item in final:
        f.write("%s\n" % item)
