import requests
from bs4 import BeautifulSoup
import os

pages = []
pages.append('https://www.bestwordlist.com/5letterwords.htm')
for i in range(2,16):
   pages.append(str('https://www.bestwordlist.com/5letterwordspage{}.htm').format(i))

total = []

for w in range(0,len(pages)):
    r = requests.get(pages[w])

    soup = BeautifulSoup(r.content, 'html.parser')

    for ultag in soup.find_all('span', {'class': 'mot'}):
            for i in ultag:
                x = i.split()
                for word in x:
                    total.append(str(word))

    for ultag in soup.find_all('span', {'class': 'mot2'}):
            for i in ultag:
                x = i.split()
                for word in x:
                    total.append(str(word))


with open('./{}.txt'.format("potentialWords"), mode='wt', encoding='utf-8') as file:
    for i in range(0,len(total)):
        file.write(total[i]+"\n")
    