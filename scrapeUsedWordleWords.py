import requests
from bs4 import BeautifulSoup
import os

r = requests.get('https://www.rockpapershotgun.com/wordle-past-answers')
soup = BeautifulSoup(r.content, 'html.parser')

prevUsedWords = []
for ultag in soup.find_all('ul', {'class': 'inline'}):
    for litag in ultag.find_all('li'):
        prevUsedWords.append(litag.text)

with open('./{}.txt'.format("usedWords"), mode='wt', encoding='utf-8') as file:
    for i in prevUsedWords:
        file.write(i+"\n")

