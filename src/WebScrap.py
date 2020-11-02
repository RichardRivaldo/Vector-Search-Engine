import requests
import csv
import re
from bs4 import BeautifulSoup

# fungsi konversi string menjadi list of char
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def webScrap() :
    page = requests.get('https://www.reuters.com/news/archive/indonesia').text
    page2 = requests.get('https://www.reuters.com/news/archive/indonesia?view=page&page=2&pageSize=10').text
    page3 = requests.get('https://www.reuters.com/news/archive/indonesia?view=page&page=3&pageSize=10').text
    soup = BeautifulSoup(page, 'lxml')
    soup2 = BeautifulSoup(page2, 'lxml')
    soup3 = BeautifulSoup(page3, 'lxml')

    TLink = []
    for list in soup.find_all('article', class_='story') :
        link = list.find('a')
        if (link != -1) :
            linkh = link['href']
            TLink.append('https://www.reuters.com'+linkh)

    for list in soup2.find_all('article', class_='story') :
        link = list.find('a')
        if (link != -1) :
            linkh = link['href']
            TLink.append('https://www.reuters.com'+linkh)

    for list in soup3.find_all('article', class_='story') :
        link = list.find('a')
        if (link != -1) :
            linkh = link['href']
            TLink.append('https://www.reuters.com'+linkh)


    for linki in TLink :
        pagei = requests.get(linki).text
        soupi = BeautifulSoup(pagei, 'lxml')

        content = []
        for h1  in soupi.find_all('h1') :
            headline = h1.text
        for p in soupi.find('div', class_='ArticleBodyWrapper').find_all('p') :
            paragraph = p.text
            content.append(paragraph)

        headlist = Convert(headline)
        for i in range(len(headlist)) :
            if headlist[i] == ':' :
                headlist[i] = ''
            if headlist[i] == '?' :
                headlist[i] = ''

        headline = ''.join(headlist)

        exportFile = open(headline+'.txt',"w", encoding='utf-8')
        exportFile.write(' '.join(content))
        exportFile.close()


webScrap()